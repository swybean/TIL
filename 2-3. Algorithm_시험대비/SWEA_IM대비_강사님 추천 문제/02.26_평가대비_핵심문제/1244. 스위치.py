'''
남자(1) : 받은 번호의 배수인 번호의 스위치를 바꿈
여자(2) : 받은 번호와 같은 번호의 스위치를 중심으로 좌우대칭인 구간의 스위치를 모두 바꿈
스위치의 마지막 상태를 출력하는 프로그램을 작성하시오.

8
0 1 0 1 0 0 0 1
2
1 3
2 3

1 0 0 0 1 1 0 1
'''
# print(switch)    # [3, 0, 1, 0, 1, 0, 0, 0, 1]

def change_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    elif switch[num] == 1:
        switch[num] = 0
    return

N = int(input())
switch = [999] + list(map(int, input().split()))    # 스위치 형태
students = int(input())                             # 학생 수     

for _ in range(students):
    sex, num = map(int, input().split())            # 성별, 번호

    # 남학생인 경우
    if sex == 1:                    
         for i in range(num, N+1):  # i를 switch에서 반복해서 찾고
            if i % num == 0:        # 배수이면
                change_switch(i)    # 함수 실행

    # 여학생인 경우
    elif sex == 2:
        change_switch(num)               # 일단 해당 번호 함수 실행
        for k in range(N//2+1):            # 범위는 절반으로 설정
            # 만약 좌우 숫자가 범위 내에 있고, 좌우 숫자가 같으면
            if num + k <= N and num - k >= 1 and switch[num + k] == switch[num - k]:
                change_switch(num + k)   # 둘 다 함수 실행
                change_switch(num - k)  
            else:                        # 같지 않으면 정지
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()