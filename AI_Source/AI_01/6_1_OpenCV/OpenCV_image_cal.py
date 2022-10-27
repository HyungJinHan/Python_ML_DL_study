import numpy as np
import cv2
from OpenCV_show_func import img_show

# src = cv2.imread('./images/pencils.jpg')
src = cv2.imread('./images/umm.png')

number1 = np.ones_like(src) * 127 
number2 = np.ones_like(src) * 2 

add = cv2.add(src, number1)
sub = cv2.subtract(src, number1)
mul = cv2.multiply(src, number2)
div = cv2.divide(src, number2)

src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number1, number1, number2, number2), axis = 1) 

dst = np.concatenate((add, sub, mul, div), axis = 1) 
dst = np.concatenate((src, number, dst), axis = 0)

img_show(['dst'], [dst])
cv2.waitKey(0)
cv2.destroyAllWindows()