'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-05-27 22:08:12
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-05-28 22:50:17
FilePath: \vnpy_fork\examples\runoob\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "002714.SZ"
start_date = "2023-05-01"
end_date = "2024-05-01"

data = yf.download(symbol, start=start_date, end=end_date)
# data.to_csv("mygf_20230501_20240501.csv")
# 简单的数据分析
print(data.describe())

# 绘制股价走势图
data['Close'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()