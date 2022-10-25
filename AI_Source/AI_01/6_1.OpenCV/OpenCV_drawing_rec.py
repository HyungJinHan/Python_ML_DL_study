import cv2
import numpy as np

src = np.full((768, 1366, 3), 255, dtype=np.uint8)

cv2.rectangle(src, (50, 50), (150, 150), (255, 0, 0))
cv2.rectangle(src, (300, 300), (100, 100), (0, 255, 0), 10)
cv2.rectangle(src, (450, 200), (200, 450), (0, 0, 255), -1)

cv2.imshow('rectangle', src)

cv2.waitKey(0)
cv2.destroyAllWindows()