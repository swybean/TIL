def f(i, ele_num, now_sum, target_sum):
    if now_sum == target_sum:
        return 1
    elif i == ele_num:    # 모든 원소를 고려했으나 s!=t인 경우
        return 0
    elif now_sum > target_sum:     # 고려한 원소의 합이 t보다 큰 경우
        return 0
    else:
        # 현재 원소를 부분집합에 포함하는 경우
        count_include_i = f(i+1, ele_num, now_sum + A[i], target_sum)
        # 현재 원소를 부분집합에 포함하지 않는 경우
        count_exclude_i = f(i+1, ele_num, now_sum, target_sum)
        return count_include_i + count_exclude_i

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = f(0, N, 0, K)
    print(f'#{tc} {cnt}')



# # i = 현재 처리하고 있는 배열A의 인덱스
# # ele_num = 배열A의 총 원소 개수
# # now_sum = 현재까지 부분집합의 합
# # target_sum = 목표로하는 부분집합의 합




