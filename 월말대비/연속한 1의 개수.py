T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    counts = 0
    ans = 0

    for i in range(N):
        if arr[i] == 1:
            counts += 1
            if counts > ans:
                ans = counts

        if arr[i] != 1:
            counts = 0
    print(f'#{test_case} {ans}')

