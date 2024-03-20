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
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    visited[i][j] += 1
                
                if arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    queue.append(ni, nj)
                    visited[ni][nj] += 1


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