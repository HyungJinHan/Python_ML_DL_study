import cv2
from OpenCV_show_func import img_show

src = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

dst0 = cv2.flip(src, 0)
dst1 = cv2.flip(src, 1)
dst2 = cv2.flip(src, -1)

img_show(
  ['src', 'dst (0)', 'dst (1)','dst (-1)'],
  [src, dst0, dst1, dst2],
  figsize=(12, 5)
)

cv2.waitKey()
cv2.destroyAllWindows()