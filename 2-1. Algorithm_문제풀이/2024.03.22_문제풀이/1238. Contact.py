'''
# 풀이방법
# 한 번 실행 -> 노드에서 연락할 수 있는 다른 노드가 "동시에" 연락
# 마지막 연락 받은 노드 중 숫자가 가장 큰 노드의 번호를 구해야 함

자료구조: 그래프, 알고리즘: BFS 사용

추가로 해야 되는 동작
- 단방향 그래프다.
- N번 만에 해당 노드를 탐색했다. _depth, depth 등으로 표현)
- 마지막_depth에서 숫자가 가장 큰 노드
- 시간 복잡도, 공간 복잡도 계산 필요

1._depth 계산
- 이전엔 N번
- 다음에는 N+1번
- 방문 표시를 1로만 하는게 아니라 +1로 해서 몇번째로 방문한건지 적어둔다!

BFS의 시간 복잡도
- 계산하는 방법 : 얼마나 방문을 할 수 있을가?
- 노드의 수(V)가 최대 100개라면 : 간선의 수는 V의 제곱에 비례 (10,000)
-> 시간 복잡도 o(V+E) : 인접 리스트 기준 
-> 즉, 완전탐색도 되는구나!

'''
# import sys
# sys.stdin = open("input_contact.txt", "r")


def bfs(start):
    # 큐에 삽입
    q = [start]

    # 방문표시
    visited = [0] * 101
    visited[start] = 1

    # 가장 깊은 depth의 가장 큰 수
    max_number = start
    # 가장 깊은 depth을 저장
    max_depth = 1

    # 큐가 빌 때까지 반복
    while q:
        now = q.pop(0)

        # 갈 수 있는 곳들
        for to in graph[now]:
            # 이미 방문했다면 pass
            if visited[to]:
                continue

            # 현재 방문 = 이전 방문 + 1번 만에 왔다!
            visited[to] = visited[now] + 1

            # depth이 더 깊어졌네? -> max_number을 초기화
            # depth은 똑같은데 숫자가 더 크네? -> max_number을 초기화
            # 1번 조건 : 현재 위치 깊이가 (저장해놨던) 최대 깊이 보다 크거나
            # 2번 조건 : (저장해놨던) 최대 깊이랑 현재 위치 깊이가 같고, (저장해놨던) 제일 큰 노드번호보다 현재 위치의
            # 노드번호가 더 크면
            # 갱신해라
            # 1번과 2번은 or 관계고, 2번 내부에서는 둘 다 성립해야 되는 and 관계
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
            
            q.append(to)

    return max_number
        


for test_case in range(1, 11):
    N, start = map(int, input().split())  # 데이터 길이 N, 시작노드 번호 start
    input_graph = list(map(int, input().split()))

    # 인접 리스트 graph
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i+1]
        graph[s].append(e)    # s는 e로 갈 수 있다.

    result = bfs(start)

    print(f'#{test_case} {result}')





