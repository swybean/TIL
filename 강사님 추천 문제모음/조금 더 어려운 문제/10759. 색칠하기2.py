di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    counts = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1 or arr[i][j] == 2:  
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        if arr[ni][nj] != arr[i][j]:  
                            counts += 1
                    else:                             
                        counts += 1
 
    print(f'#{tc} {counts}')

