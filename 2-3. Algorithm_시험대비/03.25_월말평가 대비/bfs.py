# 인접 리스트 BFS : 재귀 버전
graph = [
    [1, 3],     
    [0, 2, 4],  
    [1],        
    [0, 4],    
    [1, 3],     
]

# bfs는 재귀가 아닌 함수 내에서 다 끝나기에 함수 안에서 만들어도된다.
visited = [0] * 5   

def bfs(start):
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:

            # 이미 방문을 했으면 pass
            if visited[to] == 1:
                continue
            
            # 갈 수 있는데 아직 방문하지 않았으면 방문 표시 + 큐에 추가
            visited[to] = 1

            # print(visited) # 방문을 잘했는지 보려면 visited 프린트 해보기
            queue.append(to)

bfs(0)  # 0 1 3 2 4

