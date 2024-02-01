def binary_search(arr, N, key):
    start = 0   # 구간 초기화
    end = N - 1
    while start <= end:     # 검색 구간이 유효(s <= e)하면 반복해라
        middle = (start + end) // 2     # 중앙원소 인덱스
        if arr[middle] == key:    # 중앙값이 key랑 같으면 : 검색성공
            return middle
        elif arr[middle] > key:   # 중앙값이 key보다 크면
            end = middle - 1      
        else:                     # 중앙값이 key보다 작으면
            start = middle + 1
    return -1    # 검색실패