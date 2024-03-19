

# N = int(input())    # 사람 수 N

# a, b = map(int, input().split())    # 촌수를 계산해야 할 다른 두 사람의 번호

# M = int(input())    # 부모자식 관계 수 M

# arr = []            # 부모자식 관계 저장할 리스트

# for _ in range(N):
#     x, y = map(int, input().split())
#     arr.append((x, y))




def subtree(node):
    counts = 1
    for child in arr[node]:
        counts += subtree(child)
    return counts
 
T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    arr = [[] for _ in range(E+2)]
 
    nodes = list(map(int, input().split()))
    for i in range(0, len(nodes), 2):
        parent, child = nodes[i], nodes[i+1]
        arr[parent].append(child)
 
    print(f'#{test_case} {subtree(N)}')

####################################################

t = int(input())            # 테스트 케이스 개수 받기
 
def pre_order(T) :          # 전위 순회 함수를 만들자
    global cnt
    if T :
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])
 
for tc in range(1, t+1) :
    E, N = map(int, input().split())        # 간선의 개수 E, 서브트리에서의 루트 N
    arr = list(map(int, input().split()))   # 트리를 만들 재료들 받기
    left = [0] * (E+2)                      # 부모에서 왼쪽 자식을 넣을 리스트
    # (왜 E+2인가? 정점의 개수 N는 간선(E) + 1 , 리스트에서 0 말고 순서대로 넣으려면 N+1 해야 함 따라서 E+2)
    right = [0] * (E+2)                     # 부모에서 오른쪽 자식을 넣을 리스트
    parent = [0] * (E+2)                    # 자식들의 부모가 누군지 넣을 리스트
    cnt = 0                                 # 루트가 N인 서브트리에 노드 개수를 넣을 변수
 
    for i in range(E) :
        p, c = arr[i*2], arr[i*2 + 1]       # 앞의 수를 부모, 뒤의 수를 자식으로 받는다.
 
        if left[p] == 0 :                   # 만약 부모의 왼쪽 자식 리스트가 비어있으면,
            left[p] = c                     # 왼쪽 자식 리스트에 넣어준다.
        else :                              # 아니라면 (왼쪽 자식 리스트가 채워져 있으면)
            right[p] = c                    # 오른쪽 자식 리스트에 넣어준다.
        parent[c] = p                       # 부모 리스트 자식 인덱스에 부모 넣어주기
 
    pre_order(N)
 
    print(f'#{tc} {cnt}')