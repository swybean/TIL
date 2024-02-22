t = int(input())
 
for test_case in range(1, t + 1):
    n = int(input())
    carrot_farm = [list(map(int, input().split())) for _ in range(n)]
    x, y = 0, 0 # 꼭지점 위치
    result = 0  # 결과값 멧돼지 수
    first = 0   # 변수 단순화하기 위해서 
 
    # 왼쪽 위
    for i in range(n):
        for j in range(n):
            if carrot_farm[i][j] == 1 and first == 0:
                x, y = i, j
                first += 1
 
    for i in range(x + 1):
        for j in range(y + 1):
            if carrot_farm[i][j] == 2:
                result += 1
 
    # 오른쪽 위
    for i in range(n):
        for j in range(n):
            if carrot_farm[i][n - j - 1] == 1 and first == 1:
                x, y = i, n - j - 1
                first += 1
 
    for i in range(x + 1):
        for j in range(y + 1, n):
            if carrot_farm[i][j] == 2:
                result += 1
 
    # 왼쪽 아래
    for i in range(n):
        for j in range(n):
            if carrot_farm[n - i - 1][j] == 1 and first == 2:
                x, y = n - i - 1, j
                first += 1
 
    for i in range(x, n):
        for j in range(y + 1):
            if carrot_farm[i][j] == 2:
                result += 1
 
    # 오른쪽 아래
    for i in range(n):
        for j in range(n):
            if carrot_farm[n - i - 1][n - 1 - j] == 1 and first == 3:
                x, y = n - 1 - i, n - 1 - j
                first += 1
 
    for i in range(x, n):
        for j in range(y, n):
            if carrot_farm[i][j] == 2:
                result += 1
 
    print(f'#{test_case} {result}')