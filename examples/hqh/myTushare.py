import tushare as ts
pro = ts.pro_api('4dc982e7ed47ca420c5963a4b188d53f748862e0002a819cc42f37e8')

# df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
# df = pro.daily(trade_date='20180810')
df = pro.daily(ts_code='002714.SZ', trade_date='20240520')
print (df)