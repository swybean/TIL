T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    carrot = [0] + list(map(int, input().split()))

    total_move = 0  # 일꾼 총 이동 거리
    now_move = 0    # 현재까지 이동한 거리
    sure = 0        # 현재 수레에 실은 당근의 수

    while now_move <= N:
        if carrot[now_move] == 0:
            now_move += 1
            total_move += 1
            continue
 
        while carrot[now_move] != 0 and sure != M:
            sure += 1
            carrot[now_move] = carrot[now_move] - 1
                 
        if sure == M:
            total_move += now_move
            now_move = 0
            sure = 0
     
        if sure != M and carrot == [0] + [0]*N:
            total_move += (now_move-1)
 
    print(f"#{test_case} {total_move}")



