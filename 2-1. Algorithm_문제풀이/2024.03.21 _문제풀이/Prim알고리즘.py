# Prim 알고리즘
# 하나의 정점에서 연결된 간선들 중 하나씩 선택하면서 MST를 만들어 가는 방식
# 1. 임의 정점을 하나 선택해서 시작
# 2. 선택한 정점과 인접하는 정점들 중(bfs) 최소비용(우선순위)의 간선이 존재하는 정점을 선택
#   -> bfs의 queue + 우선순위 => 우선순위 큐  
# 3. 모든 정점이 선택될 때까지 1~2 과정을 반복

# 서로소인 2개의 집합 정보를 유지
# 트리 정점들 : MST를 만들기 위해 선택된 정점들
# 비트리 정점들 : 선택되지 않은 정점들


# 교재 문제 (12쪽)
# 노드 7개, 간선 11개

import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def prim(start):
    pq = []
    MST = [0] * V   # 방문표시 리스트 (visited와 같은 역할)

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존 bfs] 노드 번호만 관리
    # [PRIM] 우선 순위가 가중치에 따라 정렬 / 가중치가 낮으면 먼저 나와야 한다.
    # -> 관리해야 할 데이터는 2가지 : 가중치, 노드번호
    # -> 동시에 2가지 데이터 다루는 방법
    #      1. class로 만들기
    #      2. 튜플로 관리 (오늘 사용할 방법)
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # [기존 BFS] : 무조건 방문
        # [PRIM] : 일단 pq에 넣고 방문은 X
        # 우선순위 큐(prim)의 특성 상 
        # 더 먼거리로 가는 방법으로 가는 방법이 큐(pq)에 저장되어있기 때문에
        # 기존에 이미 더 짧은 거리로 방문을 했다면 continue
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        # 누적합 처리
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to] == 1:
                continue
            
            # 갈 수 있고 방문하지 않았으면
            # pq에 넣기
            heappush(pq, (graph[now][to], to))
    
    print(f'최소 비용 : {sum_weight}')


# 정점의 개수 V, 노드의 개수 E
V, E = map(int, input().split())

# 인접 행렬로 저장
# -[과제] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end, w = map(int, input().split())

    # [기존 의미] : 3에서 4로 갈 수 있다.
    # graph[3][4] = 1

    # [가중치 그래프] : 3에서 4로 가는데 31이라는 비용이 든다.
    # graph[3][4] = 31

    # 가중치 저장
    graph[start][end] = w
    graph[end][start] = w   # 무방향 그래프

prim(0)