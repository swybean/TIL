
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    result = 987654321
    area_book = 0
    area_nam = 0
    area_seo = 0
    area_dong = 0

    for i in range(N):
        for j in range(N):
            if i < j and i + j < N - 1: # 영역1 (북쪽 영역)
                area_book += carrot[i][j]
            if i < j and i + j > N - 1:
                area_dong += carrot[i][j]
            if i > j and i + j < N - 1:
                area_seo += carrot[i][j]
            if i > j and i + j > N - 1:
                area_nam += carrot[i][j]
        
    maxarea = max(area_book, area_dong, area_nam, area_seo)
    minarea = min(area_book, area_dong, area_nam, area_seo)
    result = maxarea - minarea

    print(f'#{test_case} {result}')



    