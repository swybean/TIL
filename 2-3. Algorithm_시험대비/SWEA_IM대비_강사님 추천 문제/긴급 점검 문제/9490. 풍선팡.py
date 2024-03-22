di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flower = 0  
    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            for p in range(1, arr[i][j]+1):
                for k in range(4):
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        flower += arr[ni][nj] 
            if max_flower < flower:
                max_flower = flower
    print(f'#{test_case} {max_flower}')



#### 풍선팡 기본형
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_flower = 0  # 최대 꽃가루 합 저장할 변수 0으로 초기화
    # for i in range(N):
    #     for j in range(M):
    #         flower = arr[i][j]
    #         for k in range(4):
    #             ni = i + di[k]
    #             nj = j + dj[k]
    #             if 0 <= ni < N and 0 <= nj < M:
    #                 flower += arr[ni][nj]
    #         if max_flower < flower:
    #             max_flower = flower
    # print(f'#{test_case} {max_flower}')


#### 풍선팡 변형버전 (범위설정형)
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_flower = 0  # 최대 꽃가루 합 저장할 변수 0으로 초기화

#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             flower = arr[i][j]
#             for k in range(4):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 flower += arr[ni][nj]
#             if max_flower < flower:
#                 max_flower = flower
#     print(f'#{test_case} {max_flower}')




