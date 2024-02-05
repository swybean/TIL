def algo2(n, k, num_list):

    cnt = 0     # 몇 번째 점프인지 카운트
    now = 0     # 현재 위치 표시
    ans = 0     # 연잎 수를 합산할 변수
    pre = 0     # 이전 연잎 숫자 저장 (기본값 = 0)

    # k번 점프를 다 하거나, 현재 위치가 연잎 범위를 벗어날 때 까지 반복
    while cnt <= k and 0 <= now < n:

        # 시작했을 때를 제외하고, 현재 위치의 연잎의 수를 합산
        if cnt > 0:
            ans += num_list[now]

        # 현재 위치의 연잎 수 = 다음 점프할 거리
        jump = num_list[now]

        # case 1. 다음 점프할 거리가 음수인 경우
        # 현재 위치에 다음 점프할 거리를 합산하여 다음 위치 생성
        # 현재 연잎의 수를 pre에 저장 -> 다음 점프할 거리가 양수가 됐을 때 이용
        if jump < 0:
            now += jump
            pre = jump

        # case 2. 다음 점프할 거리가 양수인 경우
        # 현재 위치, 다음 점프할 거리, 이전 뒤로갔던 거리를 합산하여 다음 위치 생성
        # pre 값 초기화
        else:
            now += jump - pre
            pre = 0

        # 점프 횟수 카운트
        cnt += 1

    return ans


T = int(input())
for case in range(1, T+1):
    # n : 연잎의 개수 / k : 점프 횟수
    n, k = map(int, input().split())
    # 연잎들
    num_list = list(map(int, input().split()))

    print(f'#{case} {algo2(n, k, num_list)}')