'''
V: 1~V번까지의 V개의 정점
E: 간선의 개수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(start, N):  # 시작 정점, 노드개수 입력
    q = []                  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(start)         # 시작점 인큐
    visited[start] = 1      # 시작점 방문표시
    
    # 큐가 비워질때까지(남은 정점이 있으면) 반복...
    while q:
        t = q.pop(0)
        # t에서 할일...
        print(t)
        for i in adjl[t]:       # t에 인접인 정점 i
            if visited[i] == 0: # 방문하지 않은 정점이면
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t] # 방문표시
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 무향 그래프

bfs(1, V)










