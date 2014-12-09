# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:24:08 2014

@author: gob
"""

import matplotlib.pyplot as plt

from skimage.data import camera
from skimage.filter import roberts, sobel


image = camera()
edge_roberts = roberts(image)
edge_sobel = sobel(image)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3)
fig.suptitle('George O. Barros - Edge Detection (scikit-image)')

ax0.imshow(edge_roberts, cmap=plt.cm.gray)
ax0.set_title('Roberts Edge Detection')
ax0.axis('off')

ax1.imshow(edge_sobel, cmap=plt.cm.gray)
ax1.set_title('Sobel Edge Detection')
ax1.axis('off')

ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_title('Normal')
ax2.axis('off')

plt.show()