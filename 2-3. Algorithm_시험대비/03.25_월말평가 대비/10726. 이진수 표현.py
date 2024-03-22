


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    ans = 'OFF'

    if M & ((1 << N) - 1) == ((1 << N) - 1):
        ans = 'ON'

    print(f'#{test_case} {ans}')