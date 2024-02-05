T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split()) # N개의 연잎, K번의 점프
    frog_jump_map = list(map(int, input().split()))
    frog_index = 0 # 개구리 위치, 연잎 배치

    count = 0
    my_sum = 0
    while count != K:
        if frog_jump_map[frog_index] >= 0: #양수인경우(앞으로 가는 경우)
            frog_index = frog_index + frog_jump_map[frog_index]
            if frog_index < 0 or frog_index > len(frog_jump_map): # 연잎에 따라 이동할 index가 연잎 밖이라면
                break
            my_sum += frog_jump_map[frog_index]
            count += 1
        else: # 음수인경우(뒤로 가는 경우)
            if_meet_positive = abs(frog_index) # 뒤로 점프 후 앞으로 가는 경우를 대비한 값
            frog_index = frog_index + frog_jump_map[frog_index]
            if frog_index < 0 or frog_index > len(frog_jump_map): # 연잎에 따라 이동할 index가 연잎 밖이라면
                break
            my_sum += frog_jump_map[frog_index]
            count += 1
            if frog_jump_map[frog_index] >= 0: #뒤로 갔는데 다시 앞으로 가야하는 상황이라면
                frog_index = frog_index + frog_jump_map[frog_index] + if_meet_positive
                if frog_index < 0 or frog_index > len(frog_jump_map): # 연잎에 따라 이동할 index가 연잎 밖이라면
                    break
                my_sum += frog_jump_map[frog_index]
                count += 1
    print(f"#{tc} {my_sum}")