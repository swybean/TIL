# import 하기
from collections import deque

# 4방향 좌표(상, 하, 좌, 우)
# 좌표우표상표하표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 함수 제작
# 함수 제작해야 되냐고~
def bfs(x, y): 
    # 큐 생성
    # 큐 생성해야 되냐고~
    queue = deque()
    # 시작위치를 큐에 추가
    # 큐에 추가해야 되냐고~
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    # 반복해야되냐고~
    while queue: 
        # 큐 맨 앞에서 (x, y) 좌표를 꺼내오기
        # 꺼내와서 뭐할꺼임?
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        # 위치 확인 해서 뭐할껀데!
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위 벗어나면 무시
            # 무시하면 정 없잖아
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 벽(1)을 만나면 무시
            # 그만 무시하라고!!!!
            if arr[nx][ny] == 1:
                continue

            # 벽이 아닌 갈 수 있는 길(0)이라면
            if arr[nx][ny] == 0:
                # 해당 위치까지 최단 거리 기록
                arr[nx][ny] = arr[x][y] + 1
                # 큐에 추가
                queue.append((nx, ny))

            # 도착점(3)에 도착하면 최단거리 반환
            if nx == end_x and ny == end_y:
                return arr[x][y] - 2    # 시작점이 2였으니까 -2하기
            
    # 도착점(3)에 갈 수 있는 경로가 없으면
    # 경로가 없으면 경로를 만들자
    return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x, start_y = i, j
            if arr[i][j] == 3:
                end_x, end_y = i, j

    print(f'#{test_case}', bfs(start_x, start_y))
    

