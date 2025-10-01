import pandas as pd
import matplotlib.pyplot as plt
import os

# === Choose ticker ===
ticker = "AAPL"   # Change to MSFT, TSLA, etc.
data_path = os.path.join("data", "raw", f"{ticker}.csv")

# === Load stock data ===
df = pd.read_csv(data_path, parse_dates=["Date"])

print("Data Preview:")
print(df.head())

# === Plot Closing Price ===
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"], label="Close Price", color="blue")
plt.title(f"{ticker} Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# === Moving Averages (SMA 20 & 50) ===
df["SMA20"] = df["Close"].rolling(window=20).mean()
df["SMA50"] = df["Close"].rolling(window=50).mean()

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"], label="Close Price", alpha=0.7)
plt.plot(df["Date"], df["SMA20"], label="SMA 20", color="orange")
plt.plot(df["Date"], df["SMA50"], label="SMA 50", color="red")
plt.title(f"{ticker} Stock with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# === Volume Analysis ===
plt.figure(figsize=(12,4))
plt.bar(df["Date"], df["Volume"], color="gray")
plt.title(f"{ticker} Stock Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
