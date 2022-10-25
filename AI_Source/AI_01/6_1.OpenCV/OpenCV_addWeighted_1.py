import cv2
from OpenCV_show_func import img_show

a = 0.0

while(a <= 1.0):
  src_cat = cv2.imread('./images/cat.jpg')
  src_butterfly = cv2.imread('./images/butterfly.jpg')

  width = src_cat.shape[1]
  height = src_cat.shape[0]
  src_butterfly = cv2.resize(src_butterfly, (width, height))

  b = 1.0 - a
  dst = cv2.addWeighted(src_cat, a, src_butterfly, b, 0)
  cv2.imshow('dst', dst)
  cv2.waitKey(0)

  print(a, ',', b)
  a += 0.2

cv2.destroyAllWindows()