
def dfs(r, s, i):   # r 이동횟수, s 배터리 소비량, i 행
    global min_v    # 최소값 받아오기

    # 기저조건
    # 모든 구역을 다 돌고 사무실로 돌아가야한다.

    # 마지막 구역까지 도착하고 다시 사무실로 돌아가야 한다면
    if r == N - 1:  #
        # min_v가 현재까지 배터리 소비량 + 마지막 구역에서 사무실 가는 소비량보다 작다면
        if min_v > s + arr[i][0]:   
            min_v = s + arr[i][0]   # min_v 갱신
            return
    elif s >= min_v:    # 구역을 모두 돌지 않았음에도 이미 최소값보다 배터리 소비량이 크면 종료
        return
    
    # range(1, N)인 이유 : range(N)으로 하면 모든 구역을 돌기 전에 사무실(0)으로 갈 수 있기 때문에
    for k in range(1, N):
        # arr[i][k]가 0이 아니고(같은 번호 구역으로 가면 안되니까) 방문하지 않았다면
        if arr[i][k] != 0 and visited[k] == 0:
            # 방문하고 방문처리하기
            visited[k] = 1

            # 재귀 호출
            # 이동횟수 +1, 배터리 소비량 더하기, *해당 열이 다음 행이 되어야함
            # *해당 구역으로 도착했으니 해당 구역에서 다른 구역으로 갈 소비량이 적힌 행으로 가야함
            dfs(r+1, s + arr[i][k], i = k)

            # 재귀가 끝나면 다음 경우의 수를 위해 방문표시 초기화
            visited[k] = 0 

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N   # 방문표시 리스트 생성
    min_v = 100 * N     # 최소값 설정
    dfs(0, 0, 0)    # 이동횟수, 배터리 소비량, 행(끝값==시작값이어야함)
    print(f'#{test_case} {min_v}')

