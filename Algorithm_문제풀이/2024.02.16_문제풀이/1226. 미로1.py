
from collections import deque
 
# 4방향 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 큐 생성
    queue = deque()
    # 시작위치를 큐에 추가
    queue.append((x, y))
 
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위 내에 있는지 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 벽이면 무시하고 지나가라
            if arr[nx][ny] == 1:
                continue

            # 통로면 거기로 가자
            if arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = 1

            # 도착점에 왔어? 1을 출력해
            if arr[nx][ny] == 3:
                return 1
            
    # 도착할 수 없어? 0을 출력해
    return 0
 


for test_case in range(10):
    case_num = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    start_x, start_y = 1, 1
 
    print(f'#{test_case+1} {bfs(start_x, start_y)}')






