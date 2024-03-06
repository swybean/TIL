

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))+ [0] for _ in range(N)] + [[0]*(N+1)]

    N += 1
    ans = 0

    for i in range(N):
        counts = 0
        for j in range(N):
            if arr[i][j]:
                counts += 1
            else:
                if counts == K:
                    ans += 1
                counts = 0
        
    for j in range(N):
        counts = 0
        for i in range(N):
            if arr[i][j]:
                counts += 1
            else:
                if counts == K:
                    ans += 1
                counts = 0

    print(f'#{tc} {ans}')





