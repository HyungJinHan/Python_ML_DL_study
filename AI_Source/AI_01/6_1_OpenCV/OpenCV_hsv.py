from OpenCV_show_func import img_show
import cv2

src = cv2.imread('./images/tomato.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
h, s, v = cv2.split(hsv)
# r, g, b = cv2.split(rgb)

img_show(
  ['Original', 'HSV', 'H', 'S', 'V'],
  [src, hsv, h, s, v],
  (12, 10)
)

cv2.waitKey()
cv2.destroyAllWindows()