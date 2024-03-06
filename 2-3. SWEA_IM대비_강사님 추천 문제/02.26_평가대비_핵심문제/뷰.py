
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    goodview = 0

    for i in range(2, N-2):
        high = 0
        for j in (-2, -1, 1, 2):
            if high < arr[i+j]:
                high = arr[i+j]
        
        if arr[i] > high:
            goodview += arr[i] - high
    
    print(f'#{tc} {goodview}')

