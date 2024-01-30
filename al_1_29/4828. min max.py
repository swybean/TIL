T = int(input())

for test_case in range(1, T+1):

    a = int(input())
    b = list(map(int, input().split()))
    max_num = 0
    min_num = 1000000
    for x in b:
        if max_num < x:
            max_num = x
    for y in b:
        if min_num > y:
            min_num = y
    print(f'#{test_case} {max_num - min_num}')
