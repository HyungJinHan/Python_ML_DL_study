import numpy as np
import cv2
from OpenCV_show_func import img_show

src = cv2.imread('./images/office.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations=9)
dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

img_show(['src', "dst"], [src, dst])
# cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()