'''
지도 세로는 M, 가로는 N
0 <= M, N <= 500
높이는 0 <= 높이 <= 10,000

시작점 : 제일 왼쪽 위 지점 / 0,0
도착점 : 제일 오른쪽 아래 지점 / M-1, N-1

항상 내리막길로만 이동 : 이동할 칸 < 현재 칸

이동경로의 개수를 구해라     


'''

# 4방향 설정
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]


def dfs(i, j):  # 시작위치 (i, j) 입력

    # 시작위치 방문표시
    visited[i][j] = 1
    now = arr[i][j]

    # 

    # 기저조건

    
    # 재귀호출
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
            cnt += 1











M, N = map(int, input().split())    # M은 세로(행), N은 가로(열)
arr = [list(map(int, input().split())) for _ in range(M)]


visited = [[0] * N for _ in range(M)]

print(visited)


