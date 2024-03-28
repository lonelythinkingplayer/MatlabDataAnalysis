import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = h5py.File("E:\Python\MatlabDataAnalysis\y.mat", 'r')
print(data)
yfm_data = data["yfm"][:]
columns = ["Column1", "Column2", "Column3", "Column4", "Column5", "Column6"]
df_yfm = pd.DataFrame(yfm_data, columns=columns)
print("基本统计信息:")
print(df_yfm.describe())


'''
# 绘制直方图
df_yfm.hist(figsize=(10, 8), bins=20)
plt.show()

# 绘制折线图
df_yfm.plot(figsize=(10, 8))
plt.legend(loc='upper right')
plt.show()
'''