import cv2 
import numpy as np
src = cv2.imread("./images/harvest.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)

dst = cv2.warpPerspective(src, matrix, (width, height))
src = cv2.resize(src, dsize=(800, 600), interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst, dsize=(800, 600), interpolation=cv2.INTER_AREA)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey() 
cv2.destroyAllWindows()