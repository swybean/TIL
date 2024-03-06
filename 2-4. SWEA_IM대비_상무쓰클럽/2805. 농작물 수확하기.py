

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    mid = N // 2  # 가장 중앙값의 인덱스
    carrot = 0

    for i in range(N):
        for j in range(N):
            if i == mid and j == mid:   # arr[mid][mid]인 곳을 구하기
                carrot += arr[i][j]

                # 중심점 기준으로 상하좌우만 쭉 더하기
                for p in range(1, N):
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni = i + di * p
                        nj = j + dj * p
                        if 0 <= ni < N and 0 <= nj < N:
                            carrot += arr[ni][nj]

    # 미드 기준 좌우로 한칸씩 가면서 해당칸에서 상하로 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == arr[mid][mid]:
                for k in range(1, mid):
                    
    
    
    
    
    
    # for number in range(1, N):
    #     if arr[ni][nj] == arr[mid][mid+number]:
    #         for q in range(1, N):








