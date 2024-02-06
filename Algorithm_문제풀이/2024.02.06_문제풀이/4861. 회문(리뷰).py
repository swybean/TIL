import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = '' # 회문인 문자열을 저장할 변수

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result = arr[i][j:j+M]
                break   # for j문을 종료시키는 break
        else:
            continue
        break

    for i in range(N-M+1):
        for j in range(N):
            vertical = ''
            for x in range(i, i+M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result = vertical
                break
        else:
            continue
        break
    print(f'#{tc} {result}')

