import numpy as np 
import cv2,PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl 
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
frame = cv2.imread("tmulti.png",1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thr3",th3)
cv2.waitKey(0)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(th3, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
cv2.imshow('ar',frame_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(ids)