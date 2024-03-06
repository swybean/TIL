# 연속한 1의 개수(강의중) 파일 참고하기

T = int(input())
for test_case in range(1, T+1): 
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) +[0] for _ in range(N)] + [[0]*(N+1)]
    # 가장자리에 0을 추가하는 방법은
    # .split())) 뒤에 +[0], 대괄호 밖에 + [[0]*(N+1)] 추가한다.
    N += 1 # 0인 행과 열 추가

    # 가로 세로로 연속한 1의 개수가 K인 경우를 찾는다.
    ans = 0

    for i in range(N):
        count = 0   # i행에서 연속된 1의 개수
        for j in range(N):
            if arr[i][j]:   # arr[i][j]==1이면
                count += 1
            else:   # arr[i][j]==0이면
                if count == K:
                    ans += 1
                count =0

    for j in range(N):
        count = 0   # j열에서 연속된 1의 개수
        for i in range(N):
            if arr[i][j]:   # arr[i][j]==1이면
                count += 1
            else:   # arr[i][j]==0이면
                if count == K:
                    ans += 1
                count =0

    print(f'#{test_case} {ans}')






