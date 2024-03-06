


# import 하기
from collections import deque


# bfs 함수 제작
def bfs(arr, start):
    visited = set()  # 방문한 노드를 저장할 집합
    bacon = {start: 0}  # 시작 노드부터의 거리를 저장할 딕셔너리
    queue = deque([start])  # BFS 탐색을 위한 큐
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐 맨 앞 노드를 방문 처리
        node = queue.popleft()
        visited.add(node)
        # 현재 노드에 연결된 모든 노드에 반복
        for i in arr[node]:
            # 만약 연결되어있지만 아직 방문 안한 노드면
            if i not in visited:
                # 방문 처리
                visited.add(i)
                # 베이컨 수 변경
                bacon[i] = bacon[node] + 1
                # 큐에 추가
                queue.append(i)
    return bacon

# 케빈 베이컨 수 계산 함수 제작
def kevin_bacon(arr, start):
    # bfs함수로 최소 베이컨 수 계산
    bacon = bfs(arr, start)
    # 총 베이컨 수
    total_bacon = sum(bacon.values())
    return total_bacon

# 입력 받기 N = 사람 수, M = 친구 관계 수
N, M = map(int, input().split())  

# 그래프 초기화 (친구 관계 표시)
arr = {i: [] for i in range(1, N+1)}

# 친구 관계 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 최소 케빈 베이컨 값 설정
min_kevin_bacon = 9999999
min_person = 0

# 최소값 찾기
for i in range(1, N+1):
    kevin_bacon_number = kevin_bacon(arr, i)
    if kevin_bacon_number < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon_number
        min_person = i

print(min_person)




