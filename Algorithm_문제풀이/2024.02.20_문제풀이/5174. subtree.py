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

