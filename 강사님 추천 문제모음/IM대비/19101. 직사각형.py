T = int(input())
for test_case in range(1, T+1):
    
    N = 1001    # 2차원 배열 틀에 쓸 범위
    result = 0  # 결과값 (직사각형1, 선분2, 점3, 공통없음4)
    h = 0       # 2가 적힌 사각형의 세로
    w = 0       # 2가 적힌 사각형의 가로

    # 2차원 배열 틀 만들기
    arr = [[0] * N for _ in range(N)]
    
    # 두 사각형의 꼭짓점 좌표값 입력받기
    x1, y1, x2, y2 = map(int, input().split())
    p1, q1, p2, q2 = map(int, input().split())

    # 첫번째 사각형 범위에 1씩 더하기
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] += 1
    # 두번째 사각형 범위에 2씩 더하기
    for p in range(p1, p2+1):
        for q in range(q1, q2+1):
            arr[p][q] += 1

    # 색칠이 완료된 전체 배열에서 2를 찾아서 세로, 가로 구하기
    for row in arr:
        if 2 in row:
            h += 1
            w = row.count(2)
            
    if h == 1 and w ==1:    # 점 (2가 적힌 칸이 1칸이라면)
        result = 3
    elif h == 1 or w == 1:  # 선분 (2가 적힌 칸이 가로,세로 중 하나만 1이라면)
        result = 2
    elif h > 1 and w > 1:   # 직사각형 (가로, 세로 모두 2가 적힌칸이 1보다 크면)
        result = 1
    else:                   # 공통없음 (2가 적힌 칸이 아예 없으면)
        result = 4
    
    print(f'#{test_case} {result}')

