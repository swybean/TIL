import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nemo = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        arr = list(map(int, input().split()))
        A1, A2, B1, B2, color = arr
        for i in range(A1, B1 + 1):
            for j in range(A2, B2 + 1):
                nemo[i][j] += color
    
    color_bora = 0

    for r in range(10):
        for c in range(10):
            if nemo[r][c] == 3:
                color_bora += 1

    print(f'#{test_case} {color_bora}')