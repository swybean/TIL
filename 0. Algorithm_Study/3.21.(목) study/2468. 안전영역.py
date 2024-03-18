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


        

def dfs(i, j, h):
    global visited
    visited[i][j] = True
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and area[ni][nj] > h:
            dfs(ni, nj, h)

N = int(input())  # 지역의 크기
area = [list(map(int, input().split())) for _ in range(N)]  # 지역의 높이 정보

di = [-1, 1, 0, 0]  # 상하좌우 이동
dj = [0, 0, -1, 1]

result = 0  # 결과값

# 높이별로 안전한 영역의 개수 구하기
for h in range(101):  # 높이는 1부터 100까지 가능
    visited = [[False] * N for _ in range(N)]  # 방문 여부 초기화
    safe_count = 0  # 안전한 영역 개수
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > h:
                dfs(i, j, h)
                safe_count += 1
    result = max(result, safe_count)  # 최대값 갱신

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