import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./images/ahah1.jpg')

def plotFigures(original_scr, blurred_scr, title):
  plt.figure(figsize=(10, 5))
  plt.subplot(121)
  plt.imshow(cv2.cvtColor(original_scr, cv2.COLOR_BGR2RGB))
  plt.title('Original')
  plt.xticks([])
  plt.yticks([])

  plt.subplot(122)
  plt.imshow(cv2.cvtColor(blurred_scr, cv2.COLOR_BGR2RGB))
  plt.title(title)
  plt.xticks([])
  plt.yticks([])

  plt.show()

blur = cv2.blur(src, (5, 5))
plotFigures(src, blur, 'cv2.blur()')

gaussian = cv2.GaussianBlur(src, (15, 15), 0)
plotFigures(src, gaussian, 'cv2.GaussianBlur()')