# def chonsu(node):
#     counts = 1
#     for child in arr[node]:
#         counts += chonsu(child)
#     if counts >= 1:
#         return counts
#     else:
#         return -1



# N = int(input())    # 전체 사람의 수 N
# arr = [[] for _ in range(N+1)]  # 각 노드의 부모-자식 관계를 저장할 리스트 arr 생성

# a, b = map(int, input().split())    # 촌수를 계산해야 할 두 사람의 번호 a, b

# nodes = []  # 부모-자식 관계 숫자를 받을 리스트

# M = int(input())    # 부모-자식 관계의 수 M

# # 부모-자식 관계 숫자들을 입력할 1차원 리스트
# for _ in range(M):
#     nodes.extend(list(map(int, input().split())))

# # 입력값을 순회하면서 부모-자식 관계를 처리
# for i in range(0, len(nodes), 2):
#     parent, child = nodes[i], nodes[i+1]
#     arr[parent].append(child)

# # print(arr) # [[], [2, 3], [7, 8, 9], [], [5, 6], [], [], [], [], []]
# print(chonsu(7))


def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)

n = int(input())

graph = [[] for _ in range(n+1)]

s, e = map(int, input().split())

M = int(input())

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0]*(n+1)

dfs(s)

if check[e] > 0:
    print(check[e])
else:
    print(-1)


'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

3
'''


'''
# SWEA 'subtree' 문제 풀이
# 이거부터 이해 완료하고 '촌수계산' 문제 풀기

def subtree(node):
    counts = 1
    for child in arr[node]:
        counts += subtree(child)
    return counts


T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())        # 간선개수 E, 루트노드 N 입력
    nodes = list(map(int, input().split())) # 부모-자식 관계 리스트
    arr = [[] for _ in range(E+2)]  # 빈 2차원 리스트, 부모-자식 관계 저장할 예정임
    # range(E+2)인 이유 : 노드의 개수는 간선 개수 + 1, range니까 +1해야해서 총 +2를 해야함

    for i in range(0, len(nodes), 2):   # 처음부터 nodes길이만큼 2칸씩 반복해서 i찾기
        parent, child = nodes[i], nodes[i+1]    # parent는 i, child는 i+1로 설정
        arr[parent].append(child)       
        # 빈 2차원 리스트 arr의 parent 인덱스 번호 내부리스트에 child를 저장하기
    
    print(f'#{test_case} {subtree(N)}')
'''



