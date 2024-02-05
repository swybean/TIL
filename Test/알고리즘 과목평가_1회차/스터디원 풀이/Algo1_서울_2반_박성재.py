Test = int(input()) # test case 변수 설정

for test in range(1, Test+1):   # test는 1부터 Test까지 반복 진행
    N = int(input())    # 가로 세로 N X N
    BOX = []
    max_result = 0
    for _ in range(N):  # N X N 박스 제작
        BOX.append(list(map(int, input().split()))) # 행마다 열에 해당되는 값 추가
    for i in range(1, N-1): # 1 ~ N-2 까지(가장자리는 보너스점수가 0이기 때문에 제외) 행 탐색
        for j in range(1, N-1): # 1 ~ N-2 까지(가장자리는 보너스점수가 0이기 때문에 제외) 열 탐색
            result = BOX[i+1][j] + BOX[i-1][j] + BOX[i][j+1] + BOX[i][j-1] - BOX[i][j] # 결과값은 상하좌우에서 내 위치의 점수 빼기
            if result > 0:  # 음수면 보너스 점수가 0이 되기에 상관 x
                if result % 2 == 0: # 짝수이면 result는 2배의 점수가 되고 값 비교 진행
                    result *= 2
                    if result > max_result: # 값 비교하여 최댓값으로 교체
                        max_result = result
                else:   # 홀수라면 그냥 값 비교 진행
                    if result > max_result:
                        max_result = result

    print(f'#{test} {max_result}')