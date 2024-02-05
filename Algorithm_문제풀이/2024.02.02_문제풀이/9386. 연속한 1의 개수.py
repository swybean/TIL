T = int(input())
 
for tc in range(T):
    N = int(input())
    num_list = input()
 
    num_max = 0
    temp = 0
 
    for i in num_list:
        if int(i) == 1:
            temp += 1
        elif int(i) == 0:
            temp = 0
 
        if num_max < temp:
            num_max = temp
 
    print(f'#{tc+1} {num_max}')

    