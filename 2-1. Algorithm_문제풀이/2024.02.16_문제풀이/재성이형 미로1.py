########## 미로 dfs

def dfs_maze(start, visited):   # 시작좌표값 start, 방문 노드까지 가는 칸 수 visited
    global flag 
    if flag:    # 출구 찾았으면 dfs 탐색 종료를 위해 리턴
        return

    visited[start[0]][start[1]] = True     # 시작 좌표에 방문했다고 표시
    di = [0, 1, 0, -1]      # 좌표 상하좌우로 변경하며 탐색
    dj = [1, 0, -1, 0]

    for _ in range(4):      # 상하좌우 4방향 탐색
        ni = start[0]+di[_]
        nj = start[1]+dj[_]
        if not (0 <= ni < N and 0 <= nj < N):   # 미로 벗어나는 경우는 빼고 반복
            continue
        if maze[ni][nj] == 3:                   # 출구를 찾은 경우 1을 설정
            flag = 1
        if maze[ni][nj] == 1:              # 벽에 막힌 경우 다른 좌표로
            continue
        if not visited[ni][nj] and maze[ni][nj] == 0:  # 통로도 있고 방문한 곳이 아니면
            dfs_maze([ni, nj], visited)     # dfs 재귀에 넣어서 더 깊게 탐색함 
    return flag     # 출구 못찾으면 그대로 0 리턴됨 

for _ in range(1, 11):
    tc = int(input())
    N = 16
    maze = []

    for i in range(N):
        temp_list = list(map(int, input()))
        for j in range(N):
            if temp_list[j] == 2:
                start = [i, j]
        maze += [temp_list]

    visited = [[False] * 16 for _ in range(16)]
    flag = 0    # 초기값으로 출구 못 찾으면 0, 찾으면 1
    print(f'#{tc}', dfs_maze(start, visited))


######## 미로 bfs
def bfs_maze(start, visited):   # 시작좌표값 start, 방문 노드까지 가는 칸 수 visited
    Q = []                  # 큐 생성
    Q += [start]            # 시작 좌표값 넣음
    visited[start[0]][start[1]] = True     # 시작 좌표에 방문했다고 표시
    di = [0, 1, 0, -1]      # 좌표 상하좌우로 변경하며 탐색
    dj = [1, 0, -1, 0]
 
    while Q:
        v = Q.pop(0)
        for _ in range(4):      # 상하좌우 4방향 탐색
            ni = v[0]+di[_]
            nj = v[1]+dj[_]
            if not (0 <= ni < N and 0 <= nj < N):   # 미로 벗어나는 경우는 빼고 반복
                continue
            if maze[ni][nj] == 3:                   # 출구를 찾은 경우 시작 좌표 방문값 1 빼고 리턴
                return 1
            if maze[ni][nj] == 1:                   # 벽에 막힌 경우 다른 좌표로
                continue
            elif not visited[ni][nj] and maze[ni][nj] == 0:  # 통로도 있고 방문한 곳이 아니면
                Q += [[ni, nj]]                             # 큐에 넣고 방문 칸 수 증가시킴
                visited[ni][nj] = True
    return 0
 
 
for _ in range(1, 11):
    tc = int(input())
    N = 16
    maze = []
 
    for i in range(N):
        temp_list = list(map(int, input()))
        for j in range(N):
            if temp_list[j] == 2:
                start = [i, j]
        maze += [temp_list]
 
    visited = [[False] * 16 for _ in range(16)]
    print(f'#{tc}', bfs_maze(start, visited))

