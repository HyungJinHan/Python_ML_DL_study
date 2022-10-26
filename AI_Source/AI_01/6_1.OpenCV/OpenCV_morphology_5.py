import numpy as np
import cv2
from OpenCV_show_func import img_show

src = cv2.imread('./images/umm.png')
# src = cv2.imread('./images/morphological.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

gradient = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
# 팽창 + 침식

img_show(['src', 'gradient'], [src, gradient])
# cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()