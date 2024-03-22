# 상하좌우 4방향 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    hcount = 0  # 기지국으로 커버되지 않는 집의 수
    
    # 배열 arr의 모든 칸을 순회
    for i in range(N):      
        for j in range(N):
            # 만약 해당칸이 A기지국이라면
            if arr[i][j] == 'A':
                for k in range(4):  # 상하좌우 1칸씩 총 4칸을 확인
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'H':  # 해당칸이 집이라면
                            arr[ni][nj] = 'X'   # X로 변경

            # 만약 해당칸이 B기지국이라면
            elif arr[i][j] == 'B':
                for p in range(1, 3):   # 상하좌우 2칸씩 확인해야 한다.
                    for k in range(4):  # 상하좌우 2칸씩 총 8칸을 확인
                        ni = i + (di[k] * p)
                        nj = j + (dj[k] * p)
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':  # 해당칸이 집이라면
                                arr[ni][nj] = 'X'   # X로 변경

            # 만약 해당칸이 C기지국이라면
            elif arr[i][j] == 'C':
                for p in range(1, 4):   # 상화좌우 3칸씩 확인해야 한다.
                    for k in range(4):  # 상화좌우 3칸씩 총 12칸을 확인
                        ni = i + (di[k] * p)
                        nj = j + (dj[k] * p)
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':  # 해당칸이 집이라면
                                arr[ni][nj] = 'X'   # X로 변경

    # 전체를 다시 탐색해보자
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':    # 아직 남아있는 집(H)가 있다면
                hcount += 1         # hcount를 +1 해라

    print(f'#{test_case} {hcount}') # 정답 출력
