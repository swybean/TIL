


T = int(input())
 
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range (N)]
 
 
    max = 0
 
    for i in range(N):
        for j in range(N):
            sum = 0
            for m1 in range(M):
                for m2 in range(M):
                    ni = i + m1
                    nj = j + m2
                    if 0<= ni < N and 0<= nj <N:
                        sum+= arr[ni][nj]
 
            if sum > max:
                max = sum
 
    print(f'#{tc} {max}')








