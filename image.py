import cv2
import numpy as np
 
img = cv2.imread('cross_validation_data/50.ppm', 1)
eia=cv2.resize(img,(64,64))
hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)

lower_range = np.array([4,100,100])
upper_range = np.array([18,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
 
cv2.imshow('mask',mask)
cv2.imshow('image', img)
 
while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
 
cv2.destroyAllWindows()
