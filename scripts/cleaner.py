import pandas as pd
import os
from scripts.utils import ensure_dir

def clean_stock_data(input_path, output_path):
    """Clean stock data (remove duplicates, handle NaNs) and save."""
    df = pd.read_csv(input_path, parse_dates=["Date"])

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values (forward fill, then drop any remaining nulls)
    df = df.fillna(method="ffill").dropna()

    # Ensure output directory exists
    ensure_dir(os.path.dirname(output_path))

    # Save cleaned data
    df.to_csv(output_path, index=False)
    return df
