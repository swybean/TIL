import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 문장 개수와 길이 / M은 부분적으로 조사할 길이
    arr = [input() for _ in range(N)]
    result = ''    
# 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j: j+M] == arr[i][j: j+M][::-1]: 
                result = arr[i][j : j+M]   
                break #
        else:
            continue  
        break 

# 세로 탐색
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



