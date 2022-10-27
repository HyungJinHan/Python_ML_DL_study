import numpy as np
import cv2
from OpenCV_show_func import img_show

# src = cv2.imread('./images/pencils.jpg')
src = cv2.imread('./images/umm.png')

number1 = np.ones_like(src) * 127
# number2 = np.ones_like(src) * 2 

_max = cv2.max(src, number1)
_min = cv2.min(src, number1)
_abs = cv2.absdiff(src, number1)
# 절대치
compare = cv2.compare(src, number1, cv2.CMP_GT)

src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number1, number1, number1, number1), axis = 1) 

dst = np.concatenate((_max, _min, _abs, compare), axis = 1) 
dst = np.concatenate((src, number, dst), axis = 0)

img_show(['dst'], [dst])
cv2.waitKey(0)
cv2.destroyAllWindows()