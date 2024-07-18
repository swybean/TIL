
N = int(input())    # 기둥 개수

bd_list = []

for _ in range(N):
    L, H = map(int, input().split())    # L은 열, H는 행
    bd_list.append((L, H))

bd_list.sort()  # [(2, 4), (4, 6), (5, 3), (8, 10), (11, 4), (13, 6), (15, 8)]

result = 0

bd = 0
bd_idx = 0
for i in range(len(bd_list)):
    if bd < bd_list[i][1]:
        bd = bd_list[i][1]
        bd_idx = i
print(f'bd : {bd}')
print(f'bd_idx : {bd_idx}')


for i in range(bd_idx):   # len(bd_list) = 7, 0~6
    if bd_list[i][1] < bd_list[i+1][1]:









'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

'''

