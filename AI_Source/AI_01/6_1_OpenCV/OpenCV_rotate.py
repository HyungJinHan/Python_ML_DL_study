import cv2
from numpy import matrix

src = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

height, width, channel = src.shape

matrix0 = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 0.7)
matrix1 = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)

print(matrix)

dst0 = cv2.warpAffine(src, matrix0, (width, height))
dst1 = cv2.warpAffine(src, matrix1, (width, height))

cv2.imshow('src', src)
cv2.imshow('dst0', dst0)
cv2.imshow('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()