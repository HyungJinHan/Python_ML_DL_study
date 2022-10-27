import cv2
from OpenCV_show_func import img_show

src = cv2.imread('./images/hats.png', cv2.IMREAD_GRAYSCALE)
templit = cv2.imread('./images/umm.png', cv2.IMREAD_GRAYSCALE)

dst = cv2.imread('./images/hats.png')
result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

x, y = minLoc
h, w = templit.shape

dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)
dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

img_show(['templit', 'dst_re'], [templit, dst_re])

# cv2.imshow('dst', dst_re)
cv2.waitKey()
cv2.destroyAllWindows()