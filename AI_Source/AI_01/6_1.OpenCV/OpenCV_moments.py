import cv2
from OpenCV_show_func import img_show

img = cv2.imread('./images/convex.png')
dst = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours:
  # 윤곽선에서 모멘트를 계산 후 dict 타입의 객체로 반환
  print(i.shape)
  M = cv2.moments(i)
  cX = int(M['m10'] / M['m00'])
  cY = int(M['m01'] / M['m00'])

  cv2.circle(dst, (cX, cY), 3, (255, 0, 0), -1)
  cv2.drawContours(dst, [i], 0, (0, 0, 255), 2)

img_show(['dst'], [dst])
# cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()