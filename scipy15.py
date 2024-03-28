import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

# 使用scipy加载.mat文件
mat_contents = sio.loadmat('E:/Python/MatlabDataAnalysis/y_data.mat')

# 提取xx数据
xx = mat_contents['xx']

# 计算傅里叶变换
fft_xx = np.fft.fft(xx)

# 对结果取绝对值
abs_fft_xx = np.abs(fft_xx)

# 计算频率
freq = np.fft.fftfreq(len(xx), d=6/10000) + 89.2

# 绘制图形
plt.figure(1)

# 绘制第一个图形
plt.subplot(1, 2, 1)
plt.plot(np.abs(np.fft.fft(np.real(xx))))
plt.semilogy(abs_fft_xx)
plt.semilogy(np.abs(np.fft.fftshift(fft_xx)))
plt.semilogy(freq, np.abs(np.fft.fftshift(fft_xx)))
plt.semilogy(abs_fft_xx)
plt.semilogy(freq, np.abs(np.fft.fftshift(fft_xx)))

# 绘制第二个图形
plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(np.fft.fftshift(fft_xx)))

plt.show()
