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
print(arr[::2])  # start : stop : step
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
print(arr[0, 2])
print(arr[0][2])
print(arr[0,])
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
print()

# 0차원 배열
arr = np.array(3)
print(arr)
print(arr.ndim)
print(arr.shape)
print()

# 3차원 배열
arr = np.array([
    [[1, 4, 2], [7, 5, 3]],
    [[0, 4, 8], [6, 9, 1]],
    [[7, 6, 9], [4, 0, 8]]
])
print(arr)
print(arr.ndim)
print(arr.shape)
print()

# 슬라이싱 결과는 배열의 주소가 전달되듯이 참조값이 할당됨
arr = np.array([1, 4, 2, 5, 3])
ref = arr[1:4]
cpy = arr[1:4].copy()
print(ref)
print(cpy)
arr[2] = 10
print(ref)
print(cpy)
print()

# NumPy 내장 함수를 이용한 배열 생성
print(np.zeros((2, 2)))
print(np.ones((2, 2)))
print(np.full((2, 2), 7))
print()

# NumPy 내장 함수를 이용한 행렬 관련 배열 생성
print(np.identity(3))
print(np.eye(3, k=2))
print(np.eye(3, k=-1))
print()

# NumPy 내장 함수를 이용한 배열 생성
print(np.random.random((2, 2)))
print(np.linspace(1, 10, num=10, endpoint=False, retstep=True))
print(np.arange(1, 10, dtype=int))

# NumPy 배열 변환
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr.reshape(3, 3))
print()

# swapaxes
arr = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
print(arr)
arr = arr.reshape(2, 4)
print(arr)
print()
print(arr.swapaxes(0, 1))
print()
print(arr.transpose(0, 1))
print()

# 2차원 배열 초기화
arr = np.arange(16).reshape((4, 4))
print(arr)
print(np.split(arr, [2]))
print()

# 유니버셜 함수
arr = np.arange(16).reshape((4, 4))
print(arr+10)
print()

arr = np.array([[3,3,3,3], [2,2,2,2]])
print(arr)
print(arr.shape)


