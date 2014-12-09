# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:53:04 2014

@author: gob
"""

import matplotlib.pyplot as plt

from skimage import data
from skimage.filter.rank import entropy
from skimage.morphology import disk
from skimage.util import img_as_ubyte


image = img_as_ubyte(data.camera())

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 4))
fig.suptitle('George O. Barros - Entropy (scikit-image)')

img0 = ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Image')
ax0.axis('off')
fig.colorbar(img0, ax=ax0)

img1 = ax1.imshow(entropy(image, disk(5)), cmap=plt.cm.jet)
ax1.set_title('Entropy')
ax1.axis('off')
fig.colorbar(img1, ax=ax1)

plt.show()