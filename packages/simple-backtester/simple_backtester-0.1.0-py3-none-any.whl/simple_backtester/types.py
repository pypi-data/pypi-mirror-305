from enum import Enum


class PRICE_TYPE(Enum):
    OPEN = 0
    CLOSE = 1
    MIDDLE = 2


class ORDER_STATUS(Enum):
    SUBMITTED = 0
    OPEN = 1
    EXECUTED_LOSS = 2
    EXECUTED_PROFIT = 3
    EXPIRED = 4


class ORDER_TYPE(Enum):
    BUY = 0
    SELL = 1
    BUY_LIMIT = 2
    SELL_LIMIT = 3
