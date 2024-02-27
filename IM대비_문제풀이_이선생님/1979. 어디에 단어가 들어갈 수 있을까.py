T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N은 가로&세로 길이, K는 단어의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차원 배열 입력
    # 2차원 배열 중 1인 부분은 단어 입력 가능 부분, 0인 부분은 단어 입력 불가능한 부분

    result = 0  # 단어 입력 가능한 칸의 수를 저장할 변수


    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
                if j == N-1:
                    if count == K:
                        result += 1
                        count = 0
                if j+1 < N:
                    if arr[i][j+1] == 0:
                        if count == K:
                            result += 1
                            count = 0

            elif arr[i][j] == 0: 
                if count == K:
                    result += 1
                count = 0

    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 0:
                if count == K:
                    result += 1
                count = 0

    print(f'#{test_case} {result}')





'''
답은 2, 6
나는 2, 5


'''