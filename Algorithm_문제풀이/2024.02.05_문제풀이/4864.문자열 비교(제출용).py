import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        num = 1
    else:
        num = 0

    print(f'#{tc} {num}')