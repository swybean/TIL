def dfs(r, s, i):   # 횟수, 전력 사용량의 합, 행
    global min_v
 
    if r == N-1:  # 모든 경우의 수를 다 돌았을 때
        if min_v > s + arr[i][0]:   # 마지막에 돌아가는 길 까지 더하기
            min_v = s + arr[i][0]
            return
    elif s >= min_v:  # 이미 min_v 보다 전력 소비량이 더 큰 경우
        return
 
    for k in range(1, N):   # 돌아가는 길은 마지막에 해야 함 
        if arr[i][k] != 0 and visited[k] == 0:  # 방문하지 않았고 0이 아니면
            visited[k] = 1  # 방문처리
            dfs(r+1, s + arr[i][k], i=k)  # 다음 구역으로 이동, s+전력량, 열이 다음 장소의 행이 되어야 함 
            visited[k] = 0  # 초기화
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = 100 * N
    dfs(0, 0, 0)  # 횟수, 전력사용량 합, 끝 값이 시작값이 되어야 함
    print(f'#{tc} {min_v}')


    