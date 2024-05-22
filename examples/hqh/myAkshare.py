import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="002714", period="daily", start_date="20230515", end_date='20240520', adjust="")
print(stock_zh_a_hist_df)