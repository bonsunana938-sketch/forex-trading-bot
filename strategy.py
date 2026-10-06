import yfinance as yf

# EUR/USD hourly data
data = yf.download(
    "EURUSD=X",
    period="30d",
    interval="1h",
    auto_adjust=False
)

# Use closing prices
close = data["Close"].squeeze()

# Moving averages
data["MA20"] = close.rolling(20).mean()
data["MA50"] = close.rolling(50).mean()

# Get the latest values
ma20 = data["MA20"].iloc[-1]
ma50 = data["MA50"].iloc[-1]

print("EUR/USD Strategy")
print("----------------")
print(f"MA20: {ma20:.5f}")
print(f"MA50: {ma50:.5f}")

if ma20 > ma50:
    signal = "BUY"
elif ma20 < ma50:
    signal = "SELL"
else:
    signal = "HOLD"

print("Signal:", signal)