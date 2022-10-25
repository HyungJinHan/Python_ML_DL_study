import cv2
import numpy as np

src = np.full((768, 1366, 3), 255, dtype=np.uint8)

cv2.putText

cv2.imshow('rectangle', src)
cv2.imshow('polyline', src)
cv2.imshow('circle', src)

cv2.waitKey(0)
cv2.destroyAllWindows()