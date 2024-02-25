
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =list(map(int, input().split()))

    max_num = 0
    min_num = 0

    for i in range(N):
        if arr[max_num] <= arr[i]:
            max_num = i
        if arr[min_num] > arr[i]:
            min_num = i
        
        result = abs(max_num - min_num)
    
    print(f'#{tc} {result}')