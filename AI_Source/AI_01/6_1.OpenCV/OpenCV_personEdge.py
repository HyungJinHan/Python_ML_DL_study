import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, frame = cap.read()
  frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
  # INTER_AREA을 통한 축소 작업
  frame = cv2.flip(frame, 1)

  if cv2.waitKey(1) == 27:
    # 27 : ESC
    break

  img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)

  edges = cv2.Laplacian(img_gray, -1, None, 5)
  
  ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

  sketch = cv2.medianBlur(sketch, 5)
  img_sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

  img_paint = cv2.blur(frame, (10, 10))
  img_paint = cv2.bitwise_and(img_paint, img_paint, mask=sketch)
  # 메모리에 저장된 이진수를 대응되는 것들끼리 연산하기
  # 결과 : 컬러로 비디오 출력

  merged = np.hstack((img_sketch, img_paint))

  cv2.imshow('Sketch Camera', merged)

cap.release()
cv2.destroyAllWindows()