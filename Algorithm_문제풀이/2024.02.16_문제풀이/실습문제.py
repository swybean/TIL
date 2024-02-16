'''
V개 노드 개수
E개 간선 정보
출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내시오.


'''
def bfs(start, N, G):  
    q = []                  
    visited = [0] * (N+1)   
    q.append(start)         
    visited[start] = 1    
    
    while q:
        t = q.pop(0)    
        if t == G:      
            return visited[t]-1
        for i in adjl[t]:       
            if visited[i]:      
                q.append(i)
                visited[i] = visited[t] + 1
    return 0    # G까지 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1) 

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')


