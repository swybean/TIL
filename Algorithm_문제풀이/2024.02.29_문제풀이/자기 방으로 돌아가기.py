

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 복도리스트 초기화
    corridor = [0] * 400
    max_v = 0

    for _ in range(N):
        # 현재방 s, 돌아갈방e
        S, E = map(int, input().split())

        # 특징 2번 아랫방을 윗방으로 변경
        if S % 2 == 0:
            S -= 1
        if E % 2 == 0:
            E -= 1
        
        # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swqp
        if S > E:
            S, E = E, S # swqp

        for i in range(S, E+1):
            corridor[i] += 1
            max_v = max(corridor[i], max_v)

    print(f'#{test_case} {max_v}')



