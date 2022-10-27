import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./images/cat.jpg', cv2.IMREAD_GRAYSCALE)
_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

imgs = {
    'Original': img,
    'BINARY': t_bin,
    'BINARY_INV': t_bininv,
    'TRUNC': t_trunc,
    'TOZERO': t_2zr
}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()