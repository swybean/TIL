# import sys
# sys.stdin = open('input2.txt', 'r')


'''
1   # 테스트 케이스 개수
6 5 # V, E : 노드 개수, 간선 개수
1 4 
1 3
2 3
2 5
4 6
1 6 # S, G : 출발노드, 도착노드
'''






'''
########## 내가 풀다 만 것 #########

# 함수 제작
def dfs(i, V): # 시작 i, 마지막 V
    # visited, stack 생성 및 초기화
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1  # 시작점 방문
    print(i)    # 정점에서 할 일
    while True: # 탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점 w가 있으면
        for w in adjl[i]:   # 인접 정점 중에서
            if visited[w] == 0: #방문 안했으면
                stack.append(i) # push(i), i를 지나서
                i = w           # w에 방문
                visited[i] = 1  # 나 방문했다 라는 뜻
                print(i)    # 방문해서 할 일
                break       # for j 중단, if문 쭉쭉 반복해라
        # i에 남은 인접 정점이 없으면
        else:   # for w에 대한 else
            if stack:   # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                        # top을 구현했으면 top > -1 이라고 하면 된다.
                i = stack.pop() 
            else:   # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break   # while True 중단
    return # 리턴값은 생략해도 된다.


def dfs(i, v):
    visited = [0] * (v+1)
    stack = []
    visited[i] = 1

    while True:
        for w in 





T = int(input())    # 테스트 케이스 입력
V, E = map(int, input().split())    # V는 노드 개수, E는 간선 개수
arr = [list(map(int, input().split())) for _ in range(E)]   # 간선 정보 입력
S, G = map(int, input().split())    # 출발노드 S, 도착노드 G

'''






















'''
T = int(input())
 
def dfs(node, start, end):
    stack = [start]
    while stack:
        now = stack.pop()
        for n in node:
            if n[0] == now:
                if n[1] == end:
                    return 1
                else:
                    stack.append(n[1])
    return 0
 
for tc in range(T):
    v, e = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int,input().split())
 
    result = dfs(node, s, g)
 
    print(f'#{tc+1} {result}')




def path(v, e, node_line_list, s, g):
 
    top = 0
    stack = [0] * v
    stack[0] = s
    while stack[0] != 0:
        flag = 0
        for i in range(e):
            if node_line_list[i][0] == stack[top]:
                top += 1
                stack[top] = node_line_list[i][1]
                node_line_list[i][0] = node_line_list[i][1] = 0
                flag = 1
                break
        if stack[top] == g:
            return 1
        if flag == 0:
            stack[top] = 0
            top -= 1
 
    return 0
 
 
T = int(input())
for case in range(1, T+1):
    v, e = map(int, input().split())    # v : 노드 개수, e = 간선 개수
    node_line_list = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())    # s : 시작 노드, g = 도착 노드
 
    print(f'#{case}', path(v, e, node_line_list, s, g))
'''