# 플로이드 워셜 알고리즘 소스코드 연습


# 무한 10억 설정
INF = int(1e9)

# 노드의 개수 n, 간선의 개수 m 입력
n = int(input())
m = int(input())

# 2차원 리스트 생성 및 모든 값 무한으로 초기화
### 왜 그래프를 이렇게 만드는 거지? 완전 모르는건 아닌데 잘 이해가 안감.
graph = [[INF] * (n+1) for _ in range(n+1)]

# 본인이 본인으로 가는 비용은 0으로 초기화
# range(1, n+1)에서 출발a와 도착b가 같다면(본인->본인) 비용은 0이다.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c     # a에서 b로 가는 비용은 c다.


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):             # 중간에 거쳐갈 지점 k를 반복순회
    for a in range(1, n+1):         # 출발점 a를 해당 범위에서 반복순회
        for b in range(1, n+1):     # 도착점 b도 해당 범위에서 반복순회
            # 최소 비용은 둘 중 더 작은 것이다.
            # a에서 b로 바로 가는 것과 // a에서 k를 가고 k에서 b를 가는 것 중에서
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()


'''
입력값
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력값
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
'''



