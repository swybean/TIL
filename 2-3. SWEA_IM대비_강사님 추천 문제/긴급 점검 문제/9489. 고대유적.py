# 오른쪽, 아래로만 가는 방향
di = [0, 1]
dj = [1, 0]

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    longest = 0  # 제일 긴 유적의 길이

    # arr을 순회해볼까
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # arr[i][j]가 1이라고?
                for k in range(2):  # 그럼 아래방향, 오른쪽 방향으로만 탐색해보자
                    gili = 1    # gili = 현재탐색하는 유적의 길이
                                # 1을 찾은 순간 해당 유적의 길이는 최소 1이니까 현재 유적의 길이를 1로 설정
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1: # 범위 내에 있으면서, 다음 칸도 1이라면 반복하자
                        gili += 1   # 길이에 1을 더해!
                        ni = ni + di[k] # 한 칸을 더 나아가볼까
                        nj = nj + dj[k] 
                        

                    if longest < gili:  # 현재 유적 길이가 longest보다 길다면
                        longest = gili  # longest를 현재 유적 길이로 바꿔
                    
    print(f'#{test_case} {longest}')
