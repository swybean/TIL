
'''
# 문제 키워드
- 선반 높이 : B
- 키
- B 이상으로 탑을 쌓아라
- B 이상 중 가장 낮은 탑을 찾아라
--> 탑의 높이 : 점원들의 키(H)의 합

-알고리즘
- DFS + 백트래킹

시간 복잡도
- 최악의 경우 : 20! = 24경 -> 불가능

가지치기
- 중복 제거를 많이 할 수 있다.
- 그런데 얼마나 가지치기가 되는지 모른다.

- 자료구조를 바꿀 수 있나?
- 접근법을 바꿀 수 있나?
-- 이렇게 2가지를 고민해봐야 한다.

# 방법 예시

1~20번까지 20명이 있다고 치면
1의 경우 쌓을까(1) 말까(0) 을 고르고
2의 경우 쌓을까(1) 말까(0) 을 고르고
~
20의 경우 쌓을까(1) 말까(0) 을 고른다.


'''




def dfs(cnt, sum_height):
    global ans

    # 기저조건
    # 기저조건 순서도 중요하다!

    # 1. 키의 합이 B 이상이면 종료
    # -> 현재까지 쌓은 탑의 높이 (sum_height)
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답 : 
        # 최소 탑의 높이는 재귀호출함수들이 "동시에" 사용함 -> 전역 변수로 빼야 된다.
        ans = min(ans, sum_height)
        return
    
    # 2. 모든 점원이 탑을 쌓는데 고려가 되었다면
    # -> 현재까지 쌓은 점원의 수 (cnt)
    if cnt == N:
        return
    
    # 재귀호출 파트
    # 쌓는다
    dfs(cnt + 1, sum_height + arr[cnt])
    # 안쌓는다
    dfs(cnt + 1, sum_height)



T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)

    dfs(0, 0)

    print(f'#{test_case} {abs(ans - B)}')








