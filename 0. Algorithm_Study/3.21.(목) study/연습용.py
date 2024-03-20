




def dfs(i, j, h):
    global visited
    visited[i][j] = True
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and area[ni][nj] > h:
            dfs(ni, nj, h)

N = int(input())  # 지역의 크기
area = [list(map(int, input().split())) for _ in range(N)]  # 지역의 높이 정보

di = [-1, 1, 0, 0]  # 상하좌우 이동
dj = [0, 0, -1, 1]

result = 0  # 결과값

# 높이별로 안전한 영역의 개수 구하기
for h in range(101):  # 높이는 1부터 100까지 가능
    visited = [[False] * N for _ in range(N)]  # 방문 여부 초기화
    safe_count = 0  # 안전한 영역 개수
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > h:
                dfs(i, j, h)
                safe_count += 1
    result = max(result, safe_count)  # 최대값 갱신

print(result)