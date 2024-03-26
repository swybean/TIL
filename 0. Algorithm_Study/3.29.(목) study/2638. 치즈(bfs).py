from collections import deque


# 4방향 설정
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

def bfs():
    global ans

    # 큐 생성
    q = deque()
    # 큐에 0,0 시작좌표 삽입
    q.append((0, 0))
    
    visited = [[0] * M for _ in range(N)]   # 방문표시 리스트 생성
    air = [[0] * M for _ in range(N)]   # 치즈랑 접한 공기가 몇개인지 세는 리스트

    # 큐가 빌 때까지 반복
    while q:

        # 0,0 좌표 꺼내오기
        i, j = q.popleft()

        # 상하좌우 탐색하기
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위를 벗어나지 않고 방문하지 않은 곳이라면
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if arr[ni][nj] == 0:    # 방문한 곳이 공기라면
                    q.append((ni, nj))  # 큐에 삽입
                    visited[ni][nj] = 1 # 방문 표시
                else:                   # 방문한 곳이 치즈라면
                    q.append((ni, nj))  # 큐에 삽입
                    air[ni][nj] += 1    # 접한 공기의 수 +1 해주기

    # 모든 곳의 탐색이 다 끝났으면 이제 공기 2개 이상이랑 접한 치즈 녹이기
    for i in range(N):
        for j in range(M):
            if air[i][j] >= 2:
                arr[i][j] = 0
                ans += 1
            
N, M = map(int, input().split())    # N은 세로(행), M은 가로(열)
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

bfs()

print(ans)