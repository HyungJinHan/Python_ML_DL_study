import cv2
import numpy as np

win_name = 'scanning'
img = cv2.imread('./images/paper.jpg')
row, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
  global pts_cnt, draw

  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle(draw, (x, y), 10, (0, 0, 0), 2)
    # -1 : 내부 채우기 / 1 : 내부 비우기
    cv2.imshow(win_name, draw)

    pts[pts_cnt] = [x, y]
    pts_cnt += 1

    if pts_cnt == 4:
      sm = pts.sum(axis=1)
      diff = np.diff(pts, axis=1)

      topLeft = pts[np.argmin(sm)]
      bottomRight = pts[np.argmax(sm)]
      topRight = pts[np.argmin(diff)]
      bottomLeft = pts[np.argmax(diff)]

      pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])
      w1 = abs(bottomRight[0] - bottomLeft[0])
      w2 = abs(topRight[0] - topLeft[0])
      h1 = abs(topRight[1] - bottomRight[1])
      h2 = abs(topLeft[1] - bottomLeft[1])

      width = int(max([w1, w2]))
      height = int(max([h1, h2]))

      pts2 = np.float32([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
      ])
      mtrx = cv2.getPerspectiveTransform(pts1, pts2)
      result = cv2.warpPerspective(img, mtrx, (width, height))

      cv2.imshow('Scanned', result)
    
  elif event == cv2.EVENT_RBUTTONDOWN:
    pts_cnt = 0
    draw = img.copy()
    cv2.imshow(win_name, draw)
    # 우클릭 시, 카운트 초기화 및 복사된 이미지 다시 불러오기
    # 위에서 전역 변수로써 사용한다고 선언해야 함

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
