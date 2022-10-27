import numpy as np
import cv2
import matplotlib.pylab as plt
from OpenCV_show_func import img_show

# src = cv2.imread('./images/yeosu.jpg')
src1 = cv2.imread('./images/umm1.png')
src2 = cv2.imread('./images/umm.png')

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)

_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_red = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
diff_red[:, :, 2] = 0

spot = cv2.bitwise_xor(src2, diff_red)

img_show(
  ['src1', 'src2', 'diff', 'spot'],
  [src1, src2, diff, spot],
  (16, 4)
)

cv2.waitKey()
cv2.destroyAllWindows()