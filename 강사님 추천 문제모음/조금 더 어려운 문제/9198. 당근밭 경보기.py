T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pig_map = [list(map(int, input().split())) for _ in range(N)]
    pig = 0

    top, down = 0, 0
    left, right = 0, 0

    find_top = False
    for i in range(N):
        if not find_top and 1 in pig_map[i]:
            top = i
            down = i
            find_top = True
        elif 1 in pig_map[i]:
            down = i
   
    find_left = False       
    for j in range(N):
        if not find_left and pig_map[top][j] == 1:
            left = j
            right = j
            find_left = True
        elif pig_map[top][j] == 1:
            right = j

    farm_i = list(range(0, top + 1)) + list(range(down, N))
    farm_j = list(range(0, left + 1)) + list(range(right, N))

    for i in farm_i:
        for j in farm_j:
            if pig_map[i][j] == 2:
                pig += 1
    print(f'#{test_case} {pig}')

