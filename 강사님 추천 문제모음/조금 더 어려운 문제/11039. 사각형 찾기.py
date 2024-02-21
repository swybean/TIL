di = [0, 1]
dj = [1, 0]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result =0 
    for i in range(N):
        for j in range(N):
            garo_sum = 0
            sero_sum = 0
            gs_sum = 0
            if arr[i][j] == 1:
                garo_sum += 1
                sero_sum += 1

                for p in range(1, N):
                    for k in range(1):
                        ni = i + di[k]*p
                        nj = j + dj[k]*p
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                            garo_sum += 1
                            if arr[ni][nj] == 0:
                                break

                for p in range(1, N):
                    for k in range(1, 2):
                        ni = i + di[k]*p
                        nj = j + dj[k]*p
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                            sero_sum += 1 
                            gs_sum = garo_sum * sero_sum
                            if arr[ni][nj] == 0:
                                break

                if result < gs_sum:
                    result = gs_sum

    print(f'#{test_case} {result}')

                






                






