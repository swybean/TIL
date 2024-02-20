T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = 987654321

    for i in range(len(arr)):
        if min_num > i:
            min_num = i
    
    for 