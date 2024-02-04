T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0



    for i in range(N):
        if arr[min_idx] > arr[i]:
            min_idx = i

        if arr[max_idx] <= arr[i]:
            max_idx = i

    
    
    ans = max_idx - min_idx if max_idx > min_idx else min_idx - max_idx
    print(f'#{test_case} {ans}')


