from OpenCV_show_func import img_show
import cv2

img = cv2.imread('./images/sudoku.jpg')

edge = cv2.Laplacian(img, -1)

img_show(
  ['img', 'Edge'],
  [img, edge]
)

cv2.waitKey(0)
cv2.destroyAllWindows()