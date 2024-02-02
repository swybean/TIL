di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
 
def flower_sum(i,j, current, matrix):
    i_coord = []
    j_coord = []
 
    for l in range(1,current+1):
        i_coord += [[i+l*change for change in di]]
        j_coord += [[j+l*change for change in dj]]
 
    sum = 0
    for u in range(0, current):
        for dir in range(0, 4): # 북 서 남 동
            if 0 <= i_coord[u][dir] < N and 0 <= j_coord[u][dir] < M:
                sum = sum + matrix[i_coord[u][dir]][j_coord[u][dir]]
 
    sum = sum + current
    return sum
 
T = int(input())
 
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) #행, 열
 
    total_map = []
    for k in range(N): # 풍선 지도 제작
        total_map += [list(map(int, input().split()))]
 
    result = 0
    for i in range(N):
        for j in range(M):
            current = total_map[i][j]
            if flower_sum(i, j, current, total_map) > result:
                result = flower_sum(i, j, current, total_map)
     
    print(f"#{tc} {result}")