T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]
    counts = 0  # 토글 1의 개수 변수

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, M+1):

                if i + j == k or (i + j) % k == 0:
                    if arr[i-1][j-1] == '0':
                        arr[i-1][j-1] = '1'

                    elif arr[i-1][j-1] == '1':
                        arr[i-1][j-1] = '0'

                elif M % k == 0:
                    if arr[i-1][j-1] == '0':
                        arr[i-1][j-1] = '1'

                    elif arr[i-1][j-1] == '1':
                        arr[i-1][j-1] = '0'
                    
                 
            if arr[i-1][j-1] == '1':      
                counts += 1                     
 
    print(f'#{tc} {counts}')    










