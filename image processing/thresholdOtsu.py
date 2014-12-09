# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 21:39:01 2014

@author: gob

Threshod Otsu
Sckit-Image example

"""

import matplotlib.pyplot as plt
from PIL import Image
#from skimage import data
from skimage.filter import threshold_otsu, threshold_adaptive
import numpy as np

image = Image.open('img/z.jpg') #data.page()
image = np.array(image.convert('L'))
 

global_thresh = threshold_otsu(image)
binary_global = image > global_thresh

block_size = 40
binary_adaptive = threshold_adaptive(image, block_size, offset=10)

fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
ax0, ax1, ax2 = axes
plt.gray()

ax0.imshow(image)
ax0.set_title('Image')

ax1.imshow(binary_global)
ax1.set_title('Global thresholding')

ax2.imshow(binary_adaptive)
ax2.set_title('Adaptive thresholding')

for ax in axes:
    ax.axis('off')

plt.show()