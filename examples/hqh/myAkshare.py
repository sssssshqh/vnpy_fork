import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

symbol="002714"
start_date = "20230515"
end_date = "20240520"
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start_date, end_date=end_date, adjust="")
# 简单的数据分析
# print(stock_zh_a_hist_df)
print(stock_zh_a_hist_df.describe())

# 绘制股价走势图
stock_zh_a_hist_df['收盘'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")
plt.switch_backend('agg')
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
plt.savefig("./output/pyplot/1.jpg")