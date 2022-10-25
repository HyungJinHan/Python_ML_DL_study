import cv2
import matplotlib.pyplot as plt

def img_show(title='image', img=None, figsize=(8, 5)):
  plt.figure(figsize=figsize)

  if type(img) == list:
    if type(title) == list:
      titles = title
    else:
      titles = []

      for i in range(len(img)):
        titles.append(title)

    for i in range(len(img)):
      # 흑백을 RGB로, BGR을 RGB로 변경하는 작업
      if len(img[i].shape) <= 2:
        rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
      else:
        rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

      # plt.subplot(
      #   1,
      #   len(img),
      #   i + 1,
      # )

      plt.subplot(
        1,
        len(img),
        i + 1
      )

      plt.imshow(rgbImg)
      plt.title(title[i])
      plt.xticks([])
      plt.yticks([])

    plt.show()
  
  else:
    # 흑백을 RGB로, BGR을 RGB로 변경하는 작업
    if len(img.shape) < 3:
      rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
      rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(rgbImg)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()