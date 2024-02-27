T = 10
for _ in range(1, T+1):
    test_case = int(input())    # 테스트 케이스 번호 입력
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원배열 100x100 만들기

    result = 0  # 최대값 저장할 변수

    # 각 행의 합 구하기
    for i in range(100):
        isum = 0
        for j in range(100):
            isum += arr[i][j]
            if result < isum:
                result = isum
    
    # 각 열의 합 구하기
    for j in range(100):
        jsum = 0
        for i in range(100):
            jsum += arr[i][j]
            if result < jsum:
                result = jsum

    # 우하향 대각선의 합 구하기
    dae1 = 0
    for i in range(100): 
        dae1 += arr[i][i]
        if result < dae1:
            result = dae1
            
    # 좌하향 대각석의 합 구하기
    dae2 =0
    for i in range(100):
        dae2 += arr[i][99-i]
        if result < dae2:
            result = dae2

    
    print(f'#{test_case} {result}')



