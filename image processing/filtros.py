import numpy as np
import matplotlib.pyplot as plt

from skimage import img_as_ubyte
from skimage import data
from skimage.morphology import disk
from skimage.filter.rank import autolevel
from skimage import exposure
from skimage.filter import rank

noisy_image = img_as_ubyte(data.camera())

# equalize globally and locally
glob = exposure.equalize_hist(noisy_image) * 255
loc = rank.equalize(noisy_image, disk(20))

# extract histogram for each image
hist = np.histogram(noisy_image, bins=np.arange(0, 256))
glob_hist = np.histogram(glob, bins=np.arange(0, 256))
loc_hist = np.histogram(loc, bins=np.arange(0, 256))

fig, ax = plt.subplots(4, 2, figsize=(10, 10))
fig.suptitle('George O. Barros - Alguns Filtros (scikit-image)')
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = ax.ravel()

ax1.imshow(noisy_image, interpolation='nearest', cmap=plt.cm.gray)
ax1.set_title('imagens')
ax1.axis('off')

ax2.plot(hist[1][:-1], hist[0], lw=2)
ax2.set_title('Histogram')

ax3.imshow(glob, interpolation='nearest', cmap=plt.cm.gray)
ax3.axis('off')

ax4.plot(glob_hist[1][:-1], glob_hist[0], lw=2)

ax5.imshow(loc, interpolation='nearest', cmap=plt.cm.gray)
ax5.axis('off')

ax6.plot(loc_hist[1][:-1], loc_hist[0], lw=2)

auto = autolevel(noisy_image.astype(np.uint16), disk(20))
ax7.imshow(auto, cmap=plt.cm.gray)
ax7.axis('off')

histAutoLevel= np.histogram(auto, bins=np.arange(0, 256))
ax8.plot(histAutoLevel[1][:-1], histAutoLevel[0], lw=2)
plt.show()