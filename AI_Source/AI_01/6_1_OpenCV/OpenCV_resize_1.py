import cv2
from OpenCV_show_func import img_show
import imutils

def print_image_info(image):
  print('이미지 사이즈 : {}'.format(image.shape))
  print('이미지 dtype : {}'.format(image.dtype))
  print('이미지 Height : {}'.format(image.shape[0]))
  print('이미지 Width : {}'.format(image.shape[1]))
  print('이미지 전체 픽셀 개수 : {}'.format(image.size))

src_cat = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

print_image_info(src_cat)
img_show(['Original'], [src_cat])
print('-------------------------------')

width = 200
aspect_ratio = float(width) / src_cat.shape[1]
dsize = (width, int(src_cat.shape[0] * aspect_ratio))
resized = cv2.resize(src_cat, dsize, interpolation=cv2.INTER_AREA)
print_image_info(resized)
img_show('Resized (Width)', resized)
print('-------------------------------')

height = 100
aspect_ratio = float(height) / src_cat.shape[0]
dsize = (height, int(src_cat.shape[1] * aspect_ratio))
resized = cv2.resize(src_cat, dsize, interpolation=cv2.INTER_AREA)
print_image_info(resized)
img_show('Resized (height)', resized)
print('-------------------------------')

resized = imutils.resize(src_cat, width=100)
print_image_info(resized)
img_show('Resized cia imutils', resized)

methods = [
  ('cv2.INTER_NEAREST', cv2.INTER_NEAREST),
  ('cv2.INTER_LINEAR', cv2.INTER_LINEAR),
  ('cv2.INTER_AREA', cv2.INTER_AREA),
  ('cv2.INTER_CUBIC', cv2.INTER_CUBIC),
  ('cv2.INTER_LANCZOS4', cv2.INTER_LANCZOS4)
]

image_label = []
image_list = []

for (name, method) in methods:
  image_label.append(name)

  resized = imutils.resize(
    src_cat,
    width=src_cat.shape[1] * 3,
    inter=method
  )

  image_list.append(resized)

img_show(
  image_label,
  image_list,
  figsize=(16, 10)
)

cv2.waitKey(0)
cv2.destroyAllWindows()