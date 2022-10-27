import numpy as np
import cv2
from OpenCV_show_func import img_show

src = cv2.imread('./images/umm.png')
# src = cv2.imread('./images/morph_dot.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

dst1 = cv2.erode(src, kernel)
# 침식 함수

dst2 = cv2.dilate(src, kernel)
# 팽창 함수

img_show(['src', "erode", 'dilate'], [src, dst1, dst2])
# cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()