# 상하좌우 4방향 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())    # t 입력
for tc in range(1, T+1):
    N = int(input())    # 과녁 크기 N입력
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차원 리스트로 과녁판 만들기

    result_bonus = 0    # 얻을 수 있는 보너스 점수의 최댓값 변수

    # i행, j열을 순회하면서 정중앙으로 삼을 칸을 고른다.
    for i in range(N):
        for j in range(N):
            bonus = arr[i][j]   # 현재 보너스 점수 변수, 정중앙으로 설정한 칸의 점수 추가
            for p in range(1, 3):   # 정중앙 기준으로 상하좌우 2칸씩 가기 위한 범위 p설정 (1, 2)
                for k in range(4):  # 상하좌우 4방향을 탐색
                    ni = i + di[k]*p    # 상하좌우 4방향으로 p값 만큼 간다
                    nj = j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:    # 해당 칸이 과녁 안에 있어서 점수가 있다면
                        bonus += arr[ni][nj]    # 현재 보너스 점수에 해당 칸의 점수를 더한다

            if result_bonus < bonus:    # 만약 현재 보너스 점수가 보너스 점수의 최댓값보다 크다면
                result_bonus = bonus    # 보너스 점수의 최댓값을 현재 보너스 점수로 바꿔준다.

    print(f'#{tc} {result_bonus}')  # 정답 출력


