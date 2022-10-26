import cv2

src = cv2.imread('./images/umm.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(
  gray,
  127,
  255,
  cv2.THRESH_BINARY
)

binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(
  binary,
  cv2.RETR_CCOMP,
  cv2.CHAIN_APPROX_NONE
)

print(len(contours))

for i in range(len(contours)):
  cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
  cv2.putText(
    src,
    str(i),
    tuple(contours[i][0][0]),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (0, 255, 0),
    1
  )

  print(i, hierarchy[0][i])

  cv2.imshow('src', src)
  cv2.waitKey()

cv2.destroyAllWindows()