import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# 장치 번호를 통해 카메라 찾기

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# 넓이, 높이 설정

# gx_k = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
# gy_k = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

while cv2.waitKey(33) < 0:
  ret, frame = capture.read()
  frame = cv2.flip(frame, 1)
  # frame = cv2.filter2D(frame, -1, gx_k + gy_k)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  cv2.imshow('VideoFrame', frame)

capture.release()
# cv2.destroyAllWindows()
cv2.destroyWindow('VideoFrame')