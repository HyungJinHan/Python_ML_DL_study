import cv2
from OpenCV_show_func import img_show
import matplotlib.pyplot as plt
import numpy as np

# src = cv2.imread('./images/pencils.jpg')
# src = cv2.imread('./images/umm.png')

alpha = 0.5

src1 = cv2.imread('./images/umm.png')
src1 = cv2.resize(src1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
src2 = cv2.imread('./images/yate.jpg')
# 사진의 사이즈가 같아야 합성 가능

print(src1.shape)
print(src2.shape)

blended = src1 * alpha + src2 * (1 - alpha)
blended = blended.astype(np.uint8)

dst = cv2.addWeighted(src1, alpha, src2, (1 - alpha), 0)
# src1, src2 : 합성할 이미지
# alpha : src1에 지정할 가중치
# beta : src2에 지정할 가중치 (주로 (1 - alpha)로 적용)
# gamma : 연산 결과에 가감할 상수 (주로 0 적용)

img_show(
  ['src1', 'src2', 'blended', 'addWeighted'],
  [src1, src2, blended, dst]
)
cv2.waitKey(0)
cv2.destroyAllWindows()