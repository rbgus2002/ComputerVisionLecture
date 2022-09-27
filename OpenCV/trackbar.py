import cv2 as cv
import numpy as np

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv.imshow('image', img)

img = np.zeros((400, 400), np.uint8)

cv.namedWindow('damm')
cv.createTrackbar('leveldamm', 'damm', 0, 16, on_level_change)

cv.imshow('damm', img)
cv.waitKey()
cv.destroyAllWindows()