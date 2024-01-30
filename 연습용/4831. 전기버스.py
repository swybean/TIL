T = int(input())

for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))  
    # K: 충전당 이동거리, N: 종점까지 총 정류장 수, M: 충전기 설치 된 정류장
    charger = list(map(int, input().split()))   # 충전기 설치 정류장 번호
    
    # 충전기가 있는지 정류장별로 표시
    bus_stop = [0] * (N+1)  
    for x in charger:
        bus_stop[x] = 1
    
    # k 범위 내에서 가장 먼 충전기를 찾으면 count += 1, bus도 해당위치로 변경
    bus = 0     # 버스의 현재 위치
    count = 0   # 충전 횟수
    while bus + K < N:  # 마지막 충전 이후 종점에 도착할 수 없다면...
        last = 0
        for i in range(bus + 1, bus + K + 1):   # bus -> bus+K 사이 마지막 충전기 위치 i 찾기
            if bus_stop[i]:     # i정류장에 충전기가 있으면
                last = i
        # 충전기가 없으면
        if last == 0:
            count = 0
            break
        # 충전기가 있으면 (운행 가능한 최대 거리이내의 마지막 충전기)
        else:
            bus = last
            count += 1

    print(f'#{test_case} {count}')







