import cv2

win_name = 'Alpha Blending'
trackbar_name = 'fade'

src1 = cv2.imread('./images/ahah.jpeg')
src2 = cv2.imread('./images/ahah1.jpg')
src1 = cv2.resize(src1, dsize=(640, 475), interpolation=cv2.INTER_AREA)
src2 = cv2.resize(src2, dsize=(640, 475), interpolation=cv2.INTER_AREA)
# src1 = cv2.imread('./images/man_face.jpg')
# src2 = cv2.imread('./images/lion_face.jpg')
print(src2.shape)

def onChange(x):
  alpha = x / 100
  dst = cv2.addWeighted(src2, 1 - alpha, src1, alpha, 0)
  cv2.imshow(win_name, dst)

cv2.imshow(win_name, src2)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()