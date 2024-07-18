'''
최대값을 구해야 한다.
행렬문제

처음 i,j 탐색해서 시작점 찾고

M 범위만큼 탐색해서 범위 내 최대값을 찾아서 result에 더해주고
해당 값의 인덱스를 기준으로 다시 M만큼 범위를 찾아야 한다.
다음 범위 내에서 찾은 최대값이 이전 최대값과 같으면 더하지 않고 탐색 종료

'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N과 M입력, N은 큰 행렬, M은 구해야되는 작은 행렬 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 최종 누적합
    now_sum = -99 # 현재 M 행렬에서의 최대값

    for i in range(N-M+1):          # M 크기만큼 에서 반복순회
        for j in range(N-M+1):
            now = arr[i][j]         # 현재값을 현재 칸에 적힌 수로 함
            if now_sum < now:       # 현재 M행렬에서 최대값보다 현재값이 크면 그값으로 변경
                now_sum = now

            if arr[i][j] == now_sum:    # 만약 arr[i][j]가 현재 M 행렬에서의 최대값과 같으면
                for p in range(N-M+1):          # 거기서 다시 M크기만큼 안에서 반복 순회
                    for q in range(N-M+1):
                        now2 = arr[i][j]         # 현재값2는 현재 위치값으로 설정
                        if now_sum < now2 and now_sum != now2:  # 만약 현재값2가 최대값보다 크고 같지 않으면
                            now_sum += now2 # 최대값에 더해준다.

            result += now_sum   # 최종 누적합에 현재 최대값을 더해준다.
    print(f'#{tc} {result}')








