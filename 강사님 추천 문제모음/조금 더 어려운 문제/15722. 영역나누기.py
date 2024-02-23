
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 987654321  # 영역 합의 최대값 - 최소값의 차이가 가장 적은 경우

    for i in range(N - 1):              # 모든 점을 순회하며 A영역 가장 오른쪽 아래 인덱스 구하기
        for j in range(N - 1):          # 4가지 영역을 만들어야하니 아래, 오른쪽 가장자리는 비운다.
            max_area = 0                    # 영역 중 가장 큰 영역의 값
            min_area = 987654322            # 영역 중 가장 작은 영역의 값
            A, B, C, D = 0, 0, 0, 0         # A, B, C, D 영역을 0으로 설정

            for x in range(N):              # 구한 인덱스를 기준으로 영역 4개로 분리
                for y in range(N):
                    if x <= i and y <= j:   # A영역 내 숫자의 합
                        A += arr[x][y]
                    elif x <= i and y > j:  # B영역 내 숫자의 합
                        B += arr[x][y]
                    elif x > i and y <= j:  # C영역 내 숫자의 합
                        C += arr[x][y]
                    elif x > i and y > j:   # D영역 내 숫자의 합
                        D += arr[x][y]

            max_area = max(A, B, C, D)      # 영역 중 최대값 구하기
            min_area = min(A, B, C, D)      # 영역 중 최소값 구하기
            minus = max_area - min_area     # 최대값 - 최소값 구하기

            if result > minus:              # 해당 값이 가장 작으면 그걸 result로
                result = minus
    
    print(f'#{test_case} {result}')

                    