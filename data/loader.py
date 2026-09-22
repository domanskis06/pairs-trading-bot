"""Fetch and cache historical close prices for a list of tickers."""

import os

import pandas as pd
import yfinance as yf

from config import DATA_CACHE_DIR


def get_prices(tickers, start, end, cache=True):
    """Return a DataFrame of daily close prices, columns=tickers, index=date.

    Each ticker is cached to its own CSV under data_cache/ keyed by
    ticker+date range, so repeated calls don't re-hit the network.
    """
    os.makedirs(DATA_CACHE_DIR, exist_ok=True)
    columns = {}
    for ticker in tickers:
        cache_path = os.path.join(DATA_CACHE_DIR, f"{ticker}_{start}_{end}.csv")
        if cache and os.path.exists(cache_path):
            close = pd.read_csv(cache_path, index_col=0, parse_dates=True)["Close"]
        else:
            raw = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
            if raw.empty:
                raise ValueError(f"No data returned for {ticker}")
            close = raw["Close"][ticker]
            close.to_frame(name="Close").to_csv(cache_path)
        columns[ticker] = close
    return pd.DataFrame(columns).dropna()
