#  505

N = int(input())    # 모험가의 수
arr = list(map(int, input().split())) # 각 모험가의 공포도
total_group = 0     # 만들 수 있는 최대 그룹수
now_group = 0       # 현재 그룹의 모험가수

arr.sort()  # 오름차순으로 변경

for i in arr:
    now_group += 1
    if now_group == i:
        total_group += 1
        now_group = 0

print(total_group)


'''
arr.sort(reverse=True)  # 3 2 2 2 1

for i in arr:
    fear = i
    if now_group < fear:
        now_group += 1
        if now_group == fear:
            total_group += 1
            now_group = 0
print(total_group)
'''  