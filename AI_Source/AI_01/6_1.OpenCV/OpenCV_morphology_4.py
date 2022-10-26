import numpy as np
import cv2
from OpenCV_show_func import img_show

# src1 = cv2.imread('./images/umm.png')
src1 = cv2.imread('./images/morph_dot.png')
src2 = cv2.imread('./images/morph_hole.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

opening = cv2.morphologyEx(src1, cv2.MORPH_OPEN, kernel)
# 침식 함수
closing = cv2.morphologyEx(src2, cv2.MORPH_CLOSE, kernel)
# 팽창 함수

merged1 = np.hstack((src1, opening))
merged2 = np.hstack((src2, closing))

img_show(['MORPH_OPEN', 'MORPH_CLOSE'], [merged1, merged2])
# cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()