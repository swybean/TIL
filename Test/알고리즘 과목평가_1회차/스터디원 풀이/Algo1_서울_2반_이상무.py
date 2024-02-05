"""
[입력]
첫 줄에 테스트케이스 개수 T가 주어진다. (1<=T<=10)
이어 각 테스트케이스별로 첫 줄에 N, 이어 N개의 줄에 칸 칸의 점수
Aij가 N개씩 주어진다. (3 <=N <= 50, 1<=Aij<=20)
[출력]
#과 1번 부터인 테스트케이스 번호, 빈 칸에 이어 보너스 점수의 최댓값을
출력한다
"""
t = int(input())  # 테스트 케이스의 개수 입력

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    max_sum = 0   # 가장 높은 합을 저장해주기 위한 변수

    for i in range(N):
        for j in range(N):
            cnt = 0       # 어레이의 값을 모두 더해주고 가운데 값을 빼 줄 값을 저장해주는 변수
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 < i < N - 1 and 0 < j < N - 1:   # 현재의 행 열이 어레이의 겉 테두리 안에 있을 때 출력
                    cnt += arr[ni][nj]
            cnt -= arr[i][j]

            if cnt <= 0:        # 만약 결과값이 0보다 작다면 cnt = 0 으로 저장
                cnt = 0

            if cnt % 2 == 0:    # 만약 결과값이 짝수라면 cnt의 결과 값 2배 증가
                cnt = cnt * 2

            if max_sum < cnt:
                max_sum = cnt
    print(f'#{tc} {max_sum}')