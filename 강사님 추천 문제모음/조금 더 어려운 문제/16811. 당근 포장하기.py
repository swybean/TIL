'''
조건1 : 당근을 소, 중, 대로 구분한다.
조건2 : 같은 크기 당근은 같은 상자
조건3 : 비어 있는 상자는 없다
조건4 : 한상자에 최대 당근 수는 N/2개 초과 불가능(이하여야한다. 홀수면 소수점 버림)
조건5 : 각 상자의 당근 수가 최소가 되어야 한다.
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()       # 당근을 크기 순서로 정렬시키기
    result = 987654321  # 당근 개수 차이 최소값 저장할 변수    

    # 조건3을 만족시키기 위해 끝에 2개는 남겨놔야 중, 대 상자에도 최소 1개는 들어간다.
    for i in range(N-2):
        for j in range(i+1, N-1):
            # 조건2를 만족시키기 위해 전 상자의 끝과 다음 상자의 시작 당근은 달라야 한다.
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                # 소, 중, 대 상자의 범위 설정
                small_box = len(carrot[:i+1])
                middle_box = len(carrot[i+1:j+1])
                big_box = len(carrot[j+1:N])
                # 조건4를 만족 시키기 위해 모든 상자는 N//2보다 작거나 같아야 함
                if small_box <= N//2 and middle_box <= N//2 and big_box <= N//2:
                    # 조건5를 만족시키기 위한 minus 값 생성
                    # max, min을 이용해서 가장 큰 상자 - 가장 작은 상자 값을 minus로 한다.
                    minus = max(small_box, middle_box, big_box) - min(small_box, middle_box, big_box)
                    # 가장 큰 상자 - 가장 작은 상자가 result보다 작으면 result 값을 변경한다.
                    if result > minus:
                        result = minus
    # 모든 i, j 경우의 수를 돌았음에도 모든 조건에 만족하는 경우가 없어 result가 그대로 987654321이라면 -1로 변경
    if result == 987654321:
        result = -1

    # 결과 출력
    print(f'#{test_case} {result}')

