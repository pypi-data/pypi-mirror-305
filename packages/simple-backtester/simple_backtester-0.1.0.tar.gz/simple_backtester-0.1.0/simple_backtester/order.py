from typing import Union, Optional
from .types import ORDER_STATUS, ORDER_TYPE
import pandas as pd
from abc import abstractmethod


class Order:
    status: ORDER_STATUS
    order_type: ORDER_TYPE
    buy_price: float
    sell_price: float
    take_profit: float
    stop_loss: float
    stake: float

    date_opened: pd.Timestamp
    date_closed: pd.Timestamp
    date_created: pd.Timestamp

    entry_price: float
    _current_price: float
    exit_price: float

    _val_col: str
    _high_col: str
    _low_col: str

    expiry_time: Union[str, pd.Timestamp, None]

    def __init__(
        self,
        order_type: ORDER_TYPE,
        create_time: pd.Timestamp,
        take_profit: float,
        stop_loss: float,
        buy_price: Optional[float] = None,
        sell_price: Optional[float] = None,
        stake: float = 1,
        price_col: str = "close",
        high_col: str = "high",
        low_col: str = "low",
        expiry_time: Union[str, pd.Timestamp, pd.Timedelta, None] = None,
    ):
        self.status = ORDER_STATUS.SUBMITTED
        self.order_type = order_type
        self.date_created = create_time

        self.stake = stake

        self.buy_price = buy_price
        self.sell_price = sell_price
        self.take_profit = take_profit
        self.stop_loss = stop_loss

        self._val_col = price_col
        self._high_col = high_col
        self._low_col = low_col

        self.entry_price = buy_price or sell_price
        self._current_price = self.entry_price

        if expiry_time:
            if type(expiry_time) == pd.Timedelta:
                self.expiry_time = create_time + expiry_time
            else:
                self.expiry_time = expiry_time
        else:
            self.expiry_time = None

    def _check_expiry(self, current_date: pd.Timestamp):
        if self.status == ORDER_STATUS.SUBMITTED:
            if self.expiry_time <= current_date:
                self.status = ORDER_STATUS.EXPIRED
                return True
        return False

    # Returns any changes to portfolio if there are any
    @abstractmethod
    def _check(self, new_value: pd.Series, current_balance: float, on_change_callback):
        pass

    @property
    def current_value(self) -> float:
        if self.status == ORDER_STATUS.SUBMITTED:
            return 0
        last_val = (self._current_price or self.exit_price) * self.stake
        entry_val = self.entry_price * self.stake
        delta = last_val - entry_val
        if (
            self.order_type == ORDER_TYPE.SELL
            or self.order_type == ORDER_TYPE.SELL_LIMIT
        ):
            delta *= -1
        return entry_val + delta

    @property
    def realized_value(self) -> float:
        if self.status == ORDER_STATUS.OPEN:
            return self.entry_price * self.stake

        if (
            self.status == ORDER_STATUS.EXECUTED_LOSS
            or self.status == ORDER_STATUS.EXECUTED_PROFIT
        ):
            return self.exit_price * self.stake

        return 0

    @property
    def is_expired(self) -> bool:
        return self.status == ORDER_STATUS.EXPIRED


class MarketOrder(Order):
    def __init__(self, **kwargs):
        order_type = kwargs["order_type"]
        assert (
            order_type == ORDER_TYPE.BUY or order_type == ORDER_TYPE.SELL
        ), "Unacceptable order type {}. Acceptable types for market orders are BUY and SELL.".format(
            order_type
        )

        try:
            kwargs["buy_price"] = kwargs.pop("buy_stop")
        except KeyError:
            pass

        try:
            kwargs["sell_price"] = kwargs.pop("sell_stop")
        except KeyError:
            pass

        super().__init__(**kwargs)

    def _check(self, new_value: pd.Series, current_balance: float, on_change_callback):
        self._current_price = new_value[self._val_col]
        low_price = new_value[self._low_col]
        high_price = new_value[self._high_col]

        # If order has expired
        if self.expiry_time:
            if self._check_expiry(new_value.name):
                return self

        #### Buy orders
        if self.order_type == ORDER_TYPE.BUY:
            # Check if order has been opened
            if self.status == ORDER_STATUS.SUBMITTED:
                # Open order
                if (
                    self.buy_stop <= self._current_price
                    and self._current_price * self.stake <= current_balance
                ):
                    self.status = ORDER_STATUS.OPEN
                    self.entry_price = self._current_price
                    self.date_opened = new_value.name
                    on_change_callback(self)

            if self.status == ORDER_STATUS.OPEN:
                ### Close
                # Stop loss
                if low_price <= self.stop_loss:
                    self.status = ORDER_STATUS.EXECUTED_LOSS
                    self.exit_price = self.stop_loss
                    self.date_closed = new_value.name
                    on_change_callback(self)

                # Take profit
                elif self.take_profit <= high_price:
                    self.status = ORDER_STATUS.EXECUTED_PROFIT
                    self.exit_price = self.take_profit
                    self.date_closed = new_value.name
                    on_change_callback(self)

                # Nothing, buy order is still open
                else:
                    pass

        #### Sell orders
        else:
            if self.status == ORDER_STATUS.SUBMITTED:
                if (
                    self.sell_stop >= self._current_price
                    and self._current_price * self.stake <= current_balance
                ):
                    self.status = ORDER_STATUS.OPEN
                    self.entry_price = self._current_price
                    self.date_opened = new_value.name
                    on_change_callback(self)

            if self.status == ORDER_STATUS.OPEN:
                if high_price >= self.stop_loss:
                    self.status = ORDER_STATUS.EXECUTED_LOSS
                    self.exit_price = self.stop_loss
                    self.date_closed = new_value.name
                    on_change_callback(self)

                elif self.take_profit >= low_price:
                    self.status = ORDER_STATUS.EXECUTED_PROFIT
                    self.exit_price = self.take_profit
                    self.date_closed = new_value.name
                    on_change_callback(self)

                # Nothing, sell order is still open
                else:
                    pass
        return self

    @property
    def buy_stop(self):
        return self.buy_price

    @property
    def sell_stop(self):
        return self.sell_price


class LimitOrder(Order):
    def __init__(
        self,
        buy_limit: Optional[float] = None,
        sell_limit: Optional[float] = None,
        **kwargs
    ):
        order_type = kwargs["order_type"]
        assert (
            order_type == ORDER_TYPE.BUY_LIMIT or order_type == ORDER_TYPE.SELL_LIMIT
        ), "Unacceptable order type {}. Acceptable types for limit orders are BUY and SELL.".format(
            order_type
        )

        if not (buy_limit or sell_limit):
            raise ValueError("Sell limit and buy limit can't be empty in limit orders")

        kwargs["buy_price"] = buy_limit
        kwargs["sell_price"] = sell_limit

        super().__init__(**kwargs)

    def _check(self, new_value: pd.Series, current_balance: float, on_change_callback):
        raise NotImplementedError("Limit orders not implemented yet")

    @property
    def buy_limit(self):
        return self.buy_price

    @property
    def sell_limit(self):
        return self.sell_limit
