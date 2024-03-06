di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    dir = 0
    number = 1
    arr[0][0] = 1

    while number < N * N:
        ni = i + di[dir]
        nj = j + dj[dir]

        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            dir = (dir+1) % 4
            ni = i + di[dir]
            nj = j + dj[dir]

        i = ni
        j = nj
        number += 1
        arr[ni][nj] = number
    
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])





