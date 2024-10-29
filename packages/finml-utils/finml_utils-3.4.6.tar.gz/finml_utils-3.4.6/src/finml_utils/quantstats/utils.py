# original code: QuantStats: Portfolio analytics for quants
# https://github.com/ranaroussi/quantstats Copyright 2019-2023 Ran Aroussi
# Licensed originally under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0


import datetime as _dt
import inspect
import io as _io
from typing import Literal

import numpy as np
import pandas as pd

from . import stats as _stats


def _mtd(df: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    return df[df.index >= _dt.datetime.now().strftime("%Y-%m-01")]


def _qtd(df: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    date = _dt.datetime.now()
    for q in [1, 4, 7, 10]:
        if date.month <= q:
            return df[df.index >= _dt.datetime(date.year, q, 1).strftime("%Y-%m-01")]
    return df[df.index >= date.strftime("%Y-%m-01")]


def _ytd(df: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    return df[df.index >= _dt.datetime.now().strftime("%Y-01-01")]


def _pandas_date(df: pd.Series | pd.DataFrame, dates):
    if not isinstance(dates, list):
        dates = [dates]
    return df[df.index.isin(dates)]


def _pandas_current_month(df: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    n = _dt.datetime.now()
    daterange = pd.date_range(_dt.date(n.year, n.month, 1), n)
    return df[df.index.isin(daterange)]


def multi_shift(df: pd.Series | pd.DataFrame, shift: int = 3) -> pd.DataFrame:
    """Get last N rows relative to another row in pandas"""
    if isinstance(df, pd.Series):
        df = pd.DataFrame(df)

    dfs = [df.shift(i) for i in np.arange(shift)]
    for ix, dfi in enumerate(dfs[1:]):
        dfs[ix + 1].columns = [str(col) for col in dfi.columns + str(ix + 1)]
    return pd.concat(dfs, 1, sort=True)


def to_returns(
    prices: pd.Series | pd.DataFrame, rf: float = 0.0
) -> pd.Series | pd.DataFrame:
    """Calculates the simple arithmetic returns of a price series"""
    return _prepare_returns(prices, rf)


def to_prices(
    returns: pd.Series | pd.DataFrame, base: float = 1e5
) -> pd.Series | pd.DataFrame:
    """Converts returns series to price data"""
    returns = returns.copy().fillna(0).replace([np.inf, -np.inf], float("NaN"))

    return base + base * _stats.compsum(returns)


def log_returns(
    returns: pd.Series | pd.DataFrame, rf: float = 0.0, nperiods: int | None = None
) -> pd.Series | float:
    """Shorthand for to_log_returns"""
    return to_log_returns(returns, rf, nperiods)


def to_log_returns(
    returns: pd.Series | pd.DataFrame, rf: float = 0.0, nperiods: int | None = None
) -> pd.Series | float:
    """Converts returns series to log returns"""
    returns = _prepare_returns(returns, rf, nperiods)
    try:
        return np.log(returns + 1).replace([np.inf, -np.inf], float("NaN"))
    except Exception:  # noqa
        return 0.0


def exponential_stdev(
    returns: pd.Series | pd.DataFrame, window: int = 30, is_halflife: bool = False
) -> pd.Series | pd.DataFrame:
    """Returns series representing exponential volatility of returns"""
    returns = _prepare_returns(returns)
    halflife = window if is_halflife else None
    return returns.ewm(
        com=None, span=window, halflife=halflife, min_periods=window
    ).std()


def rebase(
    prices: pd.Series | pd.DataFrame, base: float = 1.0
) -> pd.Series | pd.DataFrame:
    """
    Rebase all series to a given intial base.
    This makes comparing/plotting different series together easier.
    Args:
        * prices: Expects a price series/dataframe
        * base (number): starting value for all series.
    """
    return prices.dropna() / prices.dropna().iloc[0] * base


def group_returns(
    returns: pd.Series | pd.DataFrame, groupby: str, compounded: bool = False
) -> pd.Series | pd.DataFrame:
    """Summarize returns
    group_returns(df, df.index.year)
    group_returns(df, [df.index.year, df.index.month])
    """
    if compounded:
        return returns.groupby(groupby).apply(_stats.comp)
    return returns.groupby(groupby).sum()


def aggregate_returns(
    returns: pd.Series | pd.DataFrame, period=None, compounded: bool = True
) -> pd.Series | pd.DataFrame:
    """Aggregates returns based on date periods"""
    if period is None or "day" in period:
        return returns
    index = returns.index

    if "month" in period:
        return group_returns(returns, index.month, compounded=compounded)

    if "quarter" in period:
        return group_returns(returns, index.quarter, compounded=compounded)

    if period == "A" or any(x in period for x in ["year", "eoy", "yoy"]):
        return group_returns(returns, index.year, compounded=compounded)

    if "week" in period:
        return group_returns(returns, index.week, compounded=compounded)

    if "eow" in period or period == "W":
        return group_returns(returns, [index.year, index.week], compounded=compounded)

    if "eom" in period or period == "M":
        return group_returns(returns, [index.year, index.month], compounded=compounded)

    if "eoq" in period or period == "Q":
        return group_returns(
            returns, [index.year, index.quarter], compounded=compounded
        )

    if not isinstance(period, str):
        return group_returns(returns, period, compounded)

    return returns


def to_excess_returns(
    returns: pd.Series | pd.DataFrame,
    rf: float | pd.Series | pd.DataFrame,
    nperiods: int | None = None,
) -> pd.Series | pd.DataFrame:
    """
    Calculates excess returns by subtracting
    risk-free returns from total returns

    Args:
        * returns (Series, DataFrame): Returns
        * rf (float, Series, DataFrame): Risk-Free rate(s)
        * nperiods (int): Optional. If provided, will convert rf to different
            frequency using deannualize
    Returns:
        * excess_returns (Series, DataFrame): Returns - rf
    """
    if isinstance(rf, int):
        rf = float(rf)

    if not isinstance(rf, float):
        rf = rf[rf.index.isin(returns.index)]

    if nperiods is not None:
        # deannualize
        rf = np.power(1 + rf, 1.0 / nperiods) - 1.0

    return returns - rf


def _prepare_prices(data: pd.Series | pd.DataFrame, base: float = 1.0):
    """Converts return data into prices + cleanup"""
    data = data.copy()
    if isinstance(data, pd.DataFrame):
        for col in data.columns:
            if data[col].dropna().min() <= 0 or data[col].dropna().max() < 1:
                data[col] = to_prices(data[col], base)

    # is it returns?
    # elif data.min() < 0 and data.max() < 1:
    elif data.min() < 0 or data.max() < 1:
        data = to_prices(data, base)

    if isinstance(data, pd.DataFrame | pd.Series):
        data = data.fillna(0).replace([np.inf, -np.inf], float("NaN"))

    return data


def _prepare_returns(
    data: pd.Series | pd.DataFrame, rf: float = 0.0, nperiods: int | None = None
) -> pd.Series | pd.DataFrame:
    """Converts price data into returns + cleanup"""
    data = data.copy()
    function = inspect.stack()[1][3]
    if isinstance(data, pd.DataFrame):
        for col in data.columns:
            if data[col].dropna().min() >= 0 and data[col].dropna().max() > 1:
                data[col] = data[col].pct_change()
    elif data.min() >= 0 and data.max() > 1:
        data = data.pct_change()

    # cleanup data
    data = data.replace([np.inf, -np.inf], float("NaN"))

    if isinstance(data, pd.DataFrame | pd.Series):
        data = data.fillna(0).replace([np.inf, -np.inf], float("NaN"))
    unnecessary_function_calls = [
        "_prepare_benchmark",
        "cagr",
        "gain_to_pain_ratio",
        "rolling_volatility",
    ]

    if function not in unnecessary_function_calls and rf > 0:
        return to_excess_returns(data, rf, nperiods)
    return data


def _prepare_benchmark(
    benchmark: pd.Series | pd.DataFrame,
    period="max",
    rf: float = 0.0,
    prepare_returns: bool = True,
) -> pd.Series | pd.DataFrame:
    """
    Fetch benchmark if ticker is provided, and pass through
    _prepare_returns()

    period can be options or (expected) _pd.DatetimeIndex range
    """
    if benchmark is None:
        return None

    if isinstance(period, pd.DatetimeIndex) and set(period) != set(benchmark.index):
        # Adjust Benchmark to Strategy frequency
        benchmark_prices = to_prices(benchmark, base=1)
        new_index = pd.date_range(start=period[0], end=period[-1], freq="D")
        benchmark = (
            benchmark_prices.reindex(new_index, method="bfill")
            .reindex(period)
            .pct_change()
            .fillna(0)
        )
        benchmark = benchmark[benchmark.index.isin(period)]

    benchmark.index = benchmark.index.tz_localize(None)

    if prepare_returns:
        return _prepare_returns(benchmark.dropna(), rf=rf)
    return benchmark.dropna()


def _round_to_closest(
    val: float | int, res: float, decimals: int | None = None
) -> float:
    """Round to closest resolution"""
    if decimals is None and "." in str(res):
        decimals = len(str(res).split(".")[1])
    return round(round(val / res) * res, decimals)


def _file_stream():
    """Returns a file stream"""
    return _io.BytesIO()


def _count_consecutive(data: pd.Series | pd.DataFrame):
    """Counts consecutive data (like cumsum() with reset on zeroes)"""

    def _count(data: pd.Series | pd.DataFrame):
        return data * (data.groupby((data != data.shift(1)).cumsum()).cumcount() + 1)

    if isinstance(data, pd.DataFrame):
        for col in data.columns:
            data[col] = _count(data[col])
        return data
    return _count(data)


def _score_str(val: str) -> str:
    """Returns + sign for positive values (used in plots)"""
    return ("" if "-" in val else "+") + str(val)


def make_portfolio(
    returns: pd.Series | pd.DataFrame,
    start_balance: float = 1e5,
    mode: Literal["comp", "sum", "compsum", "cumsum"] = "comp",
    round_to: int | None = None,
) -> pd.DataFrame:
    """Calculates compounded value of portfolio"""
    returns = _prepare_returns(returns)

    if mode.lower() in ["cumsum", "sum"]:
        p1 = start_balance + start_balance * returns.cumsum()
    elif mode.lower() in ["compsum", "comp"]:
        p1 = to_prices(returns, start_balance)
    else:
        # fixed amount every day
        comp_rev = (start_balance + start_balance * returns.shift(1)).fillna(
            start_balance
        ) * returns
        p1 = start_balance + comp_rev.cumsum()

    # add day before with starting balance
    p0 = pd.Series(data=start_balance, index=p1.index + pd.Timedelta(days=-1))[:1]

    portfolio = pd.concat([p0, p1])

    if isinstance(returns, pd.DataFrame):
        portfolio.iloc[:1, :] = start_balance
        portfolio = portfolio.drop(columns=[0])

    if round_to:
        return np.round(portfolio, round_to)

    return portfolio
