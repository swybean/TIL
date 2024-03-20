





T = int(input())
for test_case in range(1, T+1):
    num, N = input().split()

    card = list(num)    # 주어진 숫자판 리스트
    N = int(N)          # 교환 가능 횟수
    max_v = 0           # 최대상금

    memo = [0]*(10**len(card))  # 

    print(f'#{test_case} {max_v}')












