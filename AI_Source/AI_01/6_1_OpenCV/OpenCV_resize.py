import cv2
from OpenCV_show_func import img_show

src_cat = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

dst0 = cv2.resize(
  src_cat,
  dsize=(800, 600),
  interpolation=cv2.INTER_AREA # 축소
)

dst1 = cv2.resize(
  src_cat,
  dsize=(0, 0),
  fx=0.3,
  fy=0.7,
  interpolation=cv2.INTER_LINEAR # 가장 효율적인 확대
)

cv2.imshow('scr_cat', src_cat)
cv2.imshow('dst0', dst0)
cv2.imshow('dst1', dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()