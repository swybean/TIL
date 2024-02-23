
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_carrot = 0
    carrots = 1

    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            carrots += 1
        else:
            carrots = 1

        if max_carrot < carrots:
                max_carrot = carrots  

    print(f'#{test_case} {max_carrot}')




