import yfinance as yf
import os
from scripts.utils import ensure_dir

def fetch_stock_data(ticker, start, end, save_path):
    """Fetch stock data from Yahoo Finance and save raw CSV."""
    df = yf.download(ticker, start=start, end=end)

    # Ensure directory exists
    ensure_dir(os.path.dirname(save_path))

    # Save file
    df.to_csv(save_path, index=True)  # keep Date index
    return df
