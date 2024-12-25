import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

df = pd.read_excel(r'C:\Users\HUYIFAN\Desktop\5月\reportdata\report_data.xlsx')
df_time = df['创建时间']
df_time_new = pd.to_datetime(df_time)
df_label = df['labelx2']
df_split = pd.DataFrame()

elements = df['labelx2'].unique()
#plt.figure(figsize=(30, 15)) 这个在外面是累加图

for element in elements:
    # 创建一个布尔列，元素名称作为列名，值为 True 或 False
    plt.figure(figsize=(30, 15))
    df_split[element] = df['labelx2'] == element
    #max_y = df_split[element].sum().max()
    plt.plot(df_time_new, df_split[element], label='%s' %(element))  # 使用不同的颜色绘制第一条折线
    plt.xlabel('时间')
    plt.ylabel('频次')
    plt.ylim(0, 1)
    plt.title('%s' %(element))
    plt.legend(loc='best')
    #plt.show()
    plt.savefig('%s.png' %(element))