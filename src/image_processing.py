from . import frequency
from . import manage_file as mf
import numpy as np
import cv2
import imutils

def gray_image(img_path):
	orig = cv2.imread(img_path)
	orig = imutils.resize(orig, width=500)
	gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
	return gray

def detect_blur_fft(image, frequency_threshold=60, file_name="test"):
  """
  computes if the image is blurry (i.e. a low definition image), by processing the image with a high pass filter on frequency spectrum
  """
  base_path = "output_images/"
  path = base_path + file_name + "/" + "spatial_domain_1.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, image)

  fft_image = frequency.go_to_frequency_domain(image)
  magnitude = frequency.compute_magnitude(fft_image)

  path = base_path + file_name + "/" + "frequency_domain_1.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, magnitude)

  # filtered_spectrum = frequency.square_high_pass_filter(fft_image, frequency_threshold)

  # filtered_spectrum = frequency.circle_high_pass_filter(fft_image, frequency_threshold)

  filtered_spectrum = frequency.circle_smooth_high_pass_filter(fft_image, frequency_threshold)

  filtered_magnitude = frequency.compute_magnitude(filtered_spectrum)

  path = base_path + file_name + "/" + "frequency_domain_2.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, filtered_magnitude)
    
  recon_image = frequency.return_to_spatial_domain(filtered_spectrum)
  recon_magnitude = frequency.compute_magnitude(recon_image)

  path = base_path + file_name + "/" + "spatial_domain_2.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, recon_magnitude)

  recon_mean = np.mean(recon_magnitude)
  return recon_mean