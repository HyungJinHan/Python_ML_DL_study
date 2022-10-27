import cv2

src = cv2.imread('./images/ahah1.jpg')

isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)

def onMouse(event, x, y, flags, param):
  global isDragging, x0, y0, src

  if event == cv2.EVENT_LBUTTONDOWN:
    isDragging = True
    x0 = x
    y0 = y

  elif event == cv2.EVENT_MOUSEMOVE:
    if isDragging:
      src_draw = src.copy()

      cv2.rectangle(src_draw, (x0, y0), (x, y), blue, 2)
      cv2.imshow('src', src_draw)

  elif event == cv2.EVENT_LBUTTONUP:
    if isDragging:
      isDragging = False

      w = x - x0
      h = y - y0

      print('x : %d, y : %d, w : %d, h : %d' % (x0, y0, w, h))

      if w > 0 and h > 0:
        src_draw = src.copy()

        cv2.rectangle(src_draw, (x0, y0), (x, y), red, 2)
        cv2.imshow('src', src_draw)

        roi = src[y0:y0 + h, x0:x0 + w]

        cv2.imshow('cropped', roi)
        cv2.moveWindow('cropped', 0, 0)
        cv2.imwrite('./images/cropped.jpg', roi)
        print('Cropped!')

      else:
        cv2.imshow('src', src)
        print('원하는 영역을 드래그하세요.')

cv2.imshow('src', src)
cv2.setMouseCallback('src', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()