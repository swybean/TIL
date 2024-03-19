'''
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어진다.
배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 
예를 들어, 다음은 N=5인 지역의 높이 정보이다.
물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 
위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다.

어떤 지역의 높이 정보가 주어졌을 때, 
장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
N은 2 이상 100 이하의 정수이다. 
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다.
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
높이는 1이상 100 이하의 정수이다.

첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
'''
 


def dfs(i, j):
    global num_angun
    global r

    if arr[i][j] > 0:
        if arr[i][j] > r:
            num_angun += 1
            arr[i][j] = 0

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    dfs(ni, nj)
            return num_angun
    return


# 4방향 델타 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]   

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

r = 0   # 강수량
result = 0
num_angun = 0

while r < 101:
    r += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > r:
                dfs(i, j)
                if result < num_angun:
                    result = num_angun
                num_angun = 0

print(result)





'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

6
'''