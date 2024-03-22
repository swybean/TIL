'''
4x4 격자판
-> 이차원 배열을 사용해야 한다.

동서남북 네 방향으로 총 여섯 번 이동한다
-> 방향 배열을 사용해야 한다.

"특정 시점"에서 나올 수 있는 결과가 "두 가지"네?
-> 재귀 사용해야 한다.


풀이 순서
1. 재귀
-> 숫자 이어붙이기

2. 7자리까지 반복

3. 중복 제거
-> set, dict 사용하기


경우의 수가 4000몇가지이기 때문에 단순 재귀로 풀어도 된다.

'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, path):
    # 기저 조건 : 7자리면 끝
    if len(path) == 7:
        # 현재까지의 경로를 저장
        result.add(path)
        return

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        # 범위 밖으로 넘어가면 pass
        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue
    
        dfs(new_y, new_x, path + maps[new_y][new_x])

T = int(input())
for test_case in range(1, T+1):
    # 격자판 저장
    # 갈 때 마다 경로를 더하기 위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해 set 사용
    result = set()

    # 시작 지점
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{test_case} {len(result)}')





'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''

