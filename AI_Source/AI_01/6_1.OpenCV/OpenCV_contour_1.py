import cv2
import matplotlib.pyplot as plt
from OpenCV_show_func import img_show

img = cv2.imread('./images/umm.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(
  img_gray,
  127,
  255,
  0
)

# plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
# plt.show()

contours, _ = cv2.findContours(
  thresh,
  cv2.RETR_TREE,
  cv2.CHAIN_APPROX_SIMPLE
)

img1 = cv2.drawContours(
  img,
  contours,
  -1, 
  (0, 255, 0),
  4
)

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
# plt.show()

umm = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
joon = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
sik = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img_show(
  ['umm...', 'joon...', 'sik...'],
  [umm, joon, sik]
)