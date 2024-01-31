T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    number = 0
    for num in N:
        if num > number:
            number = num


    print(f'#{test_case} {number}')




