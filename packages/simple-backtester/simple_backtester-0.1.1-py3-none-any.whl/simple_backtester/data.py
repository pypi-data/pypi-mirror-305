import pandas as pd
from datetime import datetime
from typing import Optional, List, Union
from .types import *
import warnings


class SBDataSrc:
    data: pd.DataFrame
    _all_data: pd.DataFrame  # Unfiltered dataframe

    open_col: str
    high_col: str
    low_col: str
    close_col: str
    date_col: str

    current_idx: int = -1

    start_date: Union[datetime, str, None]
    end_date: Union[datetime, str, None]

    def __init__(
        self,
        data: pd.DataFrame,
        open_col: Union[str, int] = "open",
        high_col: Union[str, int] = "high",
        low_col: Union[str, int] = "low",
        close_col: Union[str, int] = "close",
        date_col: Union[str, int] = "date",
        date_fmt: Union[str, None] = None,
        start_date: Union[datetime, str, None] = None,
        end_date: Union[datetime, str, None] = None,
    ):
        data_columns = data.columns

        self.open_col = self._set_col_name(open_col, data_columns)
        self.high_col = self._set_col_name(high_col, data_columns)
        self.low_col = self._set_col_name(low_col, data_columns)
        self.close_col = self._set_col_name(close_col, data_columns)
        self.date_col = self._set_col_name(date_col, data_columns)

        self.start_date = start_date
        self.end_date = end_date

        if len(data) == 0:
            warnings.warn("Provided data has a length of 0.")

        # Set date(time) index
        if data.index.inferred_type != "datetime64":
            try:
                data[self.date_col] = pd.to_datetime(
                    data[self.date_col], format=date_fmt
                )
            except ValueError:
                raise ValueError(
                    "Invalid data format for data source. Specify date format using date_fmt parameter."
                )
            data.set_index(self.date_col, inplace=True)

        self._all_data = data.copy()
        self.data = data[start_date:end_date]

    def set_date(
        self,
        start_date: Union[str, datetime, None] = None,
        end_date: Union[str, datetime, None] = None,
    ):
        self.data = self._all_data[start_date:end_date].copy()

    @staticmethod
    def _set_col_name(col_name_val: Union[int, str], data_columns: List[str]) -> str:
        if type(col_name_val) == int:
            return data_columns[col_name_val]

        if col_name_val not in data_columns:
            warnings.warn("Column {} not found in provided data".format(col_name_val))
        return col_name_val

    def get_next(self) -> pd.Series:
        self.current_idx += 1
        if self.current_idx >= self.length:
            return None
        cur_row = self.data.iloc[self.current_idx]
        return cur_row

    def reset(self):
        self.current_idx = -1

    @property
    def length(self) -> int:
        return len(self.data)

    @property
    def is_finished(self) -> bool:
        return self.current_idx >= self.length - 1

    @property
    def current_row(self) -> pd.Series:
        return self.data.iloc[self.current_idx]
