T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    best = -2000000000
    mini = 2000000000

    for i in range(N-1):
        if arr[i] + arr[i+1] > best:
            best = arr[i] + arr[i+1]
        if arr[i] + arr[i+1] < mini:
            mini = arr[i] + arr[i+1]

    print(f'#{tc} {best} {mini}')


