
# import 하기
from collections import deque

# 4방향 좌표(상, 하, 좌, 우)

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

# 함수 제작
def bfs(x, y): 
    # 큐 생성
    queue = deque()
    # 시작위치에 큐 추가
    queue.append((x, y))
    # 방문한 좌표를 기록하는 리스트 만들기
    visited = [[False] * N for _ in range(N)]
    # 시작 위치 방문 표시해
    visited[x][y] = True

    # 큐가 빌 때까지 반복
    while queue: 
        # 큐 맨 앞에서 (x, y) 좌표를 꺼내오기
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 다음 위치에서 벽을 만나면 무시
            if arr[nx][ny] == 1:
                continue

            # 통로(0)면 움직여
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = True
                # 통로을 가고 있는데, 3이 없이 통로가 끝난 경우라면 추가하기

            elif arr[nx][ny] == 3:
                return 1
            else:
                return 0
    return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
                break
    
    print(f'#{test_case} {bfs(x, y)}')




