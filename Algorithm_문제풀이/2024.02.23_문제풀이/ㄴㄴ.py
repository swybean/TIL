## 당근수확4
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    result = [0] * 4
 
    for i in range(N):
        for j in range(N):
            if i > j and i+j<N-1:
                result[0] += Board[i][j]
            elif i > j and i+j>N-1:
                result[1] += Board[i][j]
            elif i < j and i+j>N-1:
                result[2] += Board[i][j]
            elif i < j and i+j<N-1:
                result[3] += Board[i][j]
 
    print(f'#{testcase} {max(result)-min(result)}')