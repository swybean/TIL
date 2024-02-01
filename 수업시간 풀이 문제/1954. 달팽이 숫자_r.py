'''
팁하나
방향을 우0 하1 좌2 상3 우4로 하는 방법
방향을 현재 dir이라고 하면은 dir += 1로 하면
다시 0으로 되돌리는 방법은
while 해가지고 열심히 돌고있다 :
:
:
dir = (dir+1) % 4 이렇게 하면
dir이 3인 순간에는 1 더하면 4가되니까 % 4때문에 0이되서 다시 0으로 돌아간다.

0123 0123 반복하고 싶으면 위에 방법을 써라
코드를 짤 때 종종 사용되는 방법이다.

if dir == 3:
    dir = 0
else: 
    dir += 1
하면 어색해 보인다. 위에 방법 쓰자.

위에 방법은 방향의 정의만 하면 도는 방향이 바뀌어도 써먹을 수 있다.
'''

'''
# 조창훈님 코드 말씀
값을 1부터 시작하느냐 0부터 시작하느냐에 따라 연산하는 순서가 달라진다.


# 조창훈님 코드
T = int(input())
for tc in range(1, T + 1):
    # 배열의 크기
    N = int(input())
    # 맵 매트릭스
    matrix = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]  # 우 하 좌 상의 순서로 방향 전환
    dj = [1, 0, -1, 0]
    direction = 0
    input_v = 2
    i = j = 0
    matrix[i][j] = 1
    while input_v < N*N+1:
        ni = di[direction] + i
        nj = dj[direction] + j
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
            matrix[ni][nj] = input_v
            i = ni
            j = nj
            input_v += 1
        else:
            direction = (direction + 1) % 4
 
    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])
'''


'''
상무형 코드
구현의 순서만 위와 다를뿐 전체적인 구성은 다르다.
조금 더 간결하다
count를 1부터 시작하는게 보기 좋을 수도 있겠다.

t = int(input())
 
for test_case in range(1, t+1):
    n = int(input())
    num_list = [[0] * n for _ in range(n)]
 
    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    x = 0
    y = 0
    i = 0
    count = 1
    num_list[0][0] = 1
 
    while count < n * n:
        nx = x + dx[i]      # 이동할 곳 출력
        ny = y + dy[i]
        # 이동할 위치가 0보다 작거나 n보다 크거나 (index 여서 = 추가) 이동할 위치의 값이 0이 아니면.
        if nx < 0 or nx >= n or ny < 0 or ny >= n or num_list[nx][ny] != 0:
            i = (i + 1) % 4 # 방향을 바꿔서 계산하고
            nx = x + dx[i]
            ny = y + dy[i]
 
        x = nx      # 그렇지 않으면 아까전에 그걸 그냥 그대로 쓰면 돼
        y = ny
        count += 1
        num_list[nx][ny] = count    #증가시킨 다음에 그 증가시킨 값을 여기다가 적어
 
    print(f'#{test_case}')
    for index in range(n):
        print(*num_list[index])   # list 없이 값만 출력해줄 때 * 사용 key, value 뽑고 싶을 때는 **


'''











