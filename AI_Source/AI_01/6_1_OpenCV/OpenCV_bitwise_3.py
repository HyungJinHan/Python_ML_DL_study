import numpy as np
import cv2
from OpenCV_show_func import img_show

src_logo = cv2.imread('./images/haduri.png', cv2.IMREAD_UNCHANGED)
src_logo = cv2.resize(
  src_logo,
  dsize=(0, 0),
  fx=0.3,
  fy=0.3,
  interpolation=cv2.INTER_LINEAR
)
src_bg = cv2.imread('./images/umm1.png')

_, mask = cv2.threshold(src_logo[:, :, 3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

src_logo = cv2.cvtColor(src_logo, cv2.COLOR_BGRA2BGR)
h, w = src_logo.shape[:2]
roi = src_bg[10:10 + h, 10:10 + w]

masked_logo = cv2.bitwise_and(src_logo, src_logo, mask=mask)
masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

added = masked_logo + masked_bg
src_bg[10:10 + h, 10:10 + w] = added

cv2.imshow('result', src_bg)
img_show(
  ['mask', 'mask_inv', 'masked_logo', 'masked_bg', 'added', 'result'],
  [mask, mask_inv, masked_logo, masked_bg, added, src_bg],
  (12, 3)
)
img_show(
  ['result'],
  [src_bg]
)
cv2.waitKey()
cv2.destroyAllWindows()