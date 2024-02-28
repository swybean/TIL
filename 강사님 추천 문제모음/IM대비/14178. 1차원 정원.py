T = int(input())

for test_case in range(1, T+1):
    N, D = map(int, input().split())    # N은 꽃밭 길이, D는 분무기 범위값
    water = (2 * D) + 1 # 분무기의 범위, 양쪽 D만큼이니까 D*2, 가운데 1칸
    
    num_water = 0       # 필요한 분무기 개수
    # 꽃밭을 분무기 범위로 나눴는데 딱 떨어지면 해당 값이 필요한 개수
    if N % water == 0:
        num_water = (N // water)
    # 꽃밭을 분무기 범위로 나눴는데 딱 떨어지지 않고 나머지가 있으면 분무기 한개를 더 써야됨
    else:
        num_water = (N // water) + 1
    
    print(f'#{test_case} {num_water}')