# x1, y1, x2, y2 = [list(map(int, input().split())) for _ in range(4)]
# # print(x1, y1, x2, y2) # [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]

# arr = [[0] * 101 for _ in range(101)]
# result = 0  # 사각형의 넓이 합

# for i in range(x1, x2):
#     for j in range(y1, y2):
#         arr[i][j] = 1

# for i in range(102):
#     for j in range(102):
#         if arr[i][j] == 1:
#             result += 1

# print(result)

#####################

arr = [[0] * 101 for _ in range(101)]
result = 0  # 모든 사각형의 넓이 합

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())  # 각 사각형의 좌하단, 우상단 좌표 입력 받기
    for i in range(x1, x2):     # 좌하단 좌표부터 우상단 좌표까지 범위를 순회하면서
        for j in range(y1, y2): 
            arr[i][j] = 1       # arr의 해당 좌표 값을 1로 변경

for p in range(101):        # 모든 좌표를 순회하면서
    for q in range(101):
        if arr[p][q] == 1:  # 해당 좌표 값이 1이라면
            result += 1     # result 변수에 1을 더한다.
print(result)



