
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    doll_arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        for p in range(1, j+1):                       
            if 0 <= i-1-p < N and 0 <= i-1+p < N:      
                if doll_arr[i-1-p] == doll_arr[i-1+p]:  
                    doll_arr[i-1-p] = (doll_arr[i-1-p] + 1) % 2
                    doll_arr[i-1+p] = (doll_arr[i-1+p] + 1) % 2

    print(f'#{test_case}', *doll_arr)
