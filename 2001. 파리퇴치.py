di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
'''
모든 경우의 수에 대해서 조사해야 한다.

'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nemo = [[0] * 5 for _ in range(5)]
