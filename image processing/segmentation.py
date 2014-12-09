# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:07:59 2014

@author: gob
"""


from scipy import ndimage
import matplotlib.pyplot as plt

from skimage.morphology import watershed, disk
from skimage import data
from skimage.filter import rank
from skimage.util import img_as_ubyte


image = img_as_ubyte(data.camera())

# denoise image
denoised = rank.median(image, disk(2))

# find continuous region (low gradient) --> markers
markers = rank.gradient(denoised, disk(5)) < 10
markers = ndimage.label(markers)[0]

#local gradient
gradient = rank.gradient(denoised, disk(2))

# process the watershed
labels = watershed(gradient, markers)

# display results
fig, axes = plt.subplots(ncols=4, figsize=(8, 2.7))
fig,suptitle('George - Sementation (scikit-image)')
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax3.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest', alpha=.7)

for ax in axes:
    ax.axis('off')

fig.subplots_adjust(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)


plt.show()