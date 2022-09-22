import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)


# 다양한 그리기 함수
def drawLine():
    cv.line(img, (50, 50), (200, 50), (0, 0, 255))
    cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
    cv.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

    cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
    cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
    cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

    cv.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1, cv.LINE_8, 0, 0.5)

    cv.drawMarker(img, (50, 350), (0, 0, 255), cv.MARKER_TILTED_CROSS)

    cv.imshow('img', img)
    cv.waitKey()
    cv.destroyAllWindows()


def drawShape():
    cv.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
    cv.rectangle(img, (50, 150), (150, 200), (0, 0, 255), 2)

    cv.circle(img, (300, 120), 30, (255, 255, 0), -1, cv.LINE_AA)
    cv.circle(img, (300, 120), 60, (255, 0, 0), -1, cv.LINE_AA)

    cv.ellipse(img, (120, 300), (60, 30), 20, 0 ,270, (255, 255, 0), cv.FILLED, cv.LINE_AA)

    cv.imshow('img', img)
    cv.waitKey()
    cv.destroyAllWindows()

drawShape()

'''
img -> numpy array
line() -> 직선 그리기 함수, 인자로 LineTypes 존재
arrowedLine() -> 화살표 형태의 직선 그리기 함수
drawMarker() -> 마커 그리기 함수, 인자로 MarkerTypes 존재

'''
