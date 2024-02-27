T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    buy_price = 0       # 구매한 상품의 총 가격
    num_buy = 0         # 구매해서 보유하고 있는 상품 개수
    profit= 0           # 현재 이익
    max_profit = 0      # 최대 이익

    for i in range(N-1):
        if arr[i] <= arr[i+1]:          # 현재 가격이 다음 가격보다 작으면 구매
            buy_price += arr[i]         # 구매가에 현재 가격 추가
            num_buy += 1                # 구매한 상품 수 1 증가

        elif arr[i] > arr[i+1]:         # 현재 가격이 다음 가격보다 크면 판매
                                        # 현재이익 = (구매수 x 현재 가격) - 구매가 총합
            profit += (num_buy * arr[i]) - buy_price  
            buy_price = 0               # 구매한 상품 가격 초기화
            num_buy = 0                 # 구매해서 보유하고 있는 상품 개수 초기화

    # 마지막 날에 상품을 모두 판매한 경우를 처리
    profit += num_buy * arr[N-1]
    max_profit += profit - buy_price
    
    print(f'#{test_case} {max_profit}')


'''
예시: 1 1 3 1 2
가격 배열이 주어진다고 하면
i를 반복순회한다
i가 i+1보다 작다면 산다.
근데 위 예시처럼 같아도 사야 되는 경우가 있다
근데 같아도 산다고 했는데  1 1 1 1 1이면 ?
그냥 1 1 1 1까지 사고 마지막 1에 1에 다 팔고 최대 이익은 0으로?
일단 여기까지 코드로 시작

예시 테케는 다맞는데 
제출하면 테케 10개 중 2개 맞는다고 뜸....
'''

