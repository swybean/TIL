T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'yes'
    stop = False
    cnt = 0

    for i in range(N):
        for j in range(N):
            if stop == False:
                if arr[i][j] == '#':
                    start = i, j
                    cnt = 1
                    for k in range(1, N):
                        ii = i+k
                        jj = j+k
                        if 0 <= ii < N and 0 <= jj < N and arr[ii][jj] == '#':
                            cnt += 1
                            stop = True
    i, j = start
    for p in range(i, i+cnt):
        for q in range(j, j+cnt):
            if arr[p][q] == '#':
                arr[p][q] = '.'
            else:
                ans = 'no'
                break
        if ans == 'no':
            break

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                ans = 'no'
                break

    print(f'#{test_case} {ans}')
    
    

