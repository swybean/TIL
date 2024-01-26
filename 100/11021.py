T = int(input())
 
for test_case in range(1, T + 1):
    numbers = [int(x) for x in input().split()]
 
    odd_sum = sum(numbers)
 
    print(f'Case #{test_case}: {odd_sum}')

