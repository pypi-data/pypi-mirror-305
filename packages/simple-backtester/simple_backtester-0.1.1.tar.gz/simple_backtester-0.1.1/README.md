# Simple Backtesting in Python

![License](https://img.shields.io/pypi/l/simple-backtester)
![Python versions](https://img.shields.io/pypi/pyversions/simple-backtester)

A simple backtesting library in Python with no frills and all the customization. Just easy backtesting.

> Note that this project is in <ins>**active development**</ins>. For feature suggestions, feel free to head on over to the [Issues](https://github.com/SSBakh07/simple-backtester/issues) tab.

Compatible with Python 3.9+.

## Dependencies

- Numpy (1.26.0, <2.0.0)
- Pandas
- tqdm

## Install

You can install from [PyPI](https://pypi.org/project/simple-backtester/):

```
pip install simple-backtester
```

Or you can install directly from the repo:

```
git clone https://github.com/SSBakh07/simple-backtester
cd simple-backtester
pip install .
```

## Usage guide

Pretend we're looking to implement a simple strategy where if the closing price falls twice, we buy. If the price rises two candles in a row, we sell.

### 1. Implement your strategy

We do this by creating a class that inherits from the `SBStrat` subclass. All we need to do is implement the `on_next` method which only takes one argument: our latest data.

```python
from simple_backtester import SBStrat

class SimpleStrat(SBStrat):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bullish = False
        self.bearish = False
        self.last_price = None
    
    def on_next(self, new_row: pd.Series):
        # Fetch the latest close price
        new_close = new_row[self.close_col]
        
        # If last_price hasn't been set, let's do that first!
        if not self.last_price:
            self.last_price = new_close
            return
        
        # Compare our newest close price with our last close price
        if self.last_price >= new_close:
            if self.bullish:
                self.sell()  # Spot order
                self.bullish = False
            else:
                self.bullish = True
                self.bearish = False
        
        else:
            if self.bearish:
                self.buy()  # Spot order
                self.bearish = False
            else:
                self.bearish = True
                self.bullish = False
        
        self.last_price = new_close
```


What happens whenever `buy` or `sell` is called, an `Order` object is made. `Order`s can have one of the following statuses:
- `SUBMITTED`
- `OPEN`
- `EXECUTED_LOSS` (I.E. our position was closed at stop loss)
- `EXECUTED_PROFIT` (I.E. our position was closed at take profit)
- `EXPIRED` (I.E. order expired before it could be opened)

> Note that at the moment, only market orders have been implemented. In future versions limit orders will be added

We can set prices for our market order if we so wish:

```python
self.buy(
    buy_stop = 1000.5   # Open buy order when we hit 1000.5
)
```

or for sell orders:

```python
self.sell(
    sell_stop = 1000.5   # Open sell order when we hit 1000.5
)
```


We can also set stop losses and take profits as needed:

```python
# Set stop loss at 900, and take profit at 1100
self.buy(
    buy_stop = 1000.5,
    take_profit = 1100,
    stop_loss = 900
)
```

Or even set an expiration datetime for our buy and sell orders:

```python
# Set stop loss at 900, and take profit at 1100
self.sell(
    sell_stop = 900,
    take_profit = 800,
    stop_loss = 1150,
    expiry_time = "2024-01-01"  # Can be str or pd.Timestamp
)
```



If we want to do something every time an order's status changes (such as logging), we can implement the `on_order_change` abstract method:

```python
import logging
from simple_backtester import SBStrat, Order, ORDER_STATUS


class SimpleStrat(SBStrat):
    def __init__(self, **kwargs):
        ...
    
    def on_next(self, new_row: pd.Series):
        ...

    def on_order_change(self, order: Order):
        if order.status == ORDER_STATUS.OPEN:
            logging.info(f"Order opened! {order.order_type}")
        if order.status == sbs.ORDER_STATUS.EXECUTED_LOSS or order.status == sbs.ORDER_STATUS.EXECUTED_PROFIT:
            logging.info(f"Order closed! Current portfolio value: {self.portfolio}")
        if order.status == sbs.ORDER_STATUS.EXPIRED:
            logging.info("Order expired!")
```



And then, all we need to do is to create an instance of our strategy class:

```python
test_strat = SimpleStrat(balance = 15000)    # Start with 15000 units. Defaults to 1000
```


### 2. Add your data

For now, the only way we can add our candle data data is by passing in a [`pandas DataFrame`](https://pandas.pydata.org/docs/reference/frame.html). I'll be adding alternative data sources in the near future.

> Tick data is not supported at this time.

```python
import pandas as pd

ohlc_data = pd.read_csv("example_candle_data.csv")
test_strat.add_data(ohlc_data)
```


If our columns have different names or our date column has a specific format, we can pass those in:

```python
test_strat.add_data(
        ohlc_data,
        open_col = "OPEN",  # Defaults to "open"
        high_col = "HIGH",  # Defaults to "high"
        low_col = "LOW",    # Defaults to "low"
        close_col = "CLOSE",    # Defaults to "close"
        date_col = "DATETIME",  # Defaults to "date"
        date_fmt = "%d-%m-%Y %H:%M:%S"  # Infers by default
    )
```


### 3. Profit!

And now, all that's left is running our test!

```python
test_strat.start()
```

We can specify our tests to be run from or to a certain date:

```python
test_strat.start(
    start_date = "01-01-2023",
    end_date = "01-01-2024"
)
```

And we can fetch our win-rate like so:

```python
test_strat.win_rate
```

And if we want to start over and rerun our tests, all we need to do is call the `reset()` function:

```python
test_strat.reset()
```

It's *that* simple! :)


## To-do List:

+ [ ] Limit orders
+ [ ] Add risk/reward ratio
+ [ ] Adding support for Python3.8 and Python3.7
+ [ ] Writing up *proper* documentation
+ [ ] Adding more tests/cleaning up tests
+ [ ] Adding indicators using `talib`
+ [ ] Adding commission fees
+ [ ] Adding Yfinance support
+ [ ] Adding support for tick data


> Questions? Concerns? Email me at ssbakh07 (at) gmail.com
