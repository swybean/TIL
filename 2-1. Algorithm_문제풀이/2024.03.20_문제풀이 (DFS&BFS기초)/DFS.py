# 인정 행렬 DFS : 재귀 버전
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1], 
    [0, 1, 0, 0, 0], 
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]


visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에서는 없다.

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)

    # 여기 위쪽에는 기저조건만 적는 것을 권장
    # 위에 주석처리 한 visted 표시도 89번째 줄처럼 아래에서 하는 것을 권장

    # 다음 재귀 호출
    # dfs : 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    for to in range(5):
        # 갈 수 없다면 pass
        if graph[now][to] == 0:
            continue

        # 이미 방문했다면 pass
        if visited[to] == 1:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)
        
    # 돌아왔을 때 작업
        
# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)

print(path)


####################################################################


# 인접 리스트 DFS : 재귀 버전
graph = [
    [1, 3],     
    [0, 2, 4],  
    [1],        
    [0, 4],    
    [1, 3],     
]


visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에서는 없다.

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)

    # 여기 위쪽에는 기저조건만 적는 것을 권장
    # 위에 주석처리 한 visted 표시도 89번째 줄처럼 아래에서 하는 것을 권장

    # 다음 재귀 호출
    # 인접 리스트
    # 차이점1. 갈 수 없는 곳 조건 필요없음
    # 차이점2. for 문 작성 수정
    for to in graph[now]:
        # 이미 방문했다면 pass
        if visited[to] == 1:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)
        
    # 돌아왔을 때 작업
        
# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)

print(path)