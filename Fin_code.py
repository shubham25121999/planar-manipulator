import cv2
import numpy as np
import time
import serial
from math import *
import struct

port = 'COM17'
a=20
l = 52 *a
b = 30*a
ser = serial.Serial(port, baudrate=9600, timeout=1)

counter = 1
i=0
angles = np.zeros([3,1])

img = np.zeros((b,l, 3), np.uint8)
img[-int(9.8*a):,:]=[0,255,255]
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"PLANAR MANIPULATOR",(337,(30*a)-int(8.0*a)),font,1,(0,0,255),2)
img = cv2.putText(img,"ROBOTICS CLUB IITG",(347,(30*a)-int(5.5*a)),font,1,(0,0,255),2)
img = cv2.putText(img,"<Press Enter when done>",(300,(30*a)-int(3.0*a)),font,1,(0,0,255),2)
img= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,0])
cv2.imshow('image', img)


drawing = False  # if True, drawing is started
print(">> Press Enter when done  \n")


def process(x, y):
    global angles,i
    r = int(sqrt(x**2 + y**2))
    if x == 0:
        theta_one = 0
    else:
        theta_not = atan(y/x)
        theta_one = (pi - theta_not)*(180/pi) if x>0 else (theta_not) * (180 / pi)
    alpha = acos((2000-((r-10)**2))/1600)
    theta_two = (alpha*(180/pi))-90
    beta = acos((((r-10)**2)-1200)/(40*(r-10)))
    theta_three = (beta * (180/pi))+90
    y = np.zeros([3, 1], np.uint8)
    y[0, 0] = int(theta_one)
    y[1, 0] = int(theta_two)
    y[2, 0] = int(theta_three)
    angles = np.append(angles, y, axis=1)
    i = i + 1


def get_coordinates(event, x, y, flags, param):
        global drawing, points, i
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True

            x_temp = (x-(l/2))/a
            y_temp = ((b-y)/a)+35

            cv2.circle(img, (x, y), 3, (0, 255,0), -1)
            cv2.imshow('image', img)
            process(x_temp, y_temp)
            print(x,y,x_temp,y_temp)

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                x_temp = (x - (l / 2)) / a
                y_temp = ((b - y) / a) + 35
                process(x_temp, y_temp)

                cv2.circle(img, (x, y), 3, (0, 255,0), -1)
                cv2.imshow('image', img)

                print(x,y,x_temp,y_temp)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False




cv2.setMouseCallback('image', get_coordinates)
"""while(1):
    k=cv2.waitKey(0)
    if k==27:
        break"""
while (1):
    k = cv2.waitKey(0)

    if k==27:
        break

    if k == ord('p'):
        print("Sending Data...")

        for j in range(1,i):
            #if j%5 == 0:
                print("sending data...")
                ser.write(struct.pack('>B',255))
                ser.write(struct.pack('>B',int(angles[0,j])))
                ser.write(struct.pack('>B',int(angles[1,j])))
                ser.write(struct.pack('>B',int(angles[2,j])))

                time.sleep(3)

cv2.destroyAllWindows()

