T = int(input())

for test_case in range(1, T+1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    N = a[0]
    M = a[1]

    total1 = sum(b[-1:M-1:-1])
    total2 = sum(b[0:M])
    
    print(f'#{test_case} {total2 - total1}')


