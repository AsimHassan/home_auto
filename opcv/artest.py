import numpy as np 
import cv2,PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl 


#aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
frame = cv2.imread("t3.jpg",1)
print(frame.shape)
scale_percent = 15 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('frame',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('t3_resize.jpg',resized)