
# 최단경로
# 가선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중 간선의 가중치의 합이 최소인 경로

# 하나의 시작 정점에서 끝 정점까지의 최단경로
# 1. 다익스트라 알고리즘
# - 음의 가중치를 허용하지 않음

# 2. 벨만-포드 알고리즘
# - 음의 가중치 허용

# 모든 정점들에 대한 최단 경로
# -플로이드-워샬 알고리즘


# 다익스트라 (dijkstra) 알고리즘
# - 시작 정점에서 (누적)거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
# - 시작정점(s)에서 끝정점(t) 까지의 최단 경로에 정점 x가 존재한다.
# - 이때, 최단경로는 s에서 x까지의 최단경로와 x에서 t까지의 최단경로로 구성된다.
# - 탐욕기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사

import sys
sys.stdin = open("input2.txt", "r")

from heapq import heappush, heappop


def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # now가 이미 처리된 노드라면 pass
        if distance[now] < dist:
            continue 

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            
            # 누적 거리 계산
            new_dist = dist + next_dist
            
            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_node] = new_dist

            # next_node의 인접 노드들을 추가
            heappush(pq, (next_dist, next_node))


# 엄청 큰 값, 10억
INF = int(1e9)

V, E = map(int, input().split())

# 시작 노드 번호
start = 0

# 인접 리스트
graph = [[] for _ in range(V)]

# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    start, end, weight = map(int, input().split())
    # start에서 end까지는 weight 만큼 걸려서 갈 수 있다.
    graph[start].append([weight, end])


dijkstra(0)

print(distance)






