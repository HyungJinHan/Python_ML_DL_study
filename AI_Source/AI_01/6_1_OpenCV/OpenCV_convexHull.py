import cv2

img = cv2.imread('./images/star.jpg')
img1 = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[1]

cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)

check = cv2.isContourConvex(contour)

if not check:
  hull = cv2.convexHull(contour)
  cv2.drawContours(img1, [hull], 0, (0, 0, 255), 3)

  cv2.imshow('convexHull', img1)

cv2.imshow('contour', img)
cv2.waitKey()
cv2.destroyAllWindows()
