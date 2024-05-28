import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
print(df)

# 计算 Pearson 相关系数
correlation_matrix = df.corr()
print(correlation_matrix)