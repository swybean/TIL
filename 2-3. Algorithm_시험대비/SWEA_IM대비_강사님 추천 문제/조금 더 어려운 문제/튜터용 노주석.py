def change_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    elif switch[num] == 1:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, num = map(int, input().split())

    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change_switch(i)
    # 여자
    else:
        change_switch(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change_switch(num + k)
                change_switch(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()

'''
while True
    if switch[num-cnt] == switch[num+cnt]:
        식쓰고
        cnt +=1
        정지조건 따로 쓰기
'''