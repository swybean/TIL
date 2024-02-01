'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''



T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    
    all_num = 0
    number = 0

    for num in N:
        all_num += num
        number += 1
        result = all_num / number
    print(f'#{test_case} {round(result)}')












