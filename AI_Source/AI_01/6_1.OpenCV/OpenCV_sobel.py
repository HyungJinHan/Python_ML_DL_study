from OpenCV_show_func import img_show
import cv2

img = cv2.imread('./images/sudoku.jpg')

sobelx = cv2.Sobel(
  img,
  -1,
  1,
  0,
  ksize=3
)

sobely = cv2.Sobel(
  img,
  -1,
  0,
  1,
  ksize=3
)

img_show(
  ['img', 'Sobel (x)', 'Sobel (y)', 'Sobel (x) + Sobel (y)'],
  [img, sobelx, sobely, sobelx + sobely]
)

cv2.waitKey(0)
cv2.destroyAllWindows()