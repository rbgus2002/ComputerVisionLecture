import numpy as np

# print NumPy Version
print(np.__version__)
print()

# NumPy 배열 생성
arr = [1, 4, 2, 5, 3]
numpyArr = np.array(arr)
print(arr)
print(type(arr))
print(numpyArr)
print(type(numpyArr))
print()

# NumPy 배열의 특징
'''
Element의 type이 일치하지 않는 경우, 상위 타입으로 형변환 시킴
'''
arr = [3.14, 2, 5, 3]
numpyArr = np.array(arr)
print(arr)
print(type(arr))
print(numpyArr)
print(type(numpyArr))
print()

# Element의 type이 일치하지 않는 경우의 예시
'''
String이 상위 타입이네
'''
arr = ['3.14', 2., 5, 3]
numpyArr = np.array(arr)
print(arr)
print(type(arr))
print(numpyArr)
print(type(numpyArr))
print()

# 명시적으로 Element 타입 설정 1
arr = [1, 4, 2, 5, 3]
numpyArr = np.array(arr, dtype='float_')
print(arr)
print(type(arr))
print(numpyArr)
print(type(numpyArr))
print()

# 명시적으로 Element 타입 설정 2 (String이 float32로 변환 불가능하면 컴파일 에러 띄움)
arr = ['3.14', 4., 2, 5, 3]
numpyArr = np.array(arr, dtype='float32')
print(arr)
print(type(arr))
print(numpyArr)
print(type(numpyArr))
print()

# NumPy 배열의 속성
'''
ndim -> 차원
shape -> 배열의 모양 (2차원 배열이면 튜플형식으로 1차원에 몇 개, 2차원에 몇 개라고 알려줌)
len(arr.shape) 하면 ndim이랑 같음
size -> 배열의 크기를 세줌. len으로하면 2차원 이상 배열의 경우 원하는 값이 안나올 수 있으므로 .size 사용하기
'''
arr = np.array([1, 4, 2, 5, 3])
print(arr)
print(arr.ndim)
print(arr.shape)
print(len(arr.shape))
print(arr.size)
print()

# NumPy 배열의 값 접근
arr = np.array([1, 4, 2, 5, 3])
print(arr[1])
print(arr[:3])
print(arr[2:4])
print(arr[::2]) # start : stop : step
print()



# NumPy 2차원 배열
arr = np.array([[1, 4, 2], [7, 5, 3]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(len(arr.shape))
print(arr.size)
print()



# NumPy 2차원 배열 값 접근
arr = np.array([[1, 4, 2], [7, 5, 3]])
print(arr[0,2])
print(arr[0][2])
print(arr[0, ])
print(arr[0, :])
print(arr[:, 1:2])
print(arr[0:2, 1:2])
print(arr[1, 1:])
print(arr[:, 1:])
print()


# NumPy 2차원 배열 값 접근 유의사항
'''
슬라이싱 해서 얻는 값이랑 특정 인덱스 참조해서 얻는 값이랑 다름
슬라이싱 -> numpy arr 형태
특정 인덱스 참조 -> data 있는 그대로의 형태
'''
arr = np.array([[1, 4, 2], [7, 5, 3]])
print(arr[0:1, :])
print(arr[:1, ])
print(arr[0, :])
print()


# NumPy 2차원 배열 실습
arr = np.array([[1, 4, 2], [7, 5, 3]])
print(arr[1, 1])
print(arr[1][1])
print(arr[1:, 1])
print(arr[1:, 1:2])
print(arr[1, 0:2])
print(arr[1:, 0:2])
print(arr[:, 2])
print(arr[:, 2:])
print(arr[:, 0:2])


#


