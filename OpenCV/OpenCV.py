import cv2 as cv
import numpy as np

# opencv version 확인
def printVersion():
    print(cv.__version__)
# printVersion()


# 이미지 타입 확인하기
def checkImageType():
    img1 = cv.imread('bmpTest.bmp')

    if img1 is None:
        print("error")
        return

    print('type of img1 : ', type(img1))
    print('img1.shape : ', img1.shape)

    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a color image')

    cv.imshow('img1', img1)
    cv.waitKey()
    cv.destroyAllWindows()
# checkImageType()

# 단위 행렬 출력
def printIdentity():
    arr = np.identity(3)
    print(arr)
# printIdentity()


# 행렬 초기화
def initMatrix():
    img1 = np.empty((480, 640), np.uint8)
    img2 = np.zeros((480, 640, 3), np.uint8)
    img3 = np.ones((480, 640), np.int32)
    img4 = np.full((480, 640), 0, np.float32)

    mat1 = np.array([[11,12,13,14],
                     [21,22,23,24],
                     [31,32,33,34]]).astype(np.uint8)

    print(mat1)
    mat1[0, 1] = 100
    mat1[2,:] = 200
    print(mat1)
# initMatrix()


def copyMatrix():
    img1 = cv.imread('bmpTest.bmp', cv.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()
    img2 += 20

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()
# copyMatrix()

