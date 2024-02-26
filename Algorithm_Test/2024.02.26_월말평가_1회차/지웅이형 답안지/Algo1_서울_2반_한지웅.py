# 돌뒤집기
'''
N개의 칸에 돌이 하나씩 있다.
총 M번의 뒤집기를 진행한다.
    1. i부터 j개의 돌 뒤집기 (i, i+1 ... (i+j-1))
    2. i부터 j개의 돌을 i번째 돌의 색으로 바꾸기
    3. i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해 i와 다른색으로 바꾸기
'''
def change_stone(index):
    if stone[index] == 1:
        stone[index] = 0
    elif stone[index] == 0:
        stone[index] = 1

def work_1(a, b):
    for i in range(a,a+b):
        if 1<=i<=N:
            change_stone(i)
            # 돌 뒤집기 함수를 통해 돌 뒤집기

def work_2(a,b):
    color = stone[a]
    for i in range(a,a+b):
        if 1<=i<=N:
            stone[i] = color
            # 기준 돌의 색상으로 바꾸기

def work_3(a,b):
    for i in range(1,b+1):
        left = a-i
        right = a+i
        if 0<=left<=N and 0<=right<=N:
            if stone[left] == stone[right]:
                # 기준 돌 좌우가 동일한 색상이면서 인덱스 만족시
                change_stone(left)
                change_stone(right)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    # N은 돌의 개수, M은 작업의 총 횟수
    stone = [-1] + list(map(int,input().split()))

    for k in range(M): # 작업을 하는 횟수만큼 반복
        a, b, num = map(int,input().split())
        # a는 작업의 기준, b는 진행할 개수, num은 작업번호
        if num == 1:
            work_1(a,b)
        elif num == 2:
            work_2(a,b)
        elif num == 3:
            work_3(a,b)

    print(f"#{tc}", end = ' ')
    print(*stone[1:])
