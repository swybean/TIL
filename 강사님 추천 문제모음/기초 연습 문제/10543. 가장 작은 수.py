T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    INF = 1e9
    min_num = INF

    for i in range(len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
    
    for k in range(len(arr)):
        if arr[k] == min_num:
            print(f'#{tc}', k+1)
            break
