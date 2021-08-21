import imutils
import cv2
import matplotlib.pyplot as plt

base_path = "images/"
img_path = base_path + "fotos-embaçadas-sao-otimas-tambem-09.jpg"

orig = cv2.imread(img_path)
orig = imutils.resize(orig, width=500)
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")