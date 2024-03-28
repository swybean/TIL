
w, h = map(int, input().split())  # w는 가로 j, h는 세로 i
p, q = map(int, input().split())  # p는 j좌표, q는 i좌표 (시작위치 좌표)
t = int(input())    # t초 후 개미의 좌표 (j, i)를 출력해야 함


dj = [1, -1, -1, 1]
di = [1, 1, -1, -1]


arr = [[0] * (w+1) for _ in range(h+1)]

for j in range(w+1):
    for i in range(h+1):
        if arr[j][i] == arr[p][q]:
            for l in range(50000):
                # for k in range(4):
                nj = j + 1 * l
                ni = i + 1 * l

                # 왼쪽 위로 가는 경우
                if nj == 6:
                    nj = nj - 1 * l
                    ni = ni + 1 * l
                    # 경우 1 
                    if nj == 0:
                        nj = nj + 1 * l
                        ni = ni + 1 * l
                    if nj == 0 and ni == 4:
                        nj = nj + 1 * l
                        ni = ni - 1 * l
                    if ni == 4:
                        nj = nj -1 * l
                        ni = ni -1 * l
                    # 경우 2
                    
                    # 경우 3
                        

                
                # 왼쪽 아래로 가는 경우
                if nj == 6 and ni == 4:
                    nj = nj - 1 * l
                    ni = ni - 1 * l
                
                # 오른쪽 아래로 가는 경우
                if ni == 4:
                    nj = nj + 1 * l
                    ni = ni - 1 * l
                    
                






















# time = 0

# for j in range(w):
#     for i in range(h):
#         for k in range(4):
#             nj = j + dj[k]
#             ni = i + di[k]
#             if 0 <= nj < 6 and 0 <= ni < 4:
#                 j = nj
#                 i = ni
#                 time += 1
#                 if time == t:
#                     print(j, i)












