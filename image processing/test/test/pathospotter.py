from skimage import io
from skimage.feature import blob_log, blob_dog, blob_doh
from PIL import Image, ImageOps
from matplotlib import pyplot
from math import sqrt

# Parameters of configuration
image_file = "C:/Users/gob/Documents/GitHub/Python/image processing/x.jpg"#"subMatLesao.jpg"

# Load image file
image = Image.open(image_file)
original_image = image

# Prepare the image file
#image = image.convert('L')
#image.save("grayscale.jpg")

image = ImageOps.invert(image)
image.save("grayscale_inverted.jpg")

image = io.imread("grayscale_inverted.jpg", as_grey=False)

def run(min_s, max_s, sigma):
	# Run Blob Detection by Laplacian of Gaussian (LoG)
	blobs_log = blob_log(image, max_s, threshold=.01)

	# Compute radii in the 3rd column
	blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

	# Configure the graph
	fig, ax = pyplot.subplots(1, 1)
	ax.set_title("Laplacian of Gaussian, min_s=" + str(min_s) + ", max_s="
			 + str(max_s) + ", sigma=" + str(sigma))
	ax.imshow(image, vmin=0, vmax=255, cmap=pyplot.cm.gray)

	# Load graph
	for blob in blobs_log:
		y, x, r = blob
		c = pyplot.Circle((x, y), r, color='yellow', linewidth=2, fill=False)
		ax.add_patch(c)

# run(min_sigma, max_sigma, num_sigma)
#run(1, 30, 10)
#run(1, 10, 5)
#run(1, 10, 10)
run(1, 10, 30)

pyplot.show()
