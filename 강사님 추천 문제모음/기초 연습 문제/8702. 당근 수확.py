T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mini = 9876543210   # 두 구역의 차이의 최소값
    dang = 0            # 잘린 두 구역 중 첫번째 구역의 마지막 인덱스 번호

    for i in range(1, N):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        carrot = abs(left_sum - right_sum)

        if carrot < mini:
            mini = carrot
            dang = i

    print(f'#{tc} {dang} {mini}')

