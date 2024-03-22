T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    doll_arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        for p in range(i-1, i+j-2):                 # p번 돌부터 p+j번돌까지로 범위 설정
            if p+1 < N:                             # p+1번 돌이 배열 안에 있는 경우에만 실행
                if doll_arr[p+1] != doll_arr[p]:    # p+1번 돌이 p번 돌과 색이 다르면
                    doll_arr[p+1] = doll_arr[p]     # p번 돌 색으로 바꿔라

    print(f'#{test_case}', *doll_arr)