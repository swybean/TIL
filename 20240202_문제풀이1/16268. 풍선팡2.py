# 풍선팡2가 그냥 풍선팡보다 쉽다.

# 어디를 터트려야 종이가 제일 많이 나올지는
# 다 터트려보는 수밖에 없다.


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1): 
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0   # 최대 꽃가루 합계
    for i in range(N):      # MxM 크기의 게임판
        for j in range(M):
            cnt = arr[i][j]     # 터트린 풍선의 꽃가루 수
            # 주변 풍선의 꽃가루 
            for k in range(4):  # 주변 풍선의 인덱스는 ni, nj
                ni = i+di[k]
                nj = j+dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if max_v < cnt:
                max_v = cnt
    print(f'#{test_case} {max_v}')


