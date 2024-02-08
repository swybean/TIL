'''
연습문제 교재 63쪽

다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
모든 저점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오.
시작 정점을 1로 시작하시오.

입력 : 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 
출력 : 1 2 4 6 5 7 3
(5까지 갔다가 6으로 돌아가고, 
7, 3갔다가 뒷걸음질로 6 4 2 1로 1까지 가면서 pop해서 빈 스택으로 만든다.)

입력 : 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 의 뜻은
1-2, 1-3, 2-4, 2-5, 4-6, 5-6, 6-7, 3-7 끼리 간선으로 연결되었다는 뜻이다.
'''

'''
2번에 도착: 스택에 1푸시
4번에 가면: 스택에 2푸시
6번에 가면: 스택에 4푸시
5번에 가면: 스택에 6푸시 
-> 여기까지 스택에 1, 2, 4 , 6순으로 푸시되어잇음

이제 갈 곳이 없으니
6번으로 돌아감 : 스택에서 6번 팝
7번에 가면: 스택에 6푸시
3번에 가면: 스택에 7푸시
-> 스택은 1, 2, 4, 6, 7 순으로 푸시되어있음

다시 역순으로 돌아가면서 하나씩 스택에서 팝하면 빈 스택이 된다.
'''

'''
입력값
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 <- 인덱스 번호
인덱스번호 0,1 / 2,3 ... 이런식으로 묶어서 0, 1, ...번으로 만든다
'''

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


V, E = map(int, input().split())    # V = 노드, E = 간선의 수를 입력 받는다.
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # adjl[i] 행에는 i에 인접인 정점번호를 저장할거다.
for i in range(E):  # E개의 정점을 읽어오려고 한다.
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjl[n1].append(n2) # 1번과 2번이 연결되어있어 라는 뜻
    adjl[n2].append(n1) # 방향이 없는 경우에만 이 코드도 써줘야한다. 있는데 쓰면 오류남
    # 빠른 순으로 해야 되면 각 행을 한번씩 sort 하면 된다.
dfs(1, V)

# print(adjl) 
#출력값: [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
# 1번은 2.3에 인접, 2번은 1.4.5에 인접, 3번은 1.7에 인접... 이런 뜻임
# 맨 앞 []은 뭐지...? => 인덱스 맞추려고 넣어둔 것이라고 함
    



'''
# 인접 리스트를 먼저 만들어보자.
adjl = []
adjl[0] = 기준정점
0번행에는 뭐가 없음
i번행에는 i번에 인접인 정점 번호 저장한다.
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