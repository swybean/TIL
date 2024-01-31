



T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    
    all_num = 0
    number = 0

    for num in N:
        all_num += num
        number += 1
        result = all_num // number
    print(f'#{test_case} {result}')












