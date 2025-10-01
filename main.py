import yaml
import os
from scripts.scraper import fetch_stock_data
from scripts.cleaner import clean_stock_data
from scripts.utils import setup_logger

# Load config
with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

logger = setup_logger()

tickers = config["tickers"]
start = config["date_range"]["start"]
end = config["date_range"]["end"]

for ticker in tickers:
    try:
        logger.info(f"Fetching {ticker} data...")
        raw_path = os.path.join(config["paths"]["raw"], f"{ticker}.csv")
        cleaned_path = os.path.join(config["paths"]["cleaned"], f"{ticker}_cleaned.csv")
        
        # Step 1: Fetch
        df_raw = fetch_stock_data(ticker, start, end, raw_path)
        
        # Step 2: Clean
        df_cleaned = clean_stock_data(raw_path, cleaned_path)
        
        logger.info(f"{ticker} data processed successfully.")
    except Exception as e:
        logger.error(f"Error processing {ticker}: {e}")
