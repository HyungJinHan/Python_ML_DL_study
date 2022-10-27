from OpenCV_show_func import img_show
import cv2
import numpy as np

src = cv2.imread('./images/Billiard.jpg', cv2.IMREAD_COLOR)
src_b, src_g, src_r = cv2.split(src)

zeros = np.zeros((src.shape[0], src.shape[1], 1), dtype='uint8')

# src_b = cv2.merge([src_b, zeros, zeros])
# src_g = cv2.merge([zeros, src_g, zeros])
# src_r = cv2.merge([zeros, zeros, src_r])

src_b1 = cv2.merge([src_b, zeros, zeros])
src_g1 = cv2.merge([zeros, src_g, zeros])
src_r1 = cv2.merge([zeros, zeros, src_r])
src_rgb = cv2.merge([src_r, src_g, src_b])

img_show(
  ['BGR', 'B', 'G', 'R', 'RGB'],
  [src, src_b1, src_g1, src_r1, src_rgb],
  (16, 4)
)

cv2.waitKey()
cv2.destroyAllWindows()