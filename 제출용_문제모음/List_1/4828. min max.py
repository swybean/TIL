T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minnum = 9999999
    maxnum = 0
    for i in arr:
        if i > maxnum:
            maxnum = i
        if i < minnum:
            minnum = i
        result = maxnum - minnum
    print(f'#{tc} {result}')































