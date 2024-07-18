'''
완전탐색 + 백트래킹

출력
1. 최소비용
2. 최소비용 식재료 번호 공백구분 + 오름차순
2-1. 만족하는 답이 없으면 -1 출력, 둘째줄 아무것도 출력 x
'''



N = int(input())    # 식재료의 개수 N
target = list(map(int, input().split())) # 최소 영양성분 리스트
arr = [list(map(int, input().split())) for _ in range(N)]   # 식재료 성분 + 가격 리스트

result = 5000    # 최소 식재료의 가격 합
cost = 0

# now = [0] * 5   # 여기에 현재 고른 식재료들의 영양성분 + 가격 합 저장하기
# print(now)      # [0, 0, 0, 0, 0]

print(target)   # [100, 70, 90, 10]

print(arr)      
# [
# [30, 55, 10, 8, 100], 
# [60, 10, 10, 2, 70], 
# [10, 80, 50, 0, 50], 
# [40, 30, 30, 8, 60], 
# [60, 10, 70, 2, 120], 
# [20, 70, 50, 4, 4]
# ]

for i in range(N):
    if target[0] > 0 and target[1] > 0 and target[2] > 0 and target[3] > 0:
        target[0] - arr[i][0]
        target[1] - arr[i][1]
        target[2] - arr[i][2]
        target[3] - arr[i][3]
        cost += arr[i][4]
        if target[0] <= 0 and target[1] <= 0 and target[2] <= 0 and target[3] <= 0:
            if result > cost:
                result = cost
                print(result)

    


