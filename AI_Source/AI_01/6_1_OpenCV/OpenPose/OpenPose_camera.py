import cv2
from pathlib import Path

# MPII ver
BODY_PARTS = {
  # 'Head': 0,
  'Neck': 1,
  'RShoulder': 2,
  'RElbow': 3,
  'RWrist': 4,
  'LShoulder': 5,
  'LElbow': 6,
  'LWrist': 7,
  'RHip': 8,
  'RKnee': 9,
  'RAnkle': 10,
  'LHip': 11,
  'LKnee': 12,
  'LAnkle': 13,
  'Chest': 14,
  'Background': 15
}

POSE_PAIRS = [
  # ['Head', 'Neck'],
  ['Neck', 'RShoulder'],
  ['RShoulder', 'RElbow'],
  ['RElbow', 'RWrist'],
  ['Neck', 'LShoulder'],
  ['LShoulder', 'LElbow'],
  ['LElbow', 'LWrist'],
  ['Neck', 'Chest'],
  ['Chest', 'RHip'],
  ['RHip', 'RKnee'],
  ['RKnee', 'RAnkle'],
  ['Chest', 'LHip'],
  ['LHip', 'LKnee'],
  ['LKnee', 'LAnkle']
]

# COCO Output Format Nose – 0, Neck – 1, Right Shoulder – 2, Right Elbow – 3, Right Wrist – 4, Left Shoulder – 5, Left Elbow – 6, Left Wrist – 7, Right Hip – 8, Right Knee – 9, Right Ankle – 10, Left Hip – 11, Left Knee – 12, LAnkle – 13, Right Eye – 14, Left Eye – 15, Right Ear – 16, Left Ear – 17, Background – 18 

# 각 파일 path
BASE_DIR = Path(__file__).resolve().parent
protoFile = str(BASE_DIR) + '../../../OpenCV/file/pose_deploy_linevec_faster_4_stages.prototxt'
weightsFile = str(BASE_DIR) + '../../../OpenCV/file/pose_iter_160000.caffemodel'

# 위의 path에 있는 network 모델 불러오기
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

#쿠다 사용 안하면 밑에 이미지 크기를 줄이는게 나을 것이다
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA) #벡엔드로 쿠다를 사용하여 속도향상을 꾀한다
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA) # 쿠다 디바이스에 계산 요청

# 카메라 연결
capture = cv2.VideoCapture(0) # 0번 카메라 (웹캠)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #카메라 속성 설정
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # width:너비, height: 높이

inputWidth = 320
inputHeight = 240
inputScale = 1.0 / 255

# 반복문을 통한 카메라 프레임 지속적으로 받기
while cv2.waitKey(1) < 0:
  # 웹캠으로부터 영상 가져오기
  hasFrame, frame = capture.read()
  frame = cv2.flip(frame, 1)

  # 영상이 커서 느리면 사이즈를 줄이자
  # frame=cv2.resize(frame,dsize=(320,240),interpolation=cv2.INTER_AREA)

  # 웹캠으로 영상 가져오지 못하면 웹캠 중기
  if not hasFrame:
    cv2.waitKey()
    break

  frameWidth = frame.shape[1]
  frameHeight = frame.shape[0]

  inpBlob = cv2.dnn.blobFromImage(
    frame,
    inputScale,
    (inputWidth, inputHeight),
    (0, 0, 0),
    swapRB=False,
    crop=False
  )

  imgb=cv2.dnn.imagesFromBlob(inpBlob)
  # cv2.imshow("motion",(imgb[0]*255.0).astype(np.uint8))

  # network에 넣어주기
  net.setInput(inpBlob)

  # 결과 받아오기
  output = net.forward()

  # 키포인트 검출 시 이미지에 그려줌
  points = []

  for i in range(0, 15):
    # 해당 신체 부위 신뢰도 얻음
    probMap = output[0, i, :, :]

    # global 최대값 찾기
    minVal, prob, minloc, point = cv2.minMaxLoc(probMap)

    # 원래 이미지에 맞게 점 위치 변경
    x = (frameWidth * point[0]) / output.shape[3]
    y = (frameHeight * point[1]) / output.shape[2]

    # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로
    if prob > 0.1:    
        cv2.circle( # circle(그릴곳, 원의 중심, 반지름, 색)
          frame,
          (int(x), int(y)),
          3,
          (0, 255, 255),
          thickness=-1,
          lineType=cv2.FILLED
        )

        cv2.putText(
          frame,
          "{}".format(i),
          (int(x), int(y)),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.5,
          (0, 0, 255),
          1,
          lineType=cv2.LINE_AA
        )

        points.append((int(x), int(y)))
    else:
        points.append(None)

  # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
  for pair in POSE_PAIRS:
    partA = pair[0] # Head
    partA = BODY_PARTS[partA] # 0
    partB = pair[1] # Neck
    partB = BODY_PARTS[partB] # 1

    # partA와 partB 사이에 선을 그어줌 (cv2.line)
    if points[partA] and points[partB]:
      cv2.line(
        frame,
        points[partA],
        points[partB],
        (0, 255, 0),
        2
      )

  cv2.imshow('Output-Keypoints', frame)

capture.release() # 카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows()