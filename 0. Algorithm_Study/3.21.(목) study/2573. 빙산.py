from collections import deque

def bfs(x, y):
    queue = deque
    queue.append(x, y)
    visited[x][y] = 0

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위내에 있고 방문하지 않았으면
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                # 해당 위치가 빙산이면 방문표시 + 큐에 추가
                if arr[ni][nj] != 0:
                    visited[ni][nj] += 1
                    queue.append(ni, nj)
                
                # 해당 위치가 바닷물이라면
                if arr[ni][nj] == 0:
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        # 범위 내에 있고 상하좌우 칸이 빙산이라면
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                            arr[ni][nj] -= 1    # 빙산의 숫자를 -1 하기
                            


# 4방향 델타 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  

N, M = map(int, input().split())    # N은 행, M은 열

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]










'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

2
'''