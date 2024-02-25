di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            for p in range(1, arr[i][j]+1):
                for k in range(4):
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0<=ni<N and 0<=nj<M:
                        flower += arr[ni][nj]
                if result < flower:
                    result = flower
    print(f'#{tc} {result}')

