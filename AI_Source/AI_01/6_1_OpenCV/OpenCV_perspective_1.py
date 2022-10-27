import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/perspective.jpg')

pts1 = np.float32([[504, 1003], [243, 1525], [1000, 1000], [1280, 1685]])
pts2 = np.float32([[10, 10], [10, 1000], [1000, 10], [1000, 1000]])

cv2.circle(img, (504, 1003), 20, (255, 0, 0), -1)
cv2.circle(img, (243, 1524), 20, (0, 255, 0), -1)
cv2.circle(img, (1000, 1000), 20, (0, 0, 255), -1)
cv2.circle(img, (1280, 1685), 20, (0, 0, 0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (1100, 1100))

plt.subplot(121),plt.imshow(img)
plt.title('image')

plt.subplot(122),plt.imshow(dst)
plt.title('Perspective')

plt.show()