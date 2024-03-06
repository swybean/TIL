di = [0, 1, 0, -1, -1, 1, 1, -1]
dj = [1, 0, -1, 0, 1, 1, -1, -1]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Huboji = 0

    for i in range(N):
        for j in range(M):
            photo_ok = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        photo_ok += 1
            if photo_ok >= 4:
                Huboji += 1

    print(f'#{test_case} {Huboji}')