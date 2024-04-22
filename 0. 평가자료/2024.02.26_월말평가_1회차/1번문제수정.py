T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N은 돌의 개수, M은 작업 횟수
    doll_arr = list(map(int, input().split()))  # 처음 주어지는 돌의 배열 입력 / 0은 흰색, 1은 검은색

    for _ in range(M):
        i, j, w = map(int, input().split())      # 기준위치 i, 작업대상인 돌의 수 j, 작업번호 w 입력
        if w == 1:                          # 작업번호가 1이면
            for p in range(i-1, i+j-1):     # 해당 범위에서 p를 반복순회하는데
                if p < N:              # p는 배열을 벗어나면 안된다.
                    doll_arr[p] = (doll_arr[p] + 1) % 2

        elif w == 2:                                    # 작업번호가 2이면
            for q in range(i-1, i+j-2):                 # 해당 범위에서 q를 반복순회하는데
                if q+1 < N:                             # q도 돌 배열 범위 내에 있어야 하며
                    if doll_arr[q+1] != doll_arr[q]:    # 만약 q의 다음 순서의 돌이 색이 다르면
                        doll_arr[q+1] = doll_arr[q]     # 다음 순서의 돌을 현재 돌과 같은 색으로 만든다

        elif w == 3:                                        # 작업번호가 3이면
            for l in range(1, j+1):                         # 해당 돌을 기준으로 j만큼 양쪽 돌들을 찾을 건데
                if 0 <= i-1-l < N and 0 <= i-1+l < N:       # 양쪽으로 있는 돌도 배열 범위 내에 있어야 하며
                    if doll_arr[i-1-l] == doll_arr[i-1+l]:  # 만약에 양쪽에 있는 돌이 같은 색이면
                        doll_arr[i-1-l] = (doll_arr[i-1-l] + 1) % 2
                        doll_arr[i-1+l] = (doll_arr[i-1+l] + 1) % 2
    print(f'#{tc}', *doll_arr)  # 정답 출력