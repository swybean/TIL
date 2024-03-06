import sys
sys.stdin = open('input4.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]

    result = 0 # 회문인 문자열의 수 저장할 변수

    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                result += 1

    for i in range(8-N+1):
        for j in range(8):
            vertical = ''
            for x in range(i, i+N):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result +=1

    print(f'#{tc} {result}')




