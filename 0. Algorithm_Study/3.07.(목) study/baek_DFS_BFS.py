def dfs(now):
    v_dfs[now] = 1
    print(now, end = ' ')
    for j in range(1,N+1):
        if matrix[now][j] == 1 and v_dfs[j] == 0:
            v_dfs[j] = 1
            dfs(j)

def bfs(now, lst):
    v_bfs[now] = 1
    while True:
        if lst == []:
            break
        now = lst.pop(0)
        print(now, end = ' ')
        for j in range(1,N+1):
            if matrix[now][j] == 1 and v_bfs[j] == 0:
                lst += [j]
                v_bfs[j] = 1

N, M, V = map(int,input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    matrix[s][e] = matrix[e][s] = 1

v_dfs = [0] * (N+1)
v_bfs = [0] * (N+1)
dfs(V)
print()
bfs(V, [V])