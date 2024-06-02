'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-05-31 22:33:53
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-06-01 16:47:46
FilePath: \vnpy_fork\examples\hqh\JoinQuant\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: Huang, Quan Hang 250901214@qq.com
Date: 2024-05-31 22:33:53
LastEditors: Huang, Quan Hang 250901214@qq.com
LastEditTime: 2024-05-31 22:47:05
FilePath: \vnpy_fork\examples\hqh\JoinQuant\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import jqdatasdk

jqdatasdk.auth('18650054701', 'Hqh83515433')

# jqdatasdk.get_price(security='000001.XSHE', frequency='1m')

count=jqdatasdk.get_query_count()
print(count)

infos = jqdatasdk.get_account_info()
print(infos)