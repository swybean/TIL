
def dfs(cnt, sum_height):
    global ans
    
    if sum_height == K:
        ans += 1
        return
    
    if cnt == N:
        return
    
    dfs(cnt + 1, sum_height + arr[cnt])
    dfs(cnt + 1, sum_height)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())        # N은 자연수의 개수, K는 구해야 하는 합
    arr = list(map(int, input().split()))   # 자연수 리스트

    ans = 0     # 부분 수열의 합이 K가 되는 경우의 수

    dfs(0, 0)

    print(f'#{test_case} {ans}')


