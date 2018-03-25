import numpy as np
import cv2
import pprint
import math
import numpy as np
import cv2

import numpy as np
import cv2


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)
def newDimension(oldw, oldh):
    if oldw<oldh:
        rat = oldw/oldh
        return (500, int(500*rat))
    elif oldh>oldw:
        rat = oldh/oldw
        return (int(500*rat), 500)
    else:
        return (500,500)
print("start")
goodpic = cv2.imread('pictures/pill6.jpg', 0)
height = len(goodpic)
width = len(goodpic[0])
goodpic = cv2.resize(goodpic, newDimension(height, width))
height = len(goodpic)
width = len(goodpic[0])
print((height,width))
norm_image = goodpic
norm_image = cv2.normalize(goodpic, norm_image, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

for i in range(height):
    for j in range(width):
        norm_image[i][j] *= 1.25
        norm_image[i][j] += 20


img2 = cv2.resize(norm_image, (0,0), fx=1, fy=1)
average = np.mean(img2, axis=(0,1))
print(average)
max_black = int(-0.265 * average + 185)
print(max_black)
ret,img2 = cv2.threshold(img2,max_black,255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
print(type(kernel[0][0]))
erosion = img2
#erosion = cv2.dilate(img2,kernel,iterations = 1)
erosion = cv2.erode(img2,kernel,iterations = 2)


cv2.imshow("1", erosion)
cv2.imwrite('jv.jpg', erosion)

cv2.waitKey(0)
print("end")