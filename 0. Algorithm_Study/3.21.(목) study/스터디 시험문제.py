## 문제 1번
# 1번 함수를 이용해서 n!을 for문을 써서 구현해라.

# def fac1(N):
#     result = 1
#     for i in range(1, N+1):
#         result *= i
#     return result

# print(fac1(5))



# 2번 함수를 이용해서 n!을 재귀적으로 구현하라.

## n! = n x (n-1) x (n-2)

# def fac(num):

#     if num > 1:
#         num *= fac(num-1)
#         return num
#     else:
#         return 1

# N = int(input())

# print(fac(N))




'''
def fac(num):
    global result
    
    if num == 1:
        result *= num
        return result
    
    if num > 1:
        result *= (num - 1)
        num -= 1
        print(f' 출력 : {result}')
        fac(num)
        return result



num = int(input())

result = num

print(fac(num))
'''



## 문제2번

# 2-1번

# def dfs(node):
#     stack = []
#     stack.append(node)
#     visitd[node] = 1

#     while stack:
#         now = stack.pop()
#         print(now, end=' ')
#         for next in graph[now]:
#             if visitd[next] == 0:
#                 visitd[next] = 1
#                 stack.append(next)

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visitd = [0] * len(graph)

# dfs(1)


# ## 2-2번

# from collections import deque

# def bfs(node):
#     q = deque()
#     q.append(node)
#     visited[node] = 1
#     print(node, end=' ')

#     while q:
#         now = q.popleft()
#         for next in graph[now]:
#             if visited[next] == 0:
#                 visited[next] = 1
#                 q.append(next)
#                 print(next, end=' ')
            
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [0] * len(graph)

# bfs(1)





## dfs 재귀버전

def dfs(node):

    for next in graph[node]:
        if visited[next] == 1:
            continue
        
        visited[next] = 1
        path.append(next)
        dfs(next)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

path = []
visited = [0] * len(graph)

visited[1] = 1
path.append(1)

dfs(1)

print(path)