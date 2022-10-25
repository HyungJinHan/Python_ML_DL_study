import cv2
import numpy as np

src = np.full((768, 1366, 3), 255, dtype=np.uint8)

pts1 = np.array([[50, 50], [150, 150], [100, 140], [200, 240]], dtype=np.int32)
pts2 = np.array([[350, 50], [250, 200], [450, 200]], dtype=np.int32)
pts3 = np.array([[150, 300], [50, 450], [450, 200]], dtype=np.int32)
pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype=np.int32)

cv2.polylines(src, [pts1], False, (255, 0, 0))
cv2.polylines(src, [pts2], False, (0, 0, 0), 10)
cv2.polylines(src, [pts3], True, (0, 0, 255), 10)
cv2.polylines(src, [pts4], True, (0, 0, 0))

cv2.imshow('polyline', src)

cv2.waitKey(0)
cv2.destroyAllWindows()