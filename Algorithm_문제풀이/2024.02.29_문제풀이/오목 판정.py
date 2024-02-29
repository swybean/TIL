
def omok(y, x):
    dy = [1, 0, 1, -1]  # 아래, 오른쪽, 4시방향 대각선, 2시방향 대각선
    dx = [0, 1, 1, 1]

    # 4방향 탐색
    for bang in range(4):
        cnt = 1 # 기준 좌표에 돌이있다. cnt = 1부터 시작
        # 돌 4개를 탐색
        for power in range(1, 5):
            ny = y + (dy[bang] * power)
            nx = x + (dx[bang] * power)
            if not (0 < ny <= N and 0 < nx <= N):
                break

            if arr[ny][nx] == 'o':
                cnt += 1

            if cnt == 5:    # 오목이다.
                return True
    return False # 오목을 발견못하면 False

def game_start():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                if omok(r, c):
                    return 'YES'
    return 'NO'

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = game_start()
    print(f'#{test_case} {result}')



