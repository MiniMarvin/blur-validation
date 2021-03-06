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

def detect_blur_fft(image, frequency_threshold=60, filter_type="square", ranking_type="mean", file_name="test"):
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

  if filter_type == "smooth_square":
    filtered_spectrum = frequency.square_smooth_high_pass_filter(fft_image, frequency_threshold)
  elif filter_type == "smooth_circle":
    filtered_spectrum = frequency.circle_smooth_high_pass_filter(fft_image, frequency_threshold)
  elif filter_type == "circle":
    filtered_spectrum = frequency.circle_high_pass_filter(fft_image, frequency_threshold)
  else:
    filtered_spectrum = frequency.square_high_pass_filter(fft_image, frequency_threshold)

  filtered_magnitude = frequency.compute_magnitude(filtered_spectrum)

  path = base_path + file_name + "/" + "frequency_domain_2.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, filtered_magnitude)
    
  recon_image = frequency.return_to_spatial_domain(filtered_spectrum)
  recon_magnitude = frequency.compute_magnitude(recon_image)

  path = base_path + file_name + "/" + "spatial_domain_2.png"
  mf.ensure_dir(path)
  cv2.imwrite(path, recon_magnitude)

  recon_score = 0

  if ranking_type == "mean":
    recon_mean = np.mean(recon_magnitude)
    recon_mean = np.mean(filtered_magnitude[filtered_magnitude >= -100])
    recon_score = recon_mean
  else:
    recon_variance = -np.var(filtered_magnitude[filtered_magnitude >= -100])
    recon_score = recon_variance
    
  return recon_score