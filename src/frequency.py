import numpy as np

def return_to_spacial_domain(spectrum):
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
	fftShift = np.fft.fftshift(fft)
	return fftShift

def compute_magnitude(frequency_image):
	"""
	computes the magnitude of the frequency spectrum in a logarithmic approach so we can analyze it properly.
	"""
	magnitude = 20*np.log(np.abs(frequency_image))
	return magnitude

def logistics_interval(size):
	

def high_pass_filter(frequency_image, frequency_radius):
	(height, width) = frequency_image.shape
	(center_x, center_y) = width // 2, height // 2
	filtered_image = np.copy(frequency_image)
	# TODO: implement the reduction with smooth gaussian
	filtered_image[
		center_y - frequency_radius//2:center_y + frequency_radius//2, 
		center_x - frequency_radius//2:center_x + frequency_radius//2
	] = 0

	# apply logistics function reduction from 0 to 1 multiplication for values

	return filtered_image