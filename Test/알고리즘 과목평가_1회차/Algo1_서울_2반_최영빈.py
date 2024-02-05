T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_v = 0   # 총 보너스 점수

    for i in range(1, N-1):     # 가장자리 열은 범위에서 제외
        for j in range(1, N-1):
            cnt = 0     # 보너스 점수 기록할 변수
            for k in range(4):  # 상하좌우의 점수를 cnt에 더하기
                ni = i + di[k]
                nj = j + dj[k]
                cnt += arr[ni][nj]

            cnt -= arr[i][j]  # 상하좌우 합에서 가운데 점수 빼기

            if cnt < 0:     # 음수면 보너스 점수 0점처리
                cnt = 0
            if cnt >= 0:    # 양수이면 보너스 점수
                if cnt % 2 == 0:    # 만약 짝수라면 보너스 점수 2배
                    cnt = cnt * 2
            if cnt > max_v:     # 총 보너스 점수보다 현재 보너스 점수가 크면 바꾸기
                max_v = cnt
                
    print(f'#{tc} {max_v}')





'''
[입력 예시]
3
3
1 1 1
1 5 1
1 1 1
3
1 1 1
1 1 1
1 1 1
4
1 1 1 1
1 3 1 1
1 4 2 1
1 1 1 1

[출력 예시]
#1 0
#2 3
#3 12
'''


#1 12
#2 4
#3 12