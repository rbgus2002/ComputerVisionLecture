import cv2 as cv
import numpy as np

'''
TickMeter 클래스를 통한 특정 연산의 수행 시간 측정
'''


def time_inverse():
    src = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('error')
        exit()

    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv.TickMeter()
    tm.start()


    # == ~srcz
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y, x]

    tm.stop()
    print('image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


time_inverse()
