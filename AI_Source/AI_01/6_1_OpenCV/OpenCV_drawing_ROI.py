import cv2

src = cv2.imread('./images/sunset.jpg')

x, y, w, h = cv2.selectROI('src', src, False)

if w and h:
  roi = src[y:y + h, x:x + w]

  cv2.imshow('cropped', roi)
  cv2.moveWindow('cropped', 0, 0)
  cv2.imwrite('./images/cropped2.jpg', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()