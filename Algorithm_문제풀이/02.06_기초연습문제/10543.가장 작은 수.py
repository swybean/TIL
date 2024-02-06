# import sys
# sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    
    min_num = max(arr)
    # print(min_num)

    for i in arr:
        if i < min_num:
            min_num = i
            result = arr[min_num]

    print(result)
            

