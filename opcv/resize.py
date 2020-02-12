import numpy as np 
import cv2,PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl 

frame = cv2.imread('t3', cv2.IMREAD_UNCHANGED)
 
print(frame.shape)
 
scale_percent = 50 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()