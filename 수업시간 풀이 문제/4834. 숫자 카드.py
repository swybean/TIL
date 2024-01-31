T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))

    counts = [0] * 10


    for i in range (0, N):
        counts[arr[i]] += 1

    big_num = 0
    number = 0

    for j in range(10):
        if counts[big_num] <= counts[j]:
            number = counts[j]
            big_num = j
            
    print(f'#{test_case} {big_num} {number}')





