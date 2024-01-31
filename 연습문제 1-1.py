N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

for i in range(N):
    total += arr[i][i]  # 오른쪽 아래 대각선
    total += arr[i][N-1-i]
if N % 2:   # 크기가 홀수인 경우
    total -= arr[N//2][N//2]    # 중심원소가 중복되므로
print(total)


'''
입력값은 아래와 같다.
5
5 4 2 1 1
3 7 9 7 7
4 3 5 7 5
6 9 3 6 1
2 2 1 6 2
'''