###############아예 모르겠음###############
# 해설 코드 찾아다가 공부했는데 문제부터 이해가 안됨..
# 순열 (3, 2, 7, 8, 1, 4, 5, 6) 이게 왜 1->3->7->5->1, 2 , 4->6->8->4 로 구성되는지도 모르겠음..


# 함수 만들기
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 인접 노드들에 반복
    for i in graph[v]:
        # 인접 노드 중 방문하지 않은 노드가 있다면
        if not visited[i]:
            # dfs함수 재귀호출
            dfs(graph, i, visited)

# 테스트 케이스의 수 입력
T = int(input())

for _ in range(T):
    # 순열의 크기 입력
    N = int(input())
    
    # 순열 입력
    permutation = list(map(int, input().split()))
    
    # 그래프 생성, 1부터 N까지 노드 생성
    graph = [[] for _ in range(N+1)]
    # 1부터 N까지의 노드에 대해서
    for i in range(1, N+1):
        # 해당노드와 순열의 값을 그래프에 추가
        graph[i].append(permutation[i-1])
    
    # 방문 여부를 저장할 리스트 생성, 모두 False로 초기화
    visited = [False] * (N+1)
    
    # 순열 사이클 개수 카운트 생성
    cycle_count = 0
    # 1부터 N까지의 노드에 대해서
    for i in range(1, N+1):
        # 해당 노드를 방문하지 않았다면
        if not visited[i]:
            # 해당 노드에서 dfs함수 수행
            dfs(graph, i, visited)
            # dfs 탐색이 종료되면 사이클 개수 1 증가
            cycle_count += 1
    
    print(cycle_count)




