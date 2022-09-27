import cv2 as cv
import numpy as np


def mask_setTo():
    src = cv.imread('lenna.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('mask_smile.bmp', cv.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('error')
        exit()

    src[mask > 0] = (0, 0, 255)

    cv.imshow('src', src)
    cv.imshow('mask', mask)
    cv.waitKey()
    cv.destroyAllWindows()


def mask_copyTo():
    src = cv.imread('airplane.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('mask_plane.bmp', cv.IMREAD_GRAYSCALE)
    dst = cv.imread('field.bmp', cv.IMREAD_COLOR)

    # 예외처리
    if src is None or mask is None or dst is None:
        print('error')
        exit()

    dst[mask > 0] = src[mask > 0]

    cv.imshow('src', src)
    cv.imshow('mask', mask)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


mask_copyTo()
