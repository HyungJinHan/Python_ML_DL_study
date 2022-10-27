import numpy as np
import cv2
import matplotlib.pylab as plt
from OpenCV_show_func import img_show

# src = cv2.imread('./images/yeosu.jpg')
src = cv2.imread('./images/umm.png')
mask = np.zeros_like(src)

cv2.circle(mask, (235, 266), 180, (255, 255, 255), -1)
# cv2.circle(대상이미지, (원점x, 원점y), 반지름, (색상), 찿우기)

masked = cv2.bitwise_and(src, mask)

img_show(
  ['Original', 'Mask', 'Masked'],
  [src, mask, masked]
)

cv2.waitKey()
cv2.destroyAllWindows()