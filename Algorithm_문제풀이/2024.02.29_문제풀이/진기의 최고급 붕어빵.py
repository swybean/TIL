'''
모든 손님에게 붕어빵을 대기시간 없이 팔 수 있는지 판별하는 프로그램을 함수로 만들 것이다.



'''

def start():
    sold_bread = 0  # 팔린 빵
    for person in customers:
        # 공식, 특정시간에 만들 수 있는 빵의 개수
        made_bread = (person // M) * K

        # 빵을 1개 팔았다
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread

        # 재고가 0보다 작으면 실패
        if remain < 0:
            return 'Impossible'
    # 실패가 없었으면 성공
    return 'Possible'


T = int(input())
for test_case in range(1, T+1):
    # 손님수 N, M초에 K개의 빵을 만든다. 손님들이 도착하는 시간 customesr
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))

    customers.sort()    # 손님이 오는 순서는 적은 시간부터니까 오름차순 정렬
    result = start()
    print(f'#{test_case} {result}')
