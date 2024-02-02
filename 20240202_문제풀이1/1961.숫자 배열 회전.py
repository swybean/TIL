def degree_270(list, N):
    result = []
    for j in range(N-1,-1,-1):
        one_line = []
        for k in range(0,N):
            one_line.append(list[k][j])
        result.append(one_line)
    return result
 
def degree_180(list, N):
    result = []
    for j in range(N-1,-1,-1):
        one_line = []
        for k in range(N-1,-1,-1):
            one_line.append(list[j][k])
        result.append(one_line)
    return result
 
def degree_90(list, N):
    result = []
    for j in range(0,N):
        one_line = []
        for k in range(N-1,-1,-1):
            one_line.append(list[k][j])
        result.append(one_line)
    return result
 
def change_matrix(list, N):
    result = []
    for j in range(0,N):
        one_line = ''
        for k in range(0,N):
            one_line += str(list[j][k])
        result.append(one_line)
    return result
# 입력 값은 아래의 code부터 받는다.
 
T = int(input())
 
for tc in range(1,T+1):
    N = int(input()) # N을 받는다.
    base_matrix = [[0] * 3 for _ in range(N)] # 빈 Matrix를 형성한다.
 
    matrix_info = [] # Matrix에 대한 정보를 받는 과정
    for size in range(0,N):
        matrix_info.append(list(map(int, input().split())))
 
    matrix_90 = change_matrix(degree_90(matrix_info, N),N)
    matrix_180 = change_matrix(degree_180(matrix_info, N),N)
    matrix_270 = change_matrix(degree_270(matrix_info, N),N)
 
    for i in range(N):
        base_matrix[i][0] = matrix_90[i]
        base_matrix[i][1] = matrix_180[i]
        base_matrix[i][2] = matrix_270[i]
    print(f"#{tc}")
    for i in range(N):
        for j in range(3):
            print(base_matrix[i][j], end = ' ')
        print()