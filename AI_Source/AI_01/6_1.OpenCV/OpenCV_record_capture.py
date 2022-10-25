import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened:
  file_path = 'C:/Users/han12/OneDrive/Desktop/AIschool/Python/AI_Source/AI_01/6_1.OpenCV/recordTest.avi'
  fps = 30.0
  fourcc = cv2.VideoWriter_fourcc(*'DIVX')
  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
  size = (int(width), int(height))
  out = cv2.VideoWriter(file_path, fourcc, fps, size)

  while True:
    ret, frame = cap.read()

    if ret:
      cv2.imshow('Camera_Recording', frame)
      out.write(frame)

      if cv2.waitKey(int(1000 / fps)) != -1:
        break

    else:
      print('No Frame')
      break
    
  out.release()

else:
  print("Can't Open Camera")

cap.release()

cv2.destroyAllWindows()