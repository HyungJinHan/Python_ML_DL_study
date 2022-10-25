import cv2
from OpenCV_show_func import img_show
import numpy as np

src_song = cv2.imread(
  './images/song_1.jpg',
  cv2.IMREAD_COLOR
)

height, width, channel = src_song.shape

dst_pyrUp_song = cv2.pyrUp(
  src_song,
  dstsize=(width * 2, height * 2),
  borderType=cv2.BORDER_DEFAULT
)
dst_pyrDown_song = cv2.pyrDown(src_song)

cv2.imshow('src_song', src_song)
cv2.imshow('pyrUp_song', dst_pyrUp_song)
cv2.imshow('pyrDown_song', dst_pyrDown_song)

# ------------------------------------------------

src_cat = cv2.imread(
  './images/cat.jpg',
  cv2.IMREAD_COLOR
)

dst_pyrUp_cat = cv2.pyrUp(src_cat) # img * 4
dst_pyrDown_cat = cv2.pyrDown(src_cat) # img / 4

cv2.imshow('src_cat', src_cat)
cv2.imshow('pyrUp_cat', dst_pyrUp_cat)
cv2.imshow('pyrDown_cat', dst_pyrDown_cat)

cv2.waitKey(0)
cv2.destroyAllWindows()