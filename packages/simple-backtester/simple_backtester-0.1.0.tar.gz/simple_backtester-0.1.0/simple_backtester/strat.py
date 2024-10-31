from .data import *
from .types import *
from .order import *
from abc import abstractmethod
import numpy as np
from tqdm import tqdm


class SBStrat:
    balance: float  # Liquidity
    portfolio: float
    _current_orders: List[Order]
    closed_orders: List[Order]
    _price_type: PRICE_TYPE
    price_col: str
    main_datasrc: SBDataSrc

    def __init__(
        self, balance: float = 1000.0, price_type: PRICE_TYPE = PRICE_TYPE.CLOSE
    ):
        print(f"balance: {balance}")
        self.balance = balance
        self.portfolio = balance
        self._current_orders = []
        self.closed_orders = []
        self._price_type = price_type

    def add_data(
        self,
        data: Union[pd.DataFrame, SBDataSrc],
        name: Optional[str] = None,
        main_source: bool = True,
        open_col: Union[str, int] = "open",
        high_col: Union[str, int] = "high",
        low_col: Union[str, int] = "low",
        close_col: Union[str, int] = "close",
        date_col: Union[str, int] = "date",
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        date_fmt: Optional[str] = None,
    ):
        if main_source:
            if type(data) == SBDataSrc:
                self.main_datasrc = data

            else:
                self.main_datasrc = SBDataSrc(
                    data=data,
                    open_col=open_col,
                    high_col=high_col,
                    low_col=low_col,
                    close_col=close_col,
                    start_date=start_date,
                    end_date=end_date,
                    date_col=date_col,
                    date_fmt=date_fmt,
                )

            if self._price_type == PRICE_TYPE.CLOSE:
                self.price_col = self.main_datasrc.close_col
            elif self._price_type == PRICE_TYPE.OPEN:
                self.price_col = self.main_datasrc.open_col
            else:
                raise NotImplementedError(
                    "Alternative columns for order prices have not been implemented yet."
                )

        else:
            if not name:
                raise ValueError("For non-main data sources, name must be specified")
            self.__dict__[name] = data

    def reset(self):
        self.main_datasrc.reset()

    def buy(
        self,
        buy_stop: Optional[float] = None,
        take_profit: Optional[float] = None,
        stop_loss: Optional[float] = None,
        stake: float = 1,
        expiry_time: Union[str, pd.Timestamp, None] = None,
    ) -> MarketOrder:
        row = self.main_datasrc.current_row

        # If buy stop not specified, buy now
        buy_price = row[self.price_col]
        if buy_stop:
            buy_price = buy_stop

        # TP/SL validation
        if take_profit:
            if buy_price > take_profit:
                raise ValueError(
                    "Take profit cannot be less than buy price in buy orders. ({} > {take_profit})".format(
                        buy_price, take_profit
                    )
                )
        else:
            take_profit = np.inf

        if stop_loss:
            if stop_loss > buy_price:
                ValueError(
                    "Stop loss cannot be higher than buy price in buy orders. ({} > {})".format(
                        stop_loss, buy_price
                    )
                )
        else:
            stop_loss = -np.inf

        # Create new order
        new_order = MarketOrder(
            order_type=ORDER_TYPE.BUY,
            create_time=row.name,
            buy_stop=buy_price,
            take_profit=take_profit,
            stop_loss=stop_loss,
            price_col=self.price_col,
            stake=stake,
            high_col=self.main_datasrc.high_col,
            low_col=self.main_datasrc.low_col,
            expiry_time=expiry_time,
        )

        self._current_orders.append(new_order)
        return new_order

    def sell(
        self,
        sell_stop: Optional[float] = None,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        stake: float = 1,
        expiry_time: Union[str, pd.Timestamp, None] = None,
    ) -> MarketOrder:
        row = self.main_datasrc.current_row

        # If sell price not specified, sell now
        sell_price = row[self.price_col]
        if sell_stop:
            sell_price = sell_stop

        # TP/SL validation
        if take_profit:
            if sell_stop < take_profit:
                raise ValueError(
                    "Take profit cannot be more than sell price in sell orders. ({} > {})".format(
                        take_profit, sell_stop
                    )
                )
        else:
            take_profit = -np.inf

        if stop_loss:
            if stop_loss < sell_stop:
                raise ValueError(
                    "Stop loss cannot be less than sell price in sell orders. ({} > {})".format(
                        sell_stop, stop_loss
                    )
                )
        else:
            stop_loss = np.inf

        # Create new order
        new_order = MarketOrder(
            order_type=ORDER_TYPE.SELL,
            create_time=row.name,
            sell_stop=sell_price,
            take_profit=take_profit,
            stop_loss=stop_loss,
            price_col=self.price_col,
            stake=stake,
            high_col=self.main_datasrc.high_col,
            low_col=self.main_datasrc.low_col,
            expiry_time=expiry_time,
        )

        self._current_orders.append(new_order)
        return new_order

    def buy_limit(
        self,
        buy_limit: float,
        take_profit: Optional[float] = None,
        stop_loss: Optional[float] = None,
        stake: float = 1,
        expiry_time: Union[str, pd.Timestamp, None] = None,
    ) -> LimitOrder:
        raise NotImplementedError("Buy limit orders not implemented yet")

    def sell_limit(
        self,
        sell_limit: float,
        take_profit: Optional[float] = None,
        stop_loss: Optional[float] = None,
        stake: float = 1,
        expiry_time: Union[str, pd.Timestamp, None] = None,
    ) -> LimitOrder:
        raise NotImplementedError("Sell limit orders not implemented yet")

    @abstractmethod
    def on_order_change(self, order: Order):
        pass

    def _eval_orders(self, new_row: pd.Series) -> float:
        open_portfolio: float = 0
        closed_orders = []

        for order in self._current_orders:
            old_status = order.status
            order = order._check(new_row, self.balance, self.on_order_change)

            # Order status has changed, pnl is realized
            if order.status != old_status:
                # Submitted order has been expired
                if order.status == ORDER_STATUS.EXPIRED:
                    closed_orders.append(order)

                # Order has been opened
                elif order.status == ORDER_STATUS.OPEN:
                    self.balance -= order.realized_value

                # Order has been executed
                else:
                    closed_orders.append(order)
                    self.balance += order.realized_value

                # self.on_order_change(order)     # Call event
            else:
                open_portfolio += order.current_value

        # Remove all orders that have been executed
        for order in closed_orders:
            self._current_orders.remove(order)
        self.closed_orders += closed_orders

        self.portfolio = self.balance + open_portfolio
        return self.portfolio

    # For users to reimplement
    @abstractmethod
    def on_next(self, new_row: pd.Series):
        pass

    def _step(self) -> pd.Series:
        new_row = self.main_datasrc.get_next()
        return new_row

    def start(
        self,
        start_date: Union[str, datetime, None] = None,
        end_date: Union[str, datetime, None] = None,
    ) -> float:
        if not self.main_datasrc:
            raise ValueError("No data source provided!")

        self.main_datasrc.set_date(start_date, end_date)

        # Go through each row
        # on each row call on_next
        # after on_next, _eval all orders
        for _ in tqdm(range(self.main_datasrc.length)):
            new_row = self._step()
            if new_row is None:
                break
            self.on_next(new_row)
            self._eval_orders(new_row)

        return self.portfolio

    @property
    def open_orders(self) -> List[Order]:
        return [
            order for order in self._current_orders if order.status == ORDER_STATUS.OPEN
        ]

    @property
    def submitted_orders(self) -> List[Order]:
        return [
            order for order in self._current_orders if order.status == ORDER_STATUS.OPEN
        ]

    @property
    def data(self) -> pd.DataFrame:
        return self.main_datasrc.data

    @property
    def win_rate(self) -> float:
        n_profit_order = [
            order
            for order in self.closed_orders
            if order.status == ORDER_STATUS.EXECUTED_PROFIT
        ]
        n_executed_orders = [
            order
            for order in self.closed_orders
            if order.status != ORDER_STATUS.EXPIRED
        ]
        try:
            wr = len(n_profit_order) / len(n_executed_orders)
            return wr
        except ZeroDivisionError:
            return 0

    @property
    def all_orders(self) -> List[Order]:
        return self.closed_orders + self._current_orders

    @property
    def is_finished(self) -> bool:
        return self.main_datasrc.is_finished
    
    
    @property
    def open_col(self) -> str:
        return self.main_datasrc.open_col
    
    @property
    def high_col(self) -> str:
        return self.main_datasrc.high_col
    
    @property
    def low_col(self) -> str:
        return self.main_datasrc.low_col
    
    @property
    def close_col(self) -> str:
        return self.main_datasrc.close_col
