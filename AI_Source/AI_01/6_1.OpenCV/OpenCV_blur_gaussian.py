import cv2

src = cv2.imread('./images/ahah1.jpg', cv2.IMREAD_COLOR)

for ksize in (3, 3 * 5, 3 * 7, 3 * 9):
  # dst = cv2.GaussianBlur(
  #   src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None
  # )
  # src : 입력 이미지
  # ksize : 가우시안 커널 사이즈
  # sigmaX : X방향 sigma
  # sigmaY : Y방향 sigma
  # borderType : 가장자리 픽셀 확장 방식

  dst = cv2.GaussianBlur(
    src,
    (ksize, ksize),
    0
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