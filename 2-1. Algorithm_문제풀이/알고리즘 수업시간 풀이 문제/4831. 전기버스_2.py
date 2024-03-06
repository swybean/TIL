T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K: 충전당 이동거리, N: 종점까지 총 정류장 수, M: 충전기 설치 된 정류장
    charger = [0] + list(map(int, input().split())) + [N]   # 충전기 설치 정류장 번호

    last = 0    # 마지막 충전 위치, 초기값은 출발점 0 (정확한 표현은 0 대신 charger[0])
    count = 0   # 충전 횟수
    for i in range(1, M + 2):   # 모든 충전기 위치 charger[i]에 대해...
        if (charger[i] - charger[i - 1]) <= K:      # 충전기 사이 운행 가능하면
            if (charger[i] - last) > K:    # 마지막 충전기에서 너무 멀면
                last = charger[i -1]
                count += 1
        else:
            count = 0
            break
    print(f'#{test_case} {count}')







