def dfs():
    stack = []      # 빈스택 생성
    stack.append(X) # 시작도시를 추가하기 

    while stack:            # 스택이 비어있지 않은 동안은 반복하기 
        now = stack.pop()   # 시작도시 번호 꺼내오기 -> 여기서 빈스택이 되고
        v_dfs[now] = 1      # 시작도시 방문표시하기
        print(now)
        for i in arr[now]:
            cnt = 0
            if not v_dfs[i]:    # i 도시가 방문하지 않은 도시라면
                v_dfs[i] == 1   # 현재 i도시에 방문표시 하기
                stack.append(i) # i도시를 스택에 추가 -> 스택은 stack = [i]
                cnt += 1
        



N, M, K, X = map(int, input().split())  #도시개수N, 도로개수M, 최단거리정보K, 출발도시번호X

v_dfs = [0] * (M+1)             # dfs 함수 내에서 쓸 방문표시 리스트
arr = [[] for _ in range(N+1)]      # 단방향 간선 정보 저장할 2차원 빈리스트 생성

for _ in range(M):
    A, B = map(int, input().split())    # A도시에서 B도시로 가는 단방향 간선 정보 입력
    arr[A].append(B)            # 단방향 간선 정보 저장

dfs()   # 함수실행 및 출력
