from collections import deque

di = [2, 2, -2, -2, 1, 1, -1, -1]
dj = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(i, j):
    global cnt

    q = deque()         # 큐 생성
    q.append((i, j))   # 큐에 시작 위치 삽입
    visited = [[0] * N for _ in range(N)]   # 방문표시 리스트

    # 큐가 빌 때까지 반복
    while q:
        i, j = q.popleft()  # 시작위치 꺼내오기
        visited[i][j] = 1   # 시작위치 방문표시

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                visited[ni][nj] = visited[i][j] + 1
                # 최종 결과에서 -1 을 해줘야 한다. 왜냐? 시작할때 시작위치 +1을 했기 때문에
                q.append((ni, nj))
                if ni == target_x and nj == tartgey_y:
                    return visited[ni][nj] - 1 



T = int(input())        # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input())    # 체스판 한 변의 길이
    x, y = map(int, input().split())    # 현재 나이트 위치 좌표
    target_x, tartgey_y = map(int, input().split()) # 목표 좌표

    arr = [[0] * N for _ in range(N)]

    cnt = 0     # 도착까지 이동 횟수
    bfs(x, y)

    print(cnt)


