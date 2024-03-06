T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        if i in arr[0]:
            best1 = 0
            if arr[0][i] > best1:
                best1 = arr[0][i]
            if arr[0][i] < 0:
                break
            result += best1

        if i in arr[1]:
            best2 = 0
            if arr[1][i] > best2:
                best2 = arr[1][i]
            if arr[1][i] < 0:
                break
            result += best2

        if i in arr[2]:
            best3 = 0
            if arr[2][i] > best3:
                best3 = arr[2][i]
            if arr[2][i] < 0:
                break
            result += best3

    print(f'#{tc} {result}')

