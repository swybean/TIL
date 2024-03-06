T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N은 돌의 개수, M은 작업 횟수
    doll_arr = list(map(int, input().split()))  # 처음 주어지는 돌의 배열 입력 / 0은 흰색, 1은 검은색

    for _ in range(M):
        i, j, w = map(int, input().split())      # 기준위치 i, 작업대상인 돌의 수 j, 작업번호 w 입력

        for o in range(1):                      # 위에 i, j , w를 입력 받으면 아래를 입력 1번당 한번만 반복
            if w == 1:                          # 작업번호가 1이면
                for p in range(i-1, i+j-1):     # 해당 범위에서 p를 반복순회하는데
                    if 0 <= p < N:              # p는 배열을 벗어나면 안된다.
                        if doll_arr[p] == 0:    # 만약 0이면 1로, 1이면 0으로 바꾼다.
                            doll_arr[p] = 1
                        else:
                            doll_arr[p] = 0

            elif w == 2:                                    # 작업번호가 2이면
                for q in range(i-1, i+j-2):                 # 해당 범위에서 q를 반복순회하는데
                    if 0 <= q+1 < N:                        # q도 돌 배열 범위 내에 있어야 하며
                        if doll_arr[q+1] != doll_arr[q]:    # 만약 q의 다음 순서의 돌이 색이 다르면
                            doll_arr[q+1] = doll_arr[q]     # 다음 순서의 돌을 현재 돌과 같은 색으로 만든다

            elif w == 3:                                        # 작업번호가 3이면
                for k in range(i-1, i):                         # 중심점으로 정할 돌을 찾고
                    for l in range(1, j+1):                     # 해당 돌을 기준으로 j만큼 양쪽 돌들을 찾을 건데
                        if 0 <= k-l < N and 0 <= k+l < N:       # 양쪽으로 있는 돌도 배열 범위 내에 있어야 하며
                            if doll_arr[k-l] == doll_arr[k+l]:  # 만약에 양쪽에 있는 돌이 같은 색이면
                                if doll_arr[k-l] == 0:          # 왼쪽 돌이 0이면 1로 바꾸고
                                    doll_arr[k-l] = 1
                                else:                           # 왼쪽 돌이 1이면 0으로 바꾼다.
                                    doll_arr[k-l] = 0

                                if doll_arr[k+l] == 0:          # 오른쪽 돌도 0이면 1로, 1이면 0으로 바꾼다.
                                    doll_arr[k+l] = 1
                                else:
                                    doll_arr[k+l] = 0
                            elif doll_arr[k-l] != doll_arr[k+l]:    # 만약 양쪽 돌이 색이 다르다면
                                doll_arr[k-l] = doll_arr[k-l]       # 양쪽 돌 모두 자기자신 그대로 둔다. (색바꾸지 않음)
                                doll_arr[k+l] = doll_arr[k+l]

    print(f'#{tc}', *doll_arr)  # 정답 출력
