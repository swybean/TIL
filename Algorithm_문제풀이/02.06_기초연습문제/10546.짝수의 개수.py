import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    num = 0

    for i in range(N):
        if arr[i] % 2 == 0:
            num += 1

    print(f'#{tc} {num}')





