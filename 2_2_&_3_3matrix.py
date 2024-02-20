# -*- coding: utf-8 -*-
"""2*2 & 3*3matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rhaXYjBby_S0CFBm5DsioMQx4T8s_sPS
"""

# First import the required python libraries
import numpy as np
from skimage.io import imshow
import matplotlib.pyplot as plt
from skimage import img_as_uint
from skimage.io import imread
from skimage.color import rgb2hsv, rgb2gray

array_1 = np.array([[255,0],[0,255]])
imshow(array_1, cmap='gray')
plt.show()

array_2 = np.array([[255,0,255],[0,255,0],[255,0,255],])
imshow(array_2, cmap='gray')
plt.show()