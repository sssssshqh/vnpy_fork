import yfinance as yf

# 上海证券交易所，茅台公司股票代码
symbol = "600519.SS"

# 或者，深圳证券交易所，泸州老窖公司股票代码
# luzhou_laojiao_szse = yf.Ticker('000568.SZ')

# 获取茅台公司股票数据
maotai_data = yf.download(symbol, start="2022-01-01", end="2023-11-01")

# 打印数据的前几行
print(maotai_data.head())