'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-06-01 16:47:40
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-06-02 16:28:40
FilePath: \vnpy_fork\examples\hqh\JoinQuant\test2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 导入技术分析指标库
from jqdatasdk import *
from jqdatasdk.technical_analysis import *
import seaborn as sns
import matplotlib as plt

auth('18650054701', 'Hqh83515433')

df = get_price(get_industry_stocks('A01', date='2024-02-28'), fields=('close',), frequency='1d', start_date='2024-02-01', end_date='2024-02-28')['close']

plt.figure(figsize=[18,5])
df['000998.XSHE'].plot()
pd.rolling_mean(df['000998.XSHE'],20).plot(label='20 day moving average')
pd.rolling_mean(df['000998.XSHE'],5).plot(label='5 day moving average')
plt.legend(loc='best')