import numpy as np
import cv2

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

def square_high_pass_filter(frequency_image, frequency_radius):
  (height, width) = frequency_image.shape
  (center_x, center_y) = width // 2, height // 2

  frequency_image[center_y - frequency_radius:center_y + frequency_radius, center_x - frequency_radius:center_x + frequency_radius] = 0

  return frequency_image

def circle_high_pass_filter(frequency_image, frequency_radius):
  (height, width) = frequency_image.shape[:2]
  (center_x, center_y) = width // 2, height // 2
  
  Y, X = np.ogrid[:height, :width]

  dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)

  mask = dist_from_center <= frequency_radius
  frequency_image[mask] = 0

  return frequency_image

def circle_smooth_high_pass_filter(frequency_image, frequency_radius):
  (height, width) = frequency_image.shape[:2]
  (center_x, center_y) = width // 2, height // 2

  filter_mask = np.full((height, width), 255, dtype = np.uint8)
  filter_mask = cv2.circle(filter_mask, 
    (center_x, center_y), 
    frequency_radius, 0, -1)
    
  kernel_size = frequency_radius//10
  filter_mask = cv2.GaussianBlur(filter_mask,
  (kernel_size,kernel_size),0)/255.0
  masked_image = frequency_image * filter_mask

  return masked_image