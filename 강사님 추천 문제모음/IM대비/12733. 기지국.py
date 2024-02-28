'''
기지국 = A, B, C
A = 1, B = 2, C = 3 칸씩 커버가 가능한 기지국이라는 뜻

N = 9
인 경우로 연습
'''



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 