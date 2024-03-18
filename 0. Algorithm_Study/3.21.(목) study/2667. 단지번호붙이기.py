'''
첫째줄에 총 단지수를 출력하시오. 
각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''


N = int(input())    # 정사각형 크기 N
arr = [list(map(int, input())) for _ in range(N)]   # 배열 입력하기

# 4방향 델타 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# dfs 함수 제작
def dfs(i, j):
    if arr[i][j] == 1:  # 1인 곳을 찾으면
        arr[i][j] = 0   # 0으로 만들고
        num_dangi = 1   # 단지수를 1로 설정

        for k in range(4):  # 해당 위치에서 4방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 4방향 중 다음위치가 1이라면 이동하고 단지수 추가 및 재귀 함수
                num_dangi += dfs(ni, nj)     
        # 모든 곳을 순회하면 단지수 반환
        return num_dangi
    # 1인 곳이 없으면 0 출력 (집이 아예 없는 경우)
    return 0

groups = []
for i in range(N):
    for j in range(N):
        # arr 중 1인 곳을 찾으면
        if arr[i][j] == 1:
            # dfs함수에 집어넣고 단지 내 집의 수를 구하여 그룹에 추가
            groups.append(dfs(i, j))

groups.sort()  # 집의수 오름차순 정렬

print(len(groups))  # 단지 수 출력
for i in groups:    # 각 단지의 집의 개수 오름차순으로 출력
    print(i) 


                    



'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
'''


