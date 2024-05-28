'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-05-27 22:26:47
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-05-27 22:28:15
FilePath: \vnpy_fork\examples\runoob\test2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#也可以用from pandas_datareader import data as web
from pandas_datareader import data as web

import datetime

import fix_yahoo_finance as yf

#这一行代码非常重要
yf.pdr_override()

start_date = datetime.datetime(2020,1,10)

end_date =datetime.datetime(2020,3,18)

data = web.get_data_yahoo('601318',start_date,end_date)

