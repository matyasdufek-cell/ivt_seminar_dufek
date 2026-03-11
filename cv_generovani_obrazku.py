import cv2 as cv
import numpy as np
from random import randint

img = np.zeros((300, 400, 3), dtype=np.uint8)
"""
hls_img = cv.cvtColor(img, cv.COLOR_BGR2HLS)
"""

"""
h = randint(25, 75)
l = randint(75, 150)
s = randint(75, 150)
"""

for i in range(30):
    for j in range(40):
        """
        hls_img[10*i:10*i+10, 10*j:10*j+10, 0] = [h, l, s]
        
        img[10*i:10*i+10, 10*j:10*j+10, 0] = randint(0, 255)
        img[10*i:10*i+10, 10*j:10*j+10, 1] = randint(0, 255)
        img[10*i:10*i+10, 10*j:10*j+10, 2] = randint(0, 255)
        """
        cv.circle(img, (10*j+5, 10*i+5), 5, (randint(0, 255), randint(0, 255), randint(0, 255)), thickness=-1)

for i in range(31):
    cv.line(img, (0, 10*i), (400, 10*i), (255, 255, 255))
    for j in range(41):
        cv.line(img, (10*j, 0), (10*j, 300), (255, 255, 255))

        

cv.imshow("pampalini", img)
cv.waitKey(0)
cv.destroyAllWindows()