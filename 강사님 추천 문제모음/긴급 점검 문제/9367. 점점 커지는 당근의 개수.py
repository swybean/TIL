
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(N-1):
        counts = 0
        if arr[i] < arr[i + 1]:
            counts += 1
            i = i + 1
            if result < counts:
                result = counts
        else:
            counts = 0
    print(f'#{test_case} {result}')









