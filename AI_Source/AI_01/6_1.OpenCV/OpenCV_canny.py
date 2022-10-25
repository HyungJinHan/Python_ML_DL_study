from OpenCV_show_func import img_show
import cv2

img = cv2.imread('./images/sudoku.jpg')

edge_canny = cv2.Canny(img, 100, 200)
edge_laplacian = cv2.Laplacian(img, -1)
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)

img_show(
  ['img', 'Edge (Canny)', 'Edge (Laplacian)', 'Sobel (x + y)'],
  [img, edge_canny, edge_laplacian, sobelx + sobely]
)

cv2.waitKey(0)
cv2.destroyAllWindows()