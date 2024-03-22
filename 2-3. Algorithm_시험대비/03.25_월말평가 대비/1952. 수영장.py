'''


# 완전탐색
1월의 경우 1일, 1달, 3달 권
2월의 경우 1일, 1달, 3달 권
~
12월의 경우 1일, 1달, 3달 권
-> 따라서 경우의 수가 3의 10승 = 6만
-> 완전탐색으로 풀어도 문제 없다!




'''

def dfs(month, sum_cost):
    global ans

    # 기저 조건
    # 1. 12월까지 다 봤네? 종료
    if month > 12:
        # 최소 비용
        ans = min(ans, sum_cost)
        return
    
    # 2. 이미 최소값을 넘어갔네? 종료
    if sum_cost > ans:
        return
    
    # 모두 1일권으로 구매
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매
    dfs(month + 12, sum_cost + cost[3])    


T = int(input())
for test_case in range(1, T + 1):
    cost = list(map(int, input().split()))

    # 인덱스 0부터 시작하는거 개시러 -> 1부터 쓸래! -> 맨 앞에 0 쓰레기값 넣자
    days = [0] + list(map(int, input().split()))

    # 최소비용
    ans = int(1e9)
    dfs(1, 0)

    print(f'#{test_case} {ans}')


'''
1
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
'''