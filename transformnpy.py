# import tensorflow as tf
import numpy as np
import glob  # 查找符合特定规则的文件路径名
from PIL import Image
import os

Datapath = r'D:\pycharm\11111\*.jpg'
input_raw_data = np.zeros((1400, 128, 128, 3), dtype='float32') #(1400, 1, 64, 64)
i = 0
for imageFile in glob.glob(Datapath):
    # 打开图像并转化为数字矩阵(240x240x3)
    print(os.path.join(Datapath, imageFile))
    img = np.array(Image.open(imageFile))
    input_raw_data[i] = img
    i += 1

np.save('transformnpy.npy', input_raw_data)
