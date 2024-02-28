
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    h = 0
    w = 0
    for row in arr:
        if '#' in row:
            h += 1
            w = row.count('#')

    if h == w:
        print(f'#{test_case}', 'yes')
    else:
        print(f'#{test_case}', 'no')

    
