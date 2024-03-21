'''
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다.
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

입력 조건
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. 
(1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

출력 조건
첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. 
i번째 줄에는 정점 i의 방문 순서를 출력한다. 
시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.
'''

## pypy3 로 제출해야지 맞음
## python으로 내면 시간초과

import sys
sys.setrecursionlimit(10**5)  # 재귀 깊이 제한을 늘려줍니다.

N, M, R = map(int, input().split())

# 인접리스트 생성
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (N + 1)
order = [0] * (N + 1)
order_idx = 1

def dfs(node):
    global order_idx
    visited[node] = True
    order[node] = order_idx
    order_idx += 1
    for neighbor in sorted(adj_list[node], reverse=True):
        if not visited[neighbor]:
            dfs(neighbor)

dfs(R)

# 출력
for i in range(1, N + 1):
    print(order[i])





'''
5 5 1
1 4
1 2
2 3
2 4
3 4

1
4
3
2
0
'''
