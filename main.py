import imutils
import cv2
import src.frequency as fq
import numpy as np

base_path = "images/"
img_path = base_path + "fotos-embaçadas-sao-otimas-tambem-09.jpg"

orig = cv2.imread(img_path)
orig = imutils.resize(orig, width=500)
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

output_path = "output_images/"

## blured image parse
cv2.imwrite(output_path + "g1.png", gray)

fft_image = fq.extract_frequencies(gray)
magnitude = fq.compute_magnitude(fft_image)

cv2.imwrite(output_path + "m1.png", magnitude)

## noise image
vals = len(np.unique(gray))
vals = 2 ** np.ceil(np.log2(vals))
noisy = np.random.poisson(gray * vals) / float(vals)
cv2.imwrite(output_path + "g2.png", noisy)

fft_image = fq.extract_frequencies(noisy)
magnitude = fq.compute_magnitude(fft_image)

cv2.imwrite(output_path + "m2.png", magnitude)