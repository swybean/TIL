T = int(input())
for tc in range(1,T+1):
    N = int(input()) # size 정보
    total_map = []
    for i in range(N): # total_map 작성
        total_map += [list(map(int, input().split()))]

    result = []
    for i in range(1,N-1):
        for j in range(1,N-1): # 상하좌우를 더하고 중앙값을 빼는 과정
            for_check_bonus = total_map[i-1][j] + total_map[i][j+1] + total_map[i+1][j] + total_map[i][j-1] - total_map[i][j]
            if for_check_bonus >= 0:
                if for_check_bonus % 2 == 0: # 양수일 때 짝수라면
                    result += [2*for_check_bonus]
                else: # 홀수라면
                    result += [for_check_bonus]
            elif for_check_bonus < 0: #음수라면
                continue
    if result == []: # 보너스 점수를 받을 수 없었다면
        result = [0]

    max_value = result[0]
    for i in range(len(result)): # 최대값을 구하는 과정
        if max_value < result[i]:
            max_value = result[i]
    print(f"#{tc} {max_value}")