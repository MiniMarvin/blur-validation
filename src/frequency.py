import numpy as np

def return_to_spatial_domain(spectrum):
	"""
	puts the DC component back at position f(0,0) and computes the inverse FFT to return to the spatial domain
	"""
	uncentered_filtered_spectrum = np.fft.ifftshift(spectrum)
	return np.fft.ifft2(uncentered_filtered_spectrum)

def go_to_frequency_domain(image):
	"""
	compute the FFT to find the frequency transform, then shift the zero frequency component to the center where it will be more easy to analyze
	"""
	fft = np.fft.fft2(image)
	return np.fft.fftshift(fft)

def compute_magnitude(frequency_image):
	"""
	computes the magnitude of the frequency spectrum in a logarithmic approach so we can analyze it properly
	"""
	magnitude = 20*np.log(np.abs(frequency_image))
	return magnitude

def high_pass_filter(frequency_image, frequency_radius):
  (height, width) = frequency_image.shape
  (center_x, center_y) = width // 2, height // 2

  frequency_image[center_y - frequency_radius:center_y + frequency_radius, center_x - frequency_radius:center_x + frequency_radius] = 0

  return frequency_image
