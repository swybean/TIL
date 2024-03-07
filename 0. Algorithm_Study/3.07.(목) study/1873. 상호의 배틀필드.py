# 포탄 쏘는 함수
def shoot():
    for x in range(H):
        for y in range(W):
            if map_arr[x][y] in '><^v':
                if map_arr[x][y] == '<':
                    di, dj = [0, -1]
                elif map_arr[x][y] == 'v':
                    di, dj = [1, 0]
                elif map_arr[x][y] == '>':
                    di, dj = [0, 1]
                elif map_arr[x][y] == '^':
                    di, dj = [-1, 0]
                for p in range(1, W):
                    ni = x + di * p
                    nj = y + dj * p
                    if 0 <= ni < H and 0 <= nj < W:
                        if map_arr[ni][nj] == '#':
                            return
                        elif map_arr[ni][nj] == '*':
                            map_arr[ni][nj] = '.'
                            return

# 이동 동작 함수
def move(i):
    for x in range(H):
        for y in range(W):
            if map_arr[x][y] in '<v^>':
                if i == 'L':
                    di, dj = [0, -1]
                    map_arr[x][y] = '<'
                    ni = x + di
                    nj = y + dj
                    if 0 <= nj < W:
                        if map_arr[ni][nj] == '.':
                            map_arr[ni][nj] = '<'
                            map_arr[x][y] = '.'    
                            return                     

                elif i == 'R':
                    di, dj = [0, 1]
                    map_arr[x][y] = '>'                        
                    ni = x + di
                    nj = y + dj
                    if 0 <= nj < W:
                        if map_arr[ni][nj] == '.':
                            map_arr[ni][nj] = '>'
                            map_arr[x][y] = '.'
                            return  
       
                elif i == 'U':
                    di, dj = [-1, 0]       
                    map_arr[x][y] = '^'
                    ni = x + di
                    nj = y + dj
                    if 0 <= ni < H:
                        if map_arr[ni][nj] == '.':
                            map_arr[ni][nj] = '^'
                            map_arr[x][y] = '.'                        
                            return  
                
                elif i == 'D':
                    di, dj = [1, 0]
                    map_arr[x][y] = 'v'    
                    ni = x + di
                    nj = y + dj
                    if 0 <= ni < H:
                        if map_arr[ni][nj] == '.':
                            map_arr[ni][nj] = 'v'
                            map_arr[x][y] = '.'                          
                            return  

T = int(input())
for test_case in range(1, T+1):
    H, W = map(int, input().split())                # 맵의 높이H, 맵의 너비W
    map_arr = [list(input()) for _ in range(H)]     # 맵 배열 입력
    N = int(input())                                # 입력의 개수 N
    move_arr = list(input())                        # 이동명령값들 입력


    for i in move_arr:
        if i in 'S':
            shoot()
        elif i in 'UDRL':
            move(i)
    
    print(f'#{test_case}', end=' ')
    for i in range(H):
        print(''.join(map_arr[i]))


'''
탱크의 시작위치를 정하고 시작하자
전체 탐색 i,j 로 arr[i][j]구하고
i, j = it, jt

like 오셀로
'''


'''
맵 배열 문자
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

전차동작 문자
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.    
'''


