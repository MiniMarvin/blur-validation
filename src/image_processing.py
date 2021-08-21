import frequency
import numpy as np
import matplotlib.pyplot as plt
import cv2

def show_comparative_images(image, magnitude):
	(fig, ax) = plt.subplots(1, 2, )
	ax[0].imshow(image, cmap="gray")
	ax[0].set_title("Input")
	ax[0].set_xticks([])
	ax[0].set_yticks([])

	ax[1].imshow(magnitude, cmap="gray")
	ax[1].set_title("Magnitude Spectrum")
	ax[1].set_xticks([])
	ax[1].set_yticks([])
	plt.show()

def detect_blur_fft(image, frequency_threshold=50, thresh=15):
	"""
	computes if the image is blurry (i.e. a low definition image), by processing the image with a high pass filter on frequency spectrum
	"""
	fft_image = frequency.go_to_frequency_domain(image)
	magnitude = frequency.compute_magnitude(fft_image)

	filtered_spectrum = frequency.smooth_high_pass_filter(
		fft_image, frequency_threshold, 
		frequency_threshold//2)
    
	recon_image = frequency.return_to_spatial_domain(filtered_spectrum)
	# recon_magnitude = frequency.compute_magnitude(recon_image)

	# show_comparative_images(image, recon_magnitude)
	output_img = "../output_images/test.png"
	cv2.imwrite(output_img, recon_image)

	recon_mean = np.mean(magnitude)
	return (recon_mean, recon_mean <= thresh)