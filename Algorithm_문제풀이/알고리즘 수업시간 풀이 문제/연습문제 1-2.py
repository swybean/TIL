di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] # 5x5 2차 배열에 25개의 숫자를 저장하고
total = 0
for i in range(N): # 25개의 각 요소에 대해서  arr[i][j]
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni][nj] - arr[i][j])  # 차의 절대값을 구하시오, 총합을 구하시오.

print(total)