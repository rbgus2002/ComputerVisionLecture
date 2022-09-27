import numpy as np
import cv2 as cv

'''
FileStorage -> 데이터 파일 입출력 기능을 캡슐화하여 지원

FileStorage 객체를 생성해서 데이터를 저장하거나 읽어 옴
'''


filename = 'mydata.json'

def writeData():
    name = 'Jane'
    age = 10
    pt1 = (100, 200)
    scores = (80, 90, 50)
    mat1 = np.array([[1.0, 1.5], [2.0, 3.2]], dtype=np.float32)

    fs = cv.FileStorage(filename, cv.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print("error")
        exit()

    fs.write('name', name)
    fs.write('age', age)
    fs.write('pt1', pt1)
    fs.write('scores', scores)
    fs.write('mat1', mat1)

    fs.release()

def readData():
    fs = cv.FileStorage(filename, cv.FILE_STORAGE_READ)

    if not fs.isOpened():
        print("error")
        exit()

    name = fs.getNode('name').string()
    age = int(fs.getNode('age').real())
    pt1 = tuple(fs.getNode('pt1').mat().astype(np.int32).flatten())
    scores = tuple(fs.getNode('scores').mat().flatten())
    mat1 = fs.getNode('mat1').mat()

    fs.release()

    print(name)
    print(age)
    print(pt1)
    print(scores)
    print('data:')
    print(mat1)

readData()