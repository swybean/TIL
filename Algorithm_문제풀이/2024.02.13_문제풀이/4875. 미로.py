'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 시작위치 찾기 함수
def find_start_pos(N, arr):         # 미로 크기 N, 미로 입력 받기
    for i in range(N):              # 미로의 모든 행 i를 반복하기
        if 2 in arr[i]:             # 만약 해당 i행에 2가 있다면
            for j in range(N):      # i행에서 열 j를 반복하기
                if arr[i][j] == 2:  # 만약 시작위치인 2를 찾았다면
                    return i, j     # 시작 위치의 행, 열인 i, j를 반환
                
# 길찾기 함수
def maze(N, arr):
    stack = []  # 빈 스택 생성
    i, j = find_start_pos(N, arr)   # 시작위치 찾기 함수 사용

    # 갈 수 있는 곳으로 가기 (무한루프 시작)
    while True:
        # 4방향 이동할 수 있는지 확인하기 위해 방향을 순회하자
        for dir in range(4):
            # 미로 범위 내에서 안 벗어나는지 확인하기
            if 0 <= i + di[dir] < N and 0 <= j + dj[dir] < N:
                # 이동한 곳이 도착점이라면 1을 반환
                if arr[i + di[dir]][j + dj[dir]] == 3:
                    return 1
                # 이동한 곳이 갈 수 있는 길(0)이라면
                if arr[i + di[dir]][j + dj[dir]] == 0:
                    # 근데 스택이 비어있다면 
                    # (초기 위치에서 처음 이동할 때만 쓰는 조건)
                    if len(stack) == 0:
                        stack.append([i, j])    # 현재 위치를 스택에 담기
                        i, j = i + di[dir], j + dj[dir] # 다음 위치로 이동하기
                        break
                    # 스택이 비어있지 않고, 이동한 위치가 이전에 방문하지 않은 곳이라면
                    # (탐색 중인 상태에서 새로운 경로를 탐색하기 위한 조건)
                    elif stack and stack[-1] != [i + di[dir], j + dj[dir]]:
                        stack.append([i, j])    # 현재 위치를 스택에 담고
                        i, j = i + di[dir], j + dj[dir] # 다음 위치로 이동하자
                        break
        # 4방향으로 이동한 후에도 갈 곳이 없으면
        else:
            if stack:   # 스택이 비어있지 않으면
                arr[i][j] = 1       # 현재 위치를 벽으로 바꾸고 (이 길을 앞으로 다시 안가기 위해)
                i, j = stack.pop()  # 이전 위치로 이동해
            else:       # 스택이 비어있고, 현재 위치가 시작 위치라면
                return 0            # 탐색할 수 없는 미로니까 0을 반환해

# 입력 및 출력
T = int(input())
for test_case in range(1, 1+T):
    N = int(input())    # 미로 크기 N 입력
    arr = [list(map(int,input())) for _ in range(N)]    # 미로 입력
    
    print(f'#{test_case} {maze(N, arr)}')   # 답 출력



    