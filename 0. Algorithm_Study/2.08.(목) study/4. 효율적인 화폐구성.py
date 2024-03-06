'''
입력 조건 
• 첫째 줄에 N.M이 주어진다. (1 < N < 100, 1 < M < 10,000)
• 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 
  화폐 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건 
• 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
• 불가능할 때는-1을 출력한다.
'''

########내 풀이
N, M = map(int, input().split()) # 화폐 종류(N), 구할 금액(M) 입력

money_values = [int(input()) for _ in range(N)]  # 화폐 가격을 입력

d = [0] * 10000
d[0] = 0 # 0원 만들기 위한 화폐 개수는 0개
d[1] = 1 # 1원 만들기 위한 화폐 개수는 1개

for i in range(N):
    ㅇ


'''
#######해설 풀이
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 정수 N, M을 입력받기
n, m = map(int, input().split())

# 화폐의 단위 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i - array[i])원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

'''


