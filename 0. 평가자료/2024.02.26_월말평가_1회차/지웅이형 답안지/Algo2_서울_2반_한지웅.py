# 알고리즘 사격게임
'''
N*N size (3<=N<=8)
한 줄에서 두개이상의 표적을 맞추면 실격 (가로 세로 둘다 고려)
어떤 단계에서는 점수가 음수인 경우도 있음. 이 경우엔 음수를 맞추면 실격
'''

def dfs(n,lst):
    if n == N:
        search_list.append(lst)
        return
    for i in range(N):
        if visited[i] == 0: # 방문한 적이 없으면
            visited[i] = 1 # 방문 기록을 남기고
            dfs(n+1, lst+[i]) # 재귀
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int,input().split()))]

    # 정의한 함수를 활용해 탐색할 index를 구하자
    search_list = []
    visited = [0] * (N+1)
    dfs(0,[])

    # search_list대로 사격을 실시한다.
    score_list = []
    for k in search_list:
        score = 0
        for shoot in range(N):
            if matrix[shoot][k[shoot]] >= 0:
                score += matrix[shoot][k[shoot]]
            else:
                score = -987654321 # 음수를 쏘면 실격
                break
        score_list += [score]

    print(f"#{tc} {max(score_list)}")