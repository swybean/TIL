




T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())     
    num = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if num[i] > num[j]:
             num[i], num[j] = num[j], num[i]   

    for i in range(N):
        for j in range(i + 1, N):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
        new_list= num   


    num_2 = num[:(N/2 - 1)]
    new_list_2 = new_list[:(N/2 - 1)]      

    result_list = [new_list_2[0], num_2[0], 
                   new_list_2[1], num_2[1],
                   new_list_2[2], num_2[2],
                   new_list_2[3], num_2[3],
                   new_list_2[4], num_2[4]]

    print(result_list)

'''
num_lsit = 1 2 3 4 5 6 7 8 9 10
new_list = 10 9 8 7 6 5 4 3 2 1

N의 1/2만큼씩 리스트를 자른다.
N이 10이면 인덱스4
N이 20이면 인덱스9
즉, 인덱스 (N / 2 - 1)까지만 리스트를 다시 저장
num_lsit = 1 2 3 4 5
new_list = 10 9 8 7 6

양 리스트의 인덱스 순서대로 하나씩 번걸아 새로운 리스트에 넣는다.
(순서는 new_list부터)

result_list = 10 1 9 2 8 3 7 4 6 5
'''




    # for i in range(N):
    #     for j in range(i + 1, N):
    #         if new_list[i] < new_list[j]:
    #          new_list[i], new_list[j] = new_list[j], new_list[i]








