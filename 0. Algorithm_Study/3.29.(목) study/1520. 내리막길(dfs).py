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

# dfs 함수 제작
def dfs(i, j):  # 시작위치 (i, j) 입력
    global result

    # 시작위치 방문표시
    visited[i][j] = 1

    # 기저조건
    # 만약 끝에 도달했다면 도달 가능한 경로(result)에 +1 해주기
    if i == M - 1 and j == N - 1:
        result += 1
        return 

    # 재귀호출
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 범위 내에 있고 다음 위치가 현재 위치보다 작다면 이동
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
            # 이동한 위치 좌표에서 dfs 재귀
            dfs(ni, nj)
            
M, N = map(int, input().split())    # M은 세로(행), N은 가로(열)
arr = [list(map(int, input().split())) for _ in range(M)]

result = 0  # 경로의 개수 구할 변수

visited = [[0] * N for _ in range(M)]   # 방문표시 리스트 만들기

dfs(0, 0)   # 0, 0에서 시작하게 dfs 시작

print(result)


