<!--
 * @Author: Huang, Quan Hang 250901214@qq.com
 * @Date: 2024-05-28 22:38:07
 * @LastEditors: Huang, Quan Hang 250901214@qq.com
 * @LastEditTime: 2024-05-28 23:30:01
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