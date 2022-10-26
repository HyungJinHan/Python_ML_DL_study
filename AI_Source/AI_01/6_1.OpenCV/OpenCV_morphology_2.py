import numpy as np
import cv2
from OpenCV_show_func import img_show

src = cv2.imread('./images/umm.png')
# src = cv2.imread('./images/morph_hole.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

dst = cv2.dilate(src, kernel)
# 팽창 함수

img_show(['src', "dst"], [src, dst])
# cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()