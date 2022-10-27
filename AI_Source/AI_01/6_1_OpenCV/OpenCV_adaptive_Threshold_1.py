from OpenCV_show_func import img_show
import cv2
import matplotlib.pylab as plt

blk_size = 9
C = 5

img = cv2.imread('./images/ahah.jpeg', cv2.IMREAD_GRAYSCALE)

ret, th0 = cv2.threshold(
  img,
  0,
  255,
  cv2.THRESH_BINARY | cv2.THRESH_OTSU
)

th1 = cv2.adaptiveThreshold(
  img,
  255,
  cv2.ADAPTIVE_THRESH_MEAN_C, # 산술 평균 계산
  cv2.THRESH_BINARY,
  blk_size,
  C
)

th2 = cv2.adaptiveThreshold(
  img,
  255,
  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # 가우시안 분포에 따른 가중치 합
  cv2.THRESH_BINARY,
  blk_size,
  C
)

imgs = {
  'Original': img,
  'Global-Otsu : %d' %ret: th0,
  'Adaptive-Mean': th1,
  'Adaptive-Gaussian': th2
}

for i, (k, v) in enumerate(imgs.items()):
  plt.subplot(2, 2, i + 1)
  plt.title(k)
  plt.imshow(v, 'gray')
  plt.xticks([])
  plt.yticks([])

plt.show()