import cv2
import numpy as np
from OpenCV_show_func import img_show

img = cv2.imread('./images/ahah1.jpg')

gx_k = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
gy_k = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
# -1 : 입력 이미지와 동일한 타입의 출력 이미지 생성
edge_gy = cv2.filter2D(img, -1, gy_k)

# cv2.imshow('Original img', img)
# cv2.imshow('sobel : edge_gx', gx_k)
# cv2.imshow('sobel : edge_gy', gy_k)
# cv2.imshow('sobel : edge_gx + edge_gy', edge_gx + edge_gy)

img_show(
  ['img', 'edge_gx', 'edge_gy', 'edge_gx + edge_gy'],
  [img, edge_gx, edge_gy, edge_gx + edge_gy]
)

cv2.waitKey(0)
cv2.destroyAllWindows()