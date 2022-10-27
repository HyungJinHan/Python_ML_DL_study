import cv2
from OpenCV_show_func import img_show
import numpy as np

src_cat = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

smaller = cv2.pyrDown(src_cat)
bigger = cv2.pyrUp(smaller)
laplacian = cv2.subtract(src_cat, bigger)
restored = bigger + laplacian
merged = np.hstack((src_cat, laplacian, bigger, restored))

img_show('Laplacian Pyramid', merged, (16, 4))

cv2.imshow('src_cat', src_cat)
cv2.imshow('smaller', smaller)
cv2.imshow('bigger', bigger)
cv2.imshow('laplacian', laplacian)
cv2.imshow('restored', restored)

cv2.waitKey(0)
cv2.destroyAllWindows()