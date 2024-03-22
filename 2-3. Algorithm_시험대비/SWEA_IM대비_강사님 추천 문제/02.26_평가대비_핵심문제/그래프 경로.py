def dfs(i, V, last):
    visited = [0] * (V+1)
    




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())  #  출발 노드, 도착 노드 나눠서 받기!
        arr[n1].append(n2)
    S, G = map(int, input().split())
    result = dfs(S, V, G)
    
    print(f'#{tc} {result}')

