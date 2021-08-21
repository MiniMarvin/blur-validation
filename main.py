import imutils
import cv2
import src.image_processing as ip

base_path = "images/"
img_path = base_path + "10.jpg"

orig = cv2.imread(img_path)
orig = imutils.resize(orig, width=500)
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

output_path = "output_images/"

ip.detect_blur_fft(gray, 50, 15)
