def selectionSort(arr, N):
    for i in range(N-1): # i 주어진 구간의 시작
        minidx = i # 구간의 최솟값 위치 minidx, 첫 원소를 최소로 가정
        for j in range(i+1, N): # 실제 최솟값 위치 검색
            if arr[minidx] > arr[j]:
                minidx = j       
        arr[minidx], arr[i] = arr[i], arr[minidx] # 최솟값을 구간의 맨 앞으로 이동 
    return

N = 5
arr = [1, 3, 2, 5, 4]

selectionSort(arr, N)
print(arr)