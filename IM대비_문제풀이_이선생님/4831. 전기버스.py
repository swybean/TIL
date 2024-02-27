T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())     
    # K는 최대 이동가능한 정류장 수, N은 종점 정류장 번호, M은 충전기가 설치된 정류장 수
    charge = list(map(int, input().split()))   # 충전기가 설치된 정류장 번호 
    
    bus_stop = [[0] * (N+1)] # 모든 정류장 리스트
    for i in charge:            # 정류장 중 충전기가 있는 정류장에 1 표시
        bus_stop[i]  = 1

    bus = 0     # 버스의 현재 위치(시작위치는 0번 시작 정류장으로 해야 한다.)
    count = 0   # 충전 횟수

    while bus + K < N:  # 마지막 충전 이후 종점에 도착하지 못한다면
        last = 0        # 버스의 마지막 위치

        # 현재위치(bus+1)와 한번충전으로 갈 수 있는 최대거리(bus+1+K) 사이에서 충전기 위치 i 찾기
        for i in range(bus+1, bus+1+K): 
            if bus_stop[i]:     # i 정류장에 충전기가 있다면
                last = i        # 버스의 마지막 위치는 i로 변경
        
        # 마지막 위치에 충전기가 없다면 정지 갈 수 없음
        if last == 0:
            count = 0
            break
        # 마지막 위치에 충전기가 있다면
        else:
            bus = last  # last를 버스의 현재 위치로 설정
            count += 1  # 충전횟수 +1
    
    print(f'#{test_case} {count}')


