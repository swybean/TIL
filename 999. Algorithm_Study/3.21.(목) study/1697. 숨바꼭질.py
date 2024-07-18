# from collections import deque
 
# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if v == k:
#             return visited[v]
#         for i in (v - 1, v + 1, v * 2):
#             if 0 <= i <= 1000000 and not visited[i]:
#                 visited[i] = visited[v] + 1
#                 q.append(i)
 
# n, k = map(int, input().split())
# visited = [0 for i in range(1000001)]
# print(bfs(n))

def bfs(N, K):  # 수빈이 위치 N, 동생 위치 K
    global result
    q = []      # 큐 생성
    q.append(N) # 시작점 큐에 삽입
    visited = [0] * (100001)
    visited[N] = 1

    while q:
        now = q.pop(0)  # 현재 위치 꺼내기
        if now == K:    # 현재 위치가 동생 위치 K와 같으면 종료
            return visited[now] - 1
        
        # 걷는 경우 : X-1로 갈 때
        if now-1 >= 0 and visited[now-1] == 0:
            q.append(now-1)
            visited[now-1] = visited[now] + 1

        # 걷는 경우 : X+1로 갈 때
        if now+1 <= 100000 and visited[now+1] == 0:
            q.append(now+1)
            visited[now+1] = visited[now] + 1

        # 순간이동 : X*2로 갈 때
        if now * 2 <= 100000 and visited[now*2] == 0:
            q.append(now*2)
            visited[now*2] = visited[now] + 1

    return result

result = 100000

N, K = map(int, input().split())

print(bfs(N, K))

'''
1 0 넣으면 1
5 0 넣으면 5
'''

# ### 백준에서 77%에서 틀렸습니다 뜨는 코드
# def bfs(N, K):  # 수빈이 위치 N, 동생 위치 K
#     global result
#     q = []      # 큐 생성
#     q.append(N) # 시작점 큐에 삽입
#     visited = [0] * (100001)
#     visited[N] = 1

#     while q:
#         now = q.pop(0)  # 현재 위치 꺼내기
#         if now == K:    # 현재 위치가 동생 위치 K와 같으면 종료
#             return visited[now] - 1
        
#         # 걷는 경우 : X-1로 갈 때
#         if now-1 > 0 and visited[now-1] == 0:
#             q.append(now-1)
#             visited[now-1] = visited[now] + 1

#         # 걷는 경우 : X+1로 갈 때
#         if now+1 <= 100000 and visited[now+1] == 0:
#             q.append(now+1)
#             visited[now+1] = visited[now] + 1

#         # 순간이동 : X*2로 갈 때
#         if now * 2 <= 100000 and visited[now*2] == 0:
#             q.append(now*2)
#             visited[now*2] = visited[now] + 1
#     return result

# result = 100000

# N, K = map(int, input().split())

# print(bfs(N, K))


# ###백준에서 50%에서 틀렸습니다 뜨는 코드
# def bfs(N, M):
#     q = []              
#     q.append(N)        
#     visited = [0] * (1000001) 
#     visited[N] = 1             
    
#     while q:            
#         t = q.pop(0)   
#         if t == M:
#             return visited[t] - 1
        
#         if 0 < t -1 and visited[t - 1] == 0:
#             q.append(t - 1)
#             visited[t - 1] = visited[t] + 1
                                   
#         if t + 1 <= 1000000 and visited[t + 1] == 0:
#             q.append(t + 1)
#             visited[t + 1] = visited[t] + 1

#         if t * 2 <= 1000000 and visited[t * 2] == 0:
#             q.append(t * 2)
#             visited[t * 2] = visited[t] + 1

# N, K = map(int, input().split())

# print(bfs(N, K))
