from OpenCV_show_func import img_show
import cv2
import numpy as np

src = cv2.imread('./images/sosege.jpg', cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
inverse = cv2.merge((r, g, b))

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype='uint8')

bgz = cv2.merge((b, g, zero))

img_show(
  ['src', 'b', 'g', 'r', 'inverse', 'bgz'],
  [src, b, g, r, inverse, bgz],
  (16, 4)
)

cv2.waitKey()
cv2.destroyAllWindows()