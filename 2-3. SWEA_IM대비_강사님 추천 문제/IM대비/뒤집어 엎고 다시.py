T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    count = 0
    ans = 'yes'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                count += 1
                for k in range(1, N):
                    di = i + k
                    dj = j + k
                    if 0 <= di < N and 0 <= dj < N:
                        if arr[di][dj] == '#':
                            count += 1
                        else:
                            break
        
            








