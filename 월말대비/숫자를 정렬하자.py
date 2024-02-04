# 버블정렬
T= int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


    print(f'#{test_case}', *arr)



# 선택정렬
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if arr[j] < arr[min_index]:
                min_index = j

        # 현재 위치(i)와 최소값을 가진 위치(min_index)의 원소 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'#{test_case}', *arr)