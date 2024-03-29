


def dfs(cnt, sum_height):
    global ans

    # 기저 조건
    # 탑 높이 = B 이상일 때
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    # 모든 직원을 고려했을 때
    if cnt == N:
        return
    
    dfs(cnt+1, 
    






T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)

    dfs(0, 0)


