import cv2
import numpy as np

src = np.full((768, 1366, 3), 255, dtype=np.uint8)

cv2.circle(src, (150, 150), 100, (255, 0, 0))
cv2.circle(src, (300, 150), 70, (0, 255, 0), 5)
cv2.circle(src, (400, 150), 50, (0, 0, 255), -1)

cv2.ellipse(src, (50, 300), (50, 50), 0, 0, 360, (0, 0, 255)) 
cv2.ellipse(src, (150, 300), (50, 50), 0, 0, 180, (255, 0, 0))
cv2.ellipse(src, (200, 300), (50, 50), 0, 181, 360, (0, 0, 255))
cv2.ellipse(src, (325, 300), (75, 50), 0, 0, 360, (0, 255, 0))
cv2.ellipse(src, (450, 300), (50, 75), 0, 0, 360, (255, 0, 255))
cv2.ellipse(src, (50, 425), (50, 75), 15, 0, 360, (0, 0, 0))
cv2.ellipse(src, (200, 425), (50, 75), 45, 0, 360, (0, 0, 0))
cv2.ellipse(src, (350, 425), (50, 75), 45, 0, 180, (0, 0, 255))
cv2.ellipse(src, (400, 425), (50, 75), 45, 181, 360, (255, 0, 0))

cv2.imshow('circle', src)

cv2.waitKey(0)
cv2.destroyAllWindows()