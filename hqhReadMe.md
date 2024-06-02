<!--
 * @Author: Huang, Quan Hang 250901214@qq.com
 * @Date: 2024-05-28 22:38:07
 * @LastEditors: Huang, Quan Hang 250901214@qq.com
 * @LastEditTime: 2024-06-03 00:23:18
 * @FilePath: \vnpy_fork\hqhReadMe.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
[SimNow](https://www.simnow.com.cn/)
- 账号：18650054701
- 密码：@Hqh83515433
- 手机：18650054701
- 昵称：Honey
- investorId：226463
- brokerId：9999
- 挂靠会员：SimNow
- [经纪商代码以及交易行情服务器地址](https://www.simnow.com.cn/product.action)

[VeighNa量化社区](https://www.vnpy.com/forum/) VeighNa Station账号密码
- 邮箱：250901214@qq.com
- 手机：18650054701
- 密码：@Hqh83515433

[Tushare](https://tushare.pro/)
- 账号：18650054701
- 密码：@Hqh83515433
- ID: 666038
- Token: 4dc982e7ed47ca420c5963a4b188d53f748862e0002a819cc42f37e8

# 安装问题
- python3.10.11
```
wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz

tar -zxvf Python-3.10.11.tgz
cd Python-3.10.11
./configure
make && make install DESTDIR=/home/hqh/Market/Python3.10.11

nano ~/.bashrc
alias python='/home/hqh/Market/Python3.10.11/usr/local/bin/python3'
alias python3='/home/hqh/Market/Python3.10.11/usr/local/bin/python3'
alias pip='/home/hqh/Market/Python3.10.11/usr/local/bin/pip3'
alias pip3='/home/hqh/Market/Python3.10.11/usr/local/bin/pip3'

python -m pip install --upgrade pip
```
- venv
```
python -m venv myEnv
source myEnv/bin/activate
```
- vnpy_ctp
  ```
  mkdir gitRepository
  cd gitRepository
  git clone https://github.com/vnpy/vnpy_ctp.git
  cd vnpy_ctp
  pip install .
  ```
- vnpy_rpcservice
  ```
  pip install vnpy_rpcservice
  ```
- vnpy_ctastrategy
  ```
  pip install vnpy_ctastrategy
  ```
- vnpy_ctabacktester
  ```
  pip install vnpy_ctabacktester
  ```
- vnpy_sqlite
  ```
  pip install vnpy_sqlite
  git clone https://github.com/vnpy/vnpy_sqlite.git
  cd vnpy_sqlite
  pip install .
  ```

Pip 安装失败
- pip install pandas --default-timeout=6000
- pip install xxx.whl  # wheel
- pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
- pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
- pip install akshare --upgrade
- pip install akshare -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade

# 学习
[JoinQuant Huogo2046](https://www.joinquant.com/user/9df4817f9c39c67ea27e97be2b182d1c)

# [Python 量化交易](https://www.runoob.com/python-qt/qt-tutorial.html)

# [NumPy 教程](https://www.runoob.com/numpy/numpy-tutorial.html)
- NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。
- 在 NumPy中，每一个线性的数组称为是一个轴（axis）

# [Pandas 教程](https://www.runoob.com/pandas/pandas-tutorial.html)
- [Pandas 官方教程]https://pandas.pydata.org/pandas-docs/dev/user_guide/10min.html

# [Matplotlib 教程](https://www.runoob.com/matplotlib/matplotlib-tutorial.html)

# [Python 量化交易](https://wizardforcel.gitbooks.io/python-quant-uqer/content/)

# 网格交易
- [ETF网格交易法是什么？应该怎么做？- 雪球](https://xueqiu.com/9896818145/217941398)
- [网格交易策略（附策略源码与收益图）- CSDN](https://blog.csdn.net/weixin_57522153/article/details/116814490)

## 设定网格大小
- 主要注意标的振幅至少2倍于网格大小，最好是能几倍于网格大小，这样可以提高网格成交的概率。相对网格越小，成交的概率肯定越高，但是对资金量要求就越高（初始情况下，不知道该设置多大，保险起见可以大后小的原则试试水再适应性调整）
- 震荡行情可适当收小，尽量多的抓住每一个小的波动；趋势行情可适当放大，防止过早满仓或者空仓

## 计算建仓份数
- 选好标的、设定完价格区间和网格大小后，我们就开始建立一个用于网格交易的底仓，建仓仓位大小需根据标的当前的价位相对设定价格区间的相对位置而定，如果当前价格相对较低，则底仓可以稍微提高；价格相对较高，则可以先轻仓。
- 具体建仓份数=(上限价格-当前价格)/网格大小

## 设定每格份额
- 每格份额需要根据投入资金、网格价格上下限及网格大小来推算。
- 如果是固定股数网格，则 每格买入份额=投入资金/(建仓份数+((当前价格-1格+下限价格)/2))*(当前价格-下限价格)/网格大小))；
- 如果是固定资金网格，则直接是 投入资金/格子数量 就行了、

## 长期看长时的网格策略
- 上涨和下跌的格子宽度相同时，
  - 可以设置较高的上限和较低的下限，以引导在当前价下买入更多的份数
- 上涨和下跌的格子宽度不同时，
  - 可设置教宽的上涨格子和较窄的下跌格子，在趋势上涨的过程中不断累积持仓，一次真的下跌将吃光盈利
  - 可设置教窄的上涨格子和较宽的下跌格子，一个中反弹子弹将全打光，盈利空间太小
- 上涨格子宽度不同
- 下跌格子宽度不同

## 上限下限，止盈止损
- 止盈：如果价格达到这个值，网格将自动卖出所有头寸
- 止损：如果价格跌破该价格水平，网格将自动卖出所有头寸
- 上限：上限是网格的最高价格限制。机器人不会下达超过此限制的卖单。
- 下限：下限是网格的最低价格限制。机器人不会下达低于此限制的买入订单。


# backtrader
- [01-backtrader学习笔记](https://afox.cc/2022/02/18/backtrader-study-note-tour/)
- [what-is-grid-trading](https://phemex.com/academy/what-is-grid-trading)
- [Implementing Grid Indicator using Backtrader](https://medium.com/@jesso1908joy/implementing-grid-indicator-using-backtrader-48a8ef2ba6df)
- [search in phemex](https://phemex.com/academy/search?pageNo=1&s=grid%20trading)
- [backtrader 中文](https://www.wuzao.com/document/backtrader/introduction.html)
- [重要 资料汇总Backtrader: Getting Started Backtesting](https://analyzingalpha.com/backtrader-backtesting-trading-strategies)
  - [backtrader community](https://community.backtrader.com/)
  - [Analyzing Alpha Github.](https://github.com/leosmigel/analyzingalpha/tree/master/2019-09-26-backtrader-backtesting-trading-strategies)
  - [How to write your first, simple backtrader strategy](https://quantnomad.com/faq-how-to-write-your-first-simple-backtrader-strategy/)
  - [Backtrader for Backtesting (Python) – A Complete Guide](https://algotrading101.com/learn/backtrader-for-backtesting/)
- [Backtrader-for-backtesting](https://github.com/PythonForForex/Backtrader-for-backtesting)
- [algorithmic trading library](https://gitlab.com/algorithmic-trading-library)


# vectorbtpro 

# 框架选择
- PyAlgoTrade：https://github.com/gbeced/pyalgotrade
- bt - Backtesting：http://pmorissette.github.io/bt/
- Backtrader：https://github.com/mementum/backtrader
- pysystemtrade：https://github.com/robcarver17/pysystemtrade
- Zipline：https://github.com/quantopian/zipline
- QSTrader：https://github.com/mhallsmoore/qstrader
- backtesting：https://kernc.github.io/backtesting.py/











# jointQuants
| 交易市场 | 代码后缀 | 示例代码 | 证券简称 |
|  -----  |  -----  |  -----  | -----  |
|上海证券交易所|	.XSHG|	600519.XSHG|	贵州茅台|
|深圳证券交易所|	.XSHE|	000001.XSHE|	平安银行|
|北京证券交易所|	.BJSE|	430017.BJSE|	星昊医药|
|中金所|	.CCFX|	IC9999.CCFX|	中证500主力合约|
|大商所|	.XDCE|	A9999.XDCE|	豆一主力合约|
|上期所|	.XSGE|	AU9999.XSGE|	黄金主力合约|
|郑商所|	.XZCE|	CY8888.XZCE|	棉纱期货指数|
|上海国际能源期货交易所|	.XINE|	SC9999.XINE|	原油主力合约|
|场外基金|	.OF|	398051.OF|	中海环保新能源混合|
|上证指数|	.CSI|	932000.CSI|	中证2000指数|

## 查询数据库数据
```
from jqdatasdk import query,finance

finance.run_query(query_object) #查询股票/期货/基金数据库
opt.run_query(query_object) #查询期权数据库
bond.run_query(query_object) #查询债券数据库
macro.run_query(query_object) #查询宏观数据库
```