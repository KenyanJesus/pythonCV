from hello import ImageAnalysis
import cv2
import numpy as np

img = cv2.imread('jpeg.jpg')
image = ImageAnalysis()
result = image.returnResult(img)
print(result.circles)
print(result.qrcodes)
