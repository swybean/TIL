di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 시작위치 찾기 함수
def find_start_pos(N, arr):
    for i in range(N):
        if 2 in arr[i]:
            for j in range(N):
                if arr[i][j] == 2:
                    return i, j
                
# 길찾기 함수
def maze(N, arr):
    stack = []  
    i, j = find_start_pos(N, arr) 

    while True:
        for dir in range(4):
            if 0 <= i + di[dir] < N and 0 <= j + dj[dir] < N:
                if arr[i + di[dir]][j + dj[dir]] == 3:
                    return 1
                if arr[i + di[dir]][j + dj[dir]] == 0:
                    if len(stack) == 0:
                        stack.append([i, j])    
                        i, j = i + di[dir], j + dj[dir]
                        break
                    elif stack and stack[-1] != [i + di[dir], j + dj[dir]]:
                        stack.append([i, j])    
                        i, j = i + di[dir], j + dj[dir] 
                        break
        else:
            if stack:  
                arr[i][j] = 1     
                i, j = stack.pop() 
            else:     
                return 0         

T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    
    print(f'#{test_case} {maze(N, arr)}')