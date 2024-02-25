di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            fly1 = arr[i][j]
            fly2 = arr[i][j]

            for p in range(1, M):
                for di, dj in [[1, 0],[0, 1],[0, -1],[-1, 0]]:
                    ni = i + di*p
                    nj = j + dj*p
                    if 0 <= ni < N and 0 <= nj < N:
                        fly1 += arr[ni][nj] 

            for p in range(1, M):
                for di, dj in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    ni = i + di*p
                    nj = j + dj*p

                    if 0 <= ni < N and 0 <= nj < N:
                        fly2 += arr[ni][nj] 
            
            if result < fly1:
                result = fly1
            if result < fly2:
                result = fly2

    print(f'#{tc} {result}')


