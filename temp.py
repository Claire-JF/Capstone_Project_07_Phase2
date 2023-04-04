import csv
import datetime

import pandas as pd

# 读取CSV文件

i = 3
Date_i = datetime.datetime.today() - datetime.timedelta(days=i)
df = pd.read_csv(Date_i.strftime("%a %b %d") + '.csv')

df['Temperature'] = df['Temperature'].str.rstrip('℃').astype(float)

# 找到温度列中的最大和最小值
max_temperature = df['Temperature'].max()
min_temperature = df['Temperature'].min()

# 打印结果
print('最高温度：', max_temperature)
print('最低温度：', min_temperature)
