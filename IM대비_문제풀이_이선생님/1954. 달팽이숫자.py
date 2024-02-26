# 4방향 살펴보기 위한 델타
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 2차원 배열 크기 N 입력
    
    arr = [[0] * N for _ in range(N)]   # 달팽이 숫자 넣을 N*N 2차원 배열 생성

    number = 1          # 달팽이 배열에 넣을 숫자의 시작은 1 (추후 1씩 더하면서 넣는거 생각)
    i, j = 0, 0         # 시작 인덱스 번호
    dir = 0             # 시작 방향은 오른쪽으로 가야하니 델타[0] 써야함
    arr[0][0] = number  # 배열 좌상단 첫칸은 1로 시작 

    while number < N * N:   # number가 N*N까지만 반복하자
        ni = i + di[dir]
        nj = j + dj[dir]
        # 배열 범위를 벗어나지 않거나 숫자가 이미 적혀있는 곳이 아니라면
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            dir = (dir+1) % 4   # 델타를 0, 1, 2, 3만 반복하기 위한 설정
            ni = i + di[dir]    # ni, nj를 바뀐 dir을 이용해 재설정 (방향 변경)
            nj = j + dj[dir]

        i = ni
        j = nj
        number += 1             # 다음에 적을 숫자는 1씩 커져야하니 +1
        arr[ni][nj] = number    # 이동한 다음칸에 커진 숫자를 입력
    
    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])


