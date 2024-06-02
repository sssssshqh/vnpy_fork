'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-06-01 17:20:46
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-06-01 17:20:49
FilePath: \vnpy_fork\examples\hqh\bt\test2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt

class MyStrategy(bt.Strategy):
    params = (
        ('m', 20),
    )

    def log(self, txt, dt=None):
        df = self.datas[0].datetime.date(0)
        print('%s, %s' % (df.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close

        self.sma = bt.indicators.SMA(self.datas[0], period=self.params.m)

        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)
            print('=======order',self.bar_executed)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None


    def next(self):
        if self.order:
            self.log("==is order: %s" % self.order)
            return

        # 检查是否持仓
        if not self.position:
            # 上涨突破20日均线执行买入
            if self.dataclose[0] > self.sma[0]:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()
        else:
            # 下跌突破20日均线执行卖出
            if self.dataclose[0] < self.sma[0]:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(MyStrategy)
     # 读取数据
    df = pd.read_feather('./BTCUSDT_1d.feather')

    df.candle_begin_time = pd.to_datetime(df.candle_begin_time)

    df.set_index('candle_begin_time', inplace=True)

    # 给cerebro添加数据
    data = bt.feeds.PandasData(dataname=df)

    cerebro.adddata(data)

    # 设置初始化资金
    cerebro.broker.setcash(10000.0)    
    cerebro.broker.setcommission(commission=0.002)  # 手续费
    cerebro.run()

    cerebro.plot()