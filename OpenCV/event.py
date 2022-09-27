import cv2 as cv
import numpy as np



# 키보드 이벤트 처리
img = cv.imread("bmpTest.bmp")
if img is None:
    print("error")
    exit()

cv.namedWindow('img')
cv.imshow('img', img)

while True:
    keyCode = cv.waitKey()
    if keyCode == ord('i'):
        img = ~img
        cv.imshow("img", img)
    elif keyCode == 27 or keyCode == ord('q'):
        break
cv.destroyAllWindows()


# 마우스 이벤트 처리
def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv.EVENT_LBUTTONDOWN:
        oldx, oldy, = x, y
        print('EVENT_LBUTTONDOWN %d %d' % (x, y))

    elif event == cv.EVENT_LBUTTONUP:
        oldx, oldy, = x, y
        print('EVENT_LBUTTONUP %d %d' % (x, y))

    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            cv.line(img, (oldx, oldy), (x, y), (0, 255, 255), 2)
            cv.imshow('img', img)
            oldx, oldy = x, y

img = cv.imread("bmpTest.bmp")

if img is None:
    print('error')
    exit()

cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse) # 운영체제에서 자동으로 on_mouse 호출해줌

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
