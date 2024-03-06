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
        if arr[i] <= arr[i+1]:     
            buy_price += arr[i]  
            num_buy += 1           
 
        elif arr[i] > arr[i+1]:      
            for j in range(i, i+1):
                # 현재 가격(arr[i])이 남은 arr[i] 중 최고가격일때만 지금까지 구매한거 다 팔자 
                if arr[j] == max_price:
                    profit += (num_buy * arr[i]) - buy_price  
                    buy_price = 0              
                    num_buy = 0
                    break       
 
                # i+1이 남은 arr[i] 중 최고가격이 아니면 팔지말고 해당 상품도 매수해
                else:
                    buy_price += arr[i]         
                    num_buy += 1
                    break   
 
    # 마지막 날에 상품을 모두 판매한 경우를 처리
    profit += num_buy * arr[N-1]
    max_profit += profit - buy_price
     
    print(f'#{test_case} {max_profit}')


