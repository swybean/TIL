'''
동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 
동빈이의 위치는 (1. 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다. 
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력 조건 
• 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다. 
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 
각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 
또한 시작 칸과 마지막 칸은 항상 1 이다.

출력 조건 
• 첫째 줄에 최소 이동 칸의 개수를 출력한다.

'''
# import 하기
from collections import deque

# 4방향 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 함수 제작
def bfs(x, y): 
    # 큐 생성
    queue = deque()
    # 시작위치에 큐 추가
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue: 
        # 큐 맨 앞에서 (x, y) 좌표를 꺼내오기
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 다음 위치에서 벽을 만나면 무시
            if arr[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우
            if arr[nx][ny] == 1:
                # 해당 위치까지 최단 거리 기록
                arr[nx][ny] = arr[x][y] + 1
                # 큐에 추가
                queue.append((nx, ny))
    # 출구에 도착하면 출구까지 최단거리 반환
    return arr[N - 1 ][M - 1]


# 미로 크기 및 출구 입력
N, M = map(int, input().split())


# 미로 생성
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

print(bfs(0, 0))





