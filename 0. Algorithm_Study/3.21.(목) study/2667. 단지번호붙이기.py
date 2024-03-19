'''
첫째줄에 총 단지수를 출력하시오. 
각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''
def dfs(i, j):
    global cnt
    if arr[i][j] == 1:
        cnt += 1
        arr[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                dfs(ni, nj)
        return cnt
    return 0

# 4방향 델타 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]    

N = int(input())    # 정사각형 크기 N
arr = [list(map(int, input())) for _ in range(N)]   # 배열 입력하기
cnt = 0     # 집의 개수

danji_num = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            danji_num.append(dfs(i, j))
            cnt = 0

danji_num.sort()

print(len(danji_num))   
for i in danji_num:     
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

'''
def dfs(i, j):
    if arr[i][j] == 1:
        house_num = 1   # 단지 내 집의 수
        arr[i][j] = 0

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                house_num += 1
                dfs(ni, nj)
        return house_num
    return 0


'''
