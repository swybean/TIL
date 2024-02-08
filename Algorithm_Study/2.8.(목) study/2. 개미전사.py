'''
입력 조건 
• 첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <= 100)
• 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. 
  (0 <= K <= 1,000)
출력 조건 
• 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오、

'''


T = int(input())    # 식량 창고 개수
food = list(map(int, input().split()))  # 식량 창고 내 식량 개수

d = [0] * T   # dp 생성
d[0] = food[0]  # dp 0번은 식량창고 0번의 개수
d[1] = max(food[1], food[0])    # dp1번은 식량창고1번과 전에 구한 식량창고0번 중 큰거 선택

for i in range(2, T):   # 0번, 1번은 위에서 구했으니 2번부터 N까지 구해야함
    d[i] = max(d[i - 1], d[i - 2] + food[i])
    # 직전 창고를 턴 경우(d[i-1])와 직전창고 1칸전 창고(d[i - 2])와 현재창고를 
    # 턴 경우 중 더 많이 털 수 있는걸 선택

################# 이해 안되는 부분 ####################
# print(d[T]) 내가 썼던 답인데, 이렇게 하면 출력이 무조건 0 나옴.
# 테스트 케이스 바꿔서 해도 무조건 0밖에 안나오는데
    
print(d[T-1]) 
# 해설에서는 이렇게 하는데 왜 T-1인지 튜터 돌려보고 지피티 써봐도 명료하게 이해 불가능..
# 해결완료
# 내가 만든 dp 테이블은 인덱스가 0부터 시작이라 T만큼 만들어도 마지막 식량창고의 인덱스는 T-1
# 따라서 프린트 T가 아니라 T-1을 해야지 제대로 된 결과가 나온다.
# 0이 나왔던 이유는 내가 [0] * T로 했기 때문에 [0]값이 나온것.
