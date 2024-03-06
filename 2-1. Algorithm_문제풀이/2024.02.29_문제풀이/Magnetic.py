


# 열검사 함수
def get_sero_cnt(col):
    cnt = 0
    # red 자성체를 체크
    is_red = False
    
    for row in range(N):
        # 1. red 자성체를 발견
        if arr[row][col] == 1:
            is_red = True
    
        # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt+=1
        elif is_red and arr[row][col] == 2:
            cnt += 1
            is_red = False
    return cnt

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_count = 0
    
    # 열 순회하면서 total_count 누적
    for col in range(N):
        total_count += get_sero_cnt(col)

    print(f'#{test_case} {total_count}')





