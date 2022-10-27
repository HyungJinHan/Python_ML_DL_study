import cv2
from OpenCV_show_func import img_show
import matplotlib.pyplot as plt

# src = cv2.imread('./images/pencils.jpg')
# src = cv2.imread('./images/umm.png')

src1 = cv2.imread('./images/wing_wall.jpg')
src2 = cv2.imread('./images/yate.jpg')
src3 = src1 + src2
src4 = cv2.add(src1, src2)

srcs = {
  'src1': src1,
  'src2': src2,
  'src1 + src2': src3,
  'cv2.add(src1, src2)': src4,
}
# number2 = np.ones_like(src) * 2 

for i, (k, v) in enumerate(srcs.items()):
  plt.subplot(2, 2, i + 1)
  plt.imshow(v[:, :, ::-1])
  plt.title(k)
  plt.xticks([])
  plt.yticks([])

plt.show()

# img_show(['dst'], [dst])
# cv2.waitKey(0)
# cv2.destroyAllWindows()