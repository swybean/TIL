from collections import deque

def bfs():
    





M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M))















'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

-1
'''



'''
글러먹은 내 첫 시도

# 4방향 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(N, M):
    global q

    while q:
        i, j = q.pop(0)
        if arr[i][j] == 1:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == 0:
                        q.append([ni, nj])
                        arr[ni][nj] = 1


        
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

q = []

# 초기 배열에서 익은 토마토(1)이 있는 좌표를 큐에 넣기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j])

print(bfs(N, M))

'''