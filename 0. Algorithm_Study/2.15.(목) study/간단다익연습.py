#### 간단한 다익스트라 알고리즘 소스코드 연습




# 무한값으로 10억 설정
INF = int(1e9)

# 노드의 개수n, 간선의 개수m 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 생성
visited = [False] * (n + 1)

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)


# 모든 간선의 정보를 입력받기
for _ in range(m):
    # a노드에서 b노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 함수제작 : 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 반환
def get_small_node():
    min_v = INF     # 최소값을 10억으로 설정
    index = 0       # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        # 만약 i의 최단거리가 최소값보다 작고, 방문하지 않았던 노드라면
        if distance[i] < min_v and not visited[i]:
            min_v = distance[i]         # i의 거리를 최소값으로 설정
            index = i                   # 인덱스도 i로 설정
    return index                        # 해당 인덱스를 반환


# 함수제작 : 다익스트라 함수
def dij(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    # 시작노드 설정?
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n -1 개의 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 반복 처리
        now = get_small_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dij(start)

# 모든 노드로 가기 위한 최단 거리를 수행
for i in range(1, n+1):
    # 도달할 수 없으면 무한을 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


'''
입력값
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력값
0
2
3
1
2
4
'''








