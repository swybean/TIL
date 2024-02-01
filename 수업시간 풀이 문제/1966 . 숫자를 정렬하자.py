

T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())     

    num_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if num_list[i] > num_list[j]:
             num_list[i], num_list[j] = num_list[j], num_list[i]


    print(f'#{test_case}', *num_list)

    