'''
3
3 8 
7 7 
369 123
'''

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))

    result = ''
    num_1, num_2, = N

    if num_1 > num_2:
        result = '>'
    if num_1 < num_2:
        result = '<'
    if num_1 == num_2:
        result = '='
    
    print(f'#{test_case} {result}')



