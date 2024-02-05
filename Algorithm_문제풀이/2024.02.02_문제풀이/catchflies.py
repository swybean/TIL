T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range (N)]


    # 최댓값을 넣을 max
    max = 0

    # 시작점은 NxN 행렬 안의 (i,j)
    for i in range(N):
        for j in range(N):

            # 현재 위치 i,j를 기준으로 M*M 행렬의 합을 구할것
            sum = 0
            # 현재위치 i,j 기준으로 M*M 행렬 정의
            for m1 in range(M):
                for m2 in range(M):
                    # i,j 기준으로 i 를 0에서 (m-1)까지, j 를 0에서 (-1)까지 좌표바꿈,
                    ni = i + m1
                    nj = j + m2
                    # N*N행렬을 벗어나지 않는 한에서 바꾼 좌표의 arr 값을 sum 에 넣어줌
                    if 0<= ni < N and 0<= nj <N:
                        sum+= arr[ni][nj]

            if sum > max:
                max = sum

    print(f'#{tc} {max}')


'''
검증용 입력값
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

출력값 아래와 같이 나와야 함
#1 49
#2 159
'''




#### 잘못푼거
# T = int(input())
# # 우, 아래대각선, 하
# di = [0, 1, 1]
# dj = [1, 1, 0]
#
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range (N)]
#
#     max = 0
#     for i in range(N):
#         for j in range(N):
#             sum = arr[i][j]
#
#             # 방향대로 더해주기
#             for m in range(1,M):
#                 for k in range(3):
#                     ni = i + di[k] * m
#                     nj = j + dj[k] * m
#                     if 0<= ni<N and 0<= nj <N:
#                         sum += arr[ni][nj]
#             if sum > max:
#                 max = sum
#
#     print(f'#{tc} {sum}')