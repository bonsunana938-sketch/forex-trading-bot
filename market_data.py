import yfinance as yf

pair = "EURUSD=X"

data = yf.download(
    pair,
    period="5d",
    interval="1h",
    auto_adjust=False
)

print(data.tail())