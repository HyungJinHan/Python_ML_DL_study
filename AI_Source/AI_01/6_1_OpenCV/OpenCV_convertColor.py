import cv2
from OpenCV_show_func import img_show

src = cv2.imread(
    './images/chess.jpg',
    cv2.IMREAD_COLOR
)

dst_GRAY = cv2.cvtColor(
    src,
    cv2.COLOR_BGR2GRAY
)

dst_RGB = cv2.cvtColor(
    src,
    cv2.COLOR_BGR2RGB
)

img_show(
    ['src', 'dst_GRAY', 'dst_RGB'],
    [src, dst_GRAY, dst_RGB],
    figsize=(12, 7)
)

# cv2.imshow('src', src)
# cv2.imshow('dst_GRAY', dst_GRAY)
# cv2.imshow('dst_RGB', dst_RGB)

print('src[0:5]\n', src[0:5])
print('\ndst_GRAY[0:5]\n', dst_GRAY[0:5])
print('\ndst_RGB[0:5]\n', dst_RGB[0:5])

print('\nsrc.shape\n', src.shape)
print('\ndst_GRAY.shape\n', dst_GRAY.shape)
print('\ndst_RGB.shape\n', dst_RGB.shape)

cv2.waitKey()
cv2.destroyAllWindows()