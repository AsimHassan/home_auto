import numpy as np 
import cv2
from cv2 import aruco
import time
import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
##cap = cv2.VideoCapture('IMG_2018.mov')
cap = cv2.VideoCapture('IMG_2032.mov')
parameters =  aruco.DetectorParameters_create()
i=0
frame_rate = 10
prev = 0
while(cap.isOpened()):
    time_elapsed = time.time() - prev

    ret, frame = cap.read()
    if time_elapsed > 1/frame_rate:
        prev = time.time()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,thresh2 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        ##cv2.imshow('ar1',thresh2)
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        cv2.imshow('ar',frame_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if(ids is not None):
            ids_list=ids.tolist()
            flat_list = []
            for sublist in ids_list :
                for item in sublist:
                    flat_list.append(item)
            flat_list.sort()
            print(flat_list)
            clientSock.sendto(bytearray(flat_list), (UDP_IP_ADDRESS, UDP_PORT_NO))
            print(i)
            i=i+1

cap.release()
cv2.destroyAllWindows()


