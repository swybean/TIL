# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
         parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N은 학생들의 번호 (0 ~ N+1), M은 선생님의 연산횟수
N, M = map(int, input().split())

# 부모 테이블 생성
parent = [0] * (N + 1)

# 부모 테이블에서 부모를 자기자신으로 설정
for i in range(0, N+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(M):
    oper, a, b = map(int, input().split())
    # 합집합 연산이면
    if oper == 0:
        union_parent(parent, a, b)

    # 같은팀 확인 연산이면
    if oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')























