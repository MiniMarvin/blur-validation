import frequency
import numpy as np
import matplotlib.pyplot as plt

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

def detect_blur_fft(image, frequency_threshold=60, thresh=10):
	"""
	Computes if the image is blurry (i.e. a low definition image), by processing the image with a high pass filter on its spectrum.
	"""
	fft_image = frequency.extract_frequencies(image)
	magnitude = frequency.compute_magnitude(fft_image)
	show_comparative_images(image, magnitude)

	filtered_spectrum = frequency.high_pass_filter(
		fft_image, frequency_threshold)
	uncentered_filtered_spectrum = np.fft.ifftshift(filtered_spectrum)
	recon_image = np.fft.ifft2(uncentered_filtered_spectrum)

	recon_magnitude = frequency.compute_magnitude(recon_image)
	show_comparative_images(image, recon_magnitude)

	recon_mean = np.mean(magnitude)
	return (recon_mean, recon_mean <= thresh)