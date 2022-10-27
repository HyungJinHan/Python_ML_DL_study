from OpenCV_show_func import img_show
import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./images/ahah.jpeg')

gray = cv2.cvtColor(
  src,
  cv2.COLOR_BGR2GRAY
)

binary0 = cv2.adaptiveThreshold(
  gray,
  255,
  cv2.ADAPTIVE_THRESH_MEAN_C,
  cv2.THRESH_BINARY,
  467,
  37
)

_, binary1 = cv2.threshold(
  gray,
  130,
  255,
  cv2.THRESH_BINARY
)

binary_re0 = cv2.resize(
  binary0,
  dsize=(0, 0),
  fx=0.7,
  fy=0.7,
  interpolation=cv2.INTER_LINEAR
)

binary_re1 = cv2.resize(
  binary1,
  dsize=(0, 0),
  fx=0.7,
  fy=0.7,
  interpolation=cv2.INTER_LINEAR
)

img_show(
  ['src', 'gray', 'Adaptive Threshold', 'Threshold'],
  [src, gray, binary_re0, binary_re1],
  (16, 5)
)

# cv2.imshow('binary', binary_re)
cv2.waitKey(0)
cv2.destroyAllWindows()