import cv2
import numpy as np


def SatelliteCount():
    frame = cv2.imread('Satellite_View.png')
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    count=np.count_nonzero(green)
    print('count:', count)
    cv2.imshow("Green", green)
    cv2.imwrite("filter_image.png",green)
    cv2.waitKey()

def MapCount():
    frame = cv2.imread('Satellite_View.png')
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Green color
    low_green = np.array([25, 12, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    count=np.count_nonzero(green)
    print('count:', count)
    cv2.imshow("Green", green)
    cv2.imwrite("filter_image.png",green)
    cv2.waitKey()
