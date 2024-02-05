def algo1(n, arr):

    # 상하좌우 조회할 수 있도록 돕는 dx, dy 선언
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 최종 반환할 값인 ans의 기본값은 0점
    ans = 0

    # 첫 번째 행과 열, n번째 행과 열을 제외한 arr에 사격을 한다.
    # (상하좌우 중 하나라도 arr를 벗어나면 0점이기 때문에 고려할 필요가 없음)
    for i in range(1, n-1):
        for j in range(1, n-1):

            # 상하좌우의 값을 temp에 합산
            temp = 0
            for d in range(4):
                temp += arr[i+dx[d]][j+dy[d]]

            # 합산한 결과에서 맞춘 좌표의 점수를 뺀다.
            sum_score = temp - arr[i][j]

            # 그 점수가 짝수이면 *2 (음수인 경우는 0점이기 때문에 고려하지 않는다)
            if sum_score % 2 == 0 and sum_score > 0:
                sum_score *= 2

            # 최종 점수가 ans보다 크면 ans = 최종 점수
            if ans < sum_score:
                ans = sum_score

    # 최종 점수가 음수인 경우와 가장자리 칸을 맞춘 경우만 존재한다면 기본 값인 ans = 0이 반환된다.
    return ans


T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case} {algo1(n, arr)}')
