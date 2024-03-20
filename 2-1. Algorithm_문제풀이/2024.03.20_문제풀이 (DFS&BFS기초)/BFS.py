# BFS 특징
# 갈 수 있는 곳 다 가기
# 방문 순서대로 다음 노드 먼저 방문 -> 먼저 다음 노드
# FIFO -> queue 사용

# 방법1. list queue
# 방법2. deque queue (내부적으로 이중연결리스트로 구현되어있다.)
# - 왜 쓰냐? list queue에서 맨 앞 요소를 뺄 때(pop 등) 시간이 걸리는데 더 빠르게 가능


####################################################################


# 인정 행렬 BFS : 재귀 버전
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1], 
    [0, 1, 0, 0, 0], 
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

# bfs는 재귀가 아닌 함수 내에서 다 끝나기에 함수 안에서 만들어도된다.
visited = [0] * 5   

def bfs(start):
    # visited = [0] * 5   

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            # 갈 수 없는 곳이라면 pass
            if graph[now][to] == 0:
                continue
            
            # 이미 방문을 했으면 pass
            if visited[to] == 1:
                continue
            
            # 갈 수 있는데 아직 방문하지 않았으면 방문 표시 + 큐에 추가
            visited[to] = 1
            # print(visited) # 방문을 잘했는지 보려면 visited 프린트 해보기
            queue.append(to)

bfs(0)  # 0 1 3 2 4
        

####################################################################


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
    # visited = [0] * 5   

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









