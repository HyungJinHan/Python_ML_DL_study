import datetime
import cv2

capture = cv2.VideoCapture('./images/youquiz4.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
  if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
    capture.open('./images/youquiz4.mp4')

  ret, frame = capture.read()

  cv2.imshow('VideoFrame', frame)

  now = datetime.datetime.now().strftime('%d_%H-%M-%S')
  
  key = cv2.waitKey(33)
  print('key ->', key)

  # 종료
  if key == 27:
    # 27 : ESC
    break

  # 캡쳐
  elif key == 49:
    # 49 : 숫자 1
    print('캡쳐')
    cv2.imwrite(
      './capture/' + str(now) + '.png',
      frame
    )

  # 녹화
  elif key == 50:
    # 50 : 숫자 2
    print('녹화 시작')
    record = True
    video = cv2.VideoWriter(
      './capture/' + str(now) + '.avi',
      fourcc,
      20.0,
      (frame.shape[1], frame.shape[0])
    )

  # 녹화 중지
  elif key == 51:
    # 51 : 숫자 3
    print('녹화 중지')
    record = False
    video.release()

  elif record == True:
    print('녹화 중...')
    video.write(frame)

capture.release()
cv2.destroyAllWindows()