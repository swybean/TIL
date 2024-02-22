def f(T, N):
    if T>N:
        return 0
    if tree[T]!=0:  # 문제의 조건에 따라 잎노드면
        return tree[T]
    l = f(T*2, N)
    r = f(T*2+1, N)
    tree[T] = l+r
    return tree[T]
  
def f1(T, N):
    if T>N:
        return 0
    l = f1(T*2, N)
    r = f1(T*2+1, N)
    tree[T] += l+r
    return tree[T]
  
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
  
    tree = [0]*(N+1)    # 완전이진트리
    for _ in range(M):
        v, i = map(int, input().split())
        tree[v] = i
  
    f1(1, N)
    print(f'#{tc} {tree[L]}')










