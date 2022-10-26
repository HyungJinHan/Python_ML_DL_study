import cv2
import numpy as np
from OpenCV_show_func import img_show

img = cv2.imread('./images/umm.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corner = cv2.cornerHarris(gray, 2, 3, 0.02)

coord = np.where(corner > 0.1 * corner.max())
coord = np.stack((coord[1], coord[0]), axis=1)

for x, y in coord:
  cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX,cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

merged = np.hstack((corner_norm, img))
# merged_re = cv2.resize(merged, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Harris Corner', merged)
cv2.waitKey()
cv2.destroyAllWindows()

# 시-토마시 검출 (Shi & Tomasi Detect)
# 해리스 코너 검출을 좀더 개선한 알고리즘이다.
# cv2.goodFeaturesToTrack(
#   image,
#   -> 입력 이미지

#   maxCorners,
#   -> 최대 코너 개수
#   (코너 최대 값보다 낮은 개수만 반환 / xCorners <= 0이면 무제한)

#   qualityLevel,
#   -> 코너점 결정을 위한 값으로 환할 코너의 최소 품질을 설정
#   코너 품질은 0.0 ~ 1.0 사이의 값으로 할당할 수 있으며,
#   일반적으로 0.01 ~ 0.10 사이의 값 사용

#   minDistance,
#   -> 코너점 사이의 최소 거리
#   (설정된 최소 거리 이상의 값만 검출)

#   corners,
#   -> 컴출된 코너점 좌표

#   mask=None,
#   -> 마스크 이미지
#   (요소 값이 0인 곳은 코너로 계산하지 않는다.)

#   blockSize=None,
#   -> 코너 검출을 위한 블록 크기 (기본 값은 3)

#   useHarrisDetector=None,
#   -> 해리스 코너 방법 사용 여부 (기본 값은 False)

#   k=None
#   -> 해리스 코너 검출 시 사용할 k 값
# )

# 3차원 실수 행렬(n, 1, 2)로 반환하며 n으로 코너점 검출 개수를 반환한다.
# x 좌표는 [i, 0, 0], y 좌표는 [i, 0, 1]이다.
# 실수로 저장되므로 int로 변환하여 사용해야 한다.