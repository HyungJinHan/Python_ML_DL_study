import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./images/ahah.jpeg', cv2.IMREAD_GRAYSCALE)
_, t_80 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, t_100 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
_, t_150 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# THRESH_OTSU
# 임계 값을 임의로 정해 픽셀을 두 부류로 나누고
# 두 부류의 명암 분포를 구하는 작업을 반복함
# 모든 경우의 수 중에서 두 부류의 명암 분포가 가장 균일할 때의 임계 값을 선택함

print('otsu threshold :', t)

imgs = {
    'Original': img,
    't_80': t_80,
    't_100': t_100,
    't_130': t_130,
    't_150': t_150,
    'otsu : %d' %t: t_otsu
}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()