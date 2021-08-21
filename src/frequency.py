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
	filtered_image = np.copy(frequency_image)

	filtered_image[
		center_y - frequency_radius//2:center_y + frequency_radius//2, 
		center_x - frequency_radius//2:center_x + frequency_radius//2
	] = 0

	return filtered_image

def gaussian_2d(x, y, mu1, mu2, sig):
    return np.exp(- (np.power(x - mu1, 2) + np.power(x - mu2, 2)) / (2 * np.power(sig, 2)))

def gen_gaussian_2d_filter(size, radius):
    grid = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] = gaussian_2d(i, j, size/2, size/2, radius)
    return np.array(grid)

def smooth_high_pass_filter(frequency_image, filter_size, gaussian_radius):
	f = gen_gaussian_2d_filter(filter_size, gaussian_radius)

	(height, width) = frequency_image.shape
	(center_x, center_y) = width // 2, height // 2
	filtered_image = np.copy(frequency_image)
	filtered_image = filtered_image[
		center_x - filter_size//2:center_x + filter_size//2,
		center_y - filter_size//2:center_y + filter_size//2] * f
	return filtered_image
