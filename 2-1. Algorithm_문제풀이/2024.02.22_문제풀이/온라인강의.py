N = int(input())

list = [[0] * 7 for _ in range(2)]

t1 = N
for i in range(4):
    list[0][i] = t1
    t1 += 1

t2 = N
for i in range(6, 2, -1):
    list[1][i] = t2
    t2 -= 1

print(list[0])
print(list[1])










