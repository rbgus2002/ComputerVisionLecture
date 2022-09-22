import cv2 as cv
import numpy as np

def camera_in():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        return

    print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print('Frame num : ', int(cap.get(cv.CAP_PROP_FPS)))

    while True:
        ret, frame = cap.read()     # read() : 동영상으로부터 프레임 받아옴


        if not ret:
            break

        inversed = ~frame

        cv.imshow('frame', frame)
        cv.imshow('inversed', inversed)

        if cv.waitKey(10) == 27:
            break

    cv.destroyAllWindows()

# camera_in()

'''
동영상 파일 -> 초당 프레임 수 가지고 있음 == cv.CAP_PROP_FPS
'''


cap = cv.VideoCapture('video.mp4')

if not cap.isOpened():
    print('error')
    exit()

print('Frame Count', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print(fps)
delay = round(1000 / fps)

while True:
    ret, frame = cap.read()  # read() : 동영상으로부터 프레임 받아옴

    if not ret:
        break

    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
