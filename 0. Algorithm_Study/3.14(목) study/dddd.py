from collections import deque

n, k = map(int, input().split())

graph = []                          # 전체 보드 정보를 담는 리스트
data = []                           # 바이러스에 대한 정보를 담는 리스트


for i in range(n):                  # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):                  # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))





print(graph)    # [[1, 0, 2], [0, 0, 0], [3, 0, 0]]



