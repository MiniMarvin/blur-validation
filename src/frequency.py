import numpy as np

def extract_frequencies(image):
	"""
	compute the FFT to find the frequency transform, then shift the zero frequency component (i.e., DC component located at the top-left corner) to the center where it will be more easy to analyze
	"""
	fft = np.fft.fft2(image)
	fftShift = np.fft.fftshift(fft)
	return fftShift

def compute_magnitude(frequency_image):
	"""
	computes the magnitude of the frequency spectrum in a logarithmic approach so we can analyse it properly.
	"""
	magnitude = 20*np.log(np.abs(frequency_image))
	return magnitude

def high_pass_filter(frequency_image, frequency_radius):
	(height, width) = frequency_image.shape
	(center_x, center_y) = width // 2, height // 2
	filtered_image = np.copy(frequency_image)
	filtered_image[
		center_y - frequency_radius:center_y + frequency_radius, 
		center_x - frequency_radius:center_x + frequency_radius
	] = 0
	return filtered_image