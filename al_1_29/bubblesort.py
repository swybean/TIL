N = 6
arr = [7, 2, 5, 3, 1, 4]

def asc(arr, N):
    for i in range(N-1, 0, -1):   # 정렬할 구간의 마지막 인덱스
        for j in range(i):     # 비교할 두 원소 중 왼쪽의 인덱스
            if arr[j] > arr[j + 1]:   # 오름차순은 큰 수를 오른쪽으로
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # 자리를 바꿔라

def dec(arr, N):
    for i in range(N-1, 0, -1):   # 정렬할 구간의 마지막 인덱스
        for j in range(i):     # 비교할 두 원소 중 왼쪽의 인덱스
            if arr[j] < arr[j + 1]:   # 내림차순은 작은 수를 오른쪽으로
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # 자리를 바꿔라

asc(arr, N)
# dec(arr, N)  # 내림차순
print(arr)