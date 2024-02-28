# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     price = list(map(int, input().split()))
#     maxprice = [0] * N
#     total = 0
 
#     # 마지막부터 역순으로 각 날짜 이후의 최대 가격 찾기
#     maxprice[N - 1] = price[N - 1]
#     for i in range(N - 2, -1, -1):
#         maxprice[i] = price[i] if price[i] > maxprice[i + 1] else maxprice[i + 1]
#         total += maxprice[i] - price[i]
 
#     print(f'#{test_case} {total}')


# 풀다가 포기 일단 다른 문제부터 풀어야함 for문으로 푸는건 나~중에
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    buy_price = 0           # 구매한 상품의 총 가격
    num_buy = 0             # 구매해서 보유하고 있는 상품 개수
    profit= 0               # 현재 이익
    max_profit = 0          # 최대 이익
    max_price = max(arr)    # arr 중 최고가격
 
    for i in range(N-1):
        if arr[i] <= arr[i+1]:       # 현재 가격이 다음 가격보다 작으면 구매
            buy_price += arr[i]      # 구매가에 현재 가격 추가
            num_buy += 1             # 구매한 상품 수 1 증가
 
        elif arr[i] > arr[i+1]:      # 현재 가격이 다음 가격보다 크면 판매할건데 아래 조건에 만족해야함
            for j in range(i, i+1):
                # 현재 가격(arr[i])이 남은 arr[i] 중 최고가격일때만 지금까지 구매한거 다 팔자 
                if arr[j] == max_price:
                    profit += (num_buy * arr[i]) - buy_price  
                    buy_price = 0              
                    num_buy = 0
                    max_price = max(arr[j+1:])
                    break   # 판매한 후 for j문 탈출하고 다시 for i문으로 돌아가서 마저 반복         
 
                # i+1이 남은 arr[i] 중 최고가격이 아니면 팔지말고 해당 상품도 매수해
                else:
                    if arr[i] != max(arr[i+1:]):    # 만약 계속 가격이 줄어드는 중이라 구매한게 없다면 안사기 위한 조건
                        buy_price += arr[i]         
                        num_buy += 1
                        max_price = max(arr[j+1:])
                        break    # 구매하고 for j문 탈출하고 다시 for i문으로 돌아가서 마저 반복
 
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

10 7 6 일때 오류남
10에서 안사는데
7일때 else문으로 넘어가서 buy_price, num_buy에 값을 추가하고
6일때는 #마지막날로 넘어가서 위에서 저장된 가격으로 max_profit을 구해서 -1이 나옴

'''