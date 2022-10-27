import cv2

src = cv2.imread('./images/ahah1.jpg', cv2.IMREAD_COLOR)

for ksize in (3, 9, 15, 21):
  dst = cv2.blur(
    src,
    (ksize, ksize),
    anchor=(-1, -1),
    borderType=cv2.BORDER_DEFAULT
  )

  desc = 'Mean : {} X {}'.format(ksize, ksize)

  cv2.putText(
    dst,
    desc,
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,
    255,
    1,
    cv2.LINE_AA
  )

  cv2.imshow('dst', dst)
  cv2.waitKey()

cv2.destroyAllWindows()