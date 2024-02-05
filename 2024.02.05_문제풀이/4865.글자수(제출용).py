import sys
sys.stdin = open('input1.txt', 'r')

# 내가 직접 혼자 해낸 코드!!!!!!!!!!!!!!!!!!!
T = int(input())
for tc in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    total = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
                if cnt > total:
                    total = cnt
    print(f'#{tc} {total}')



#재성이형 코드 (내것보다 길이 더 짧음)
T = int(input())
for tc in range(1, T+1):
    str1 = input()      # 여기서 차이남 그냥 input()만 받아도 됨
    str2 = input()      # 여기서 차이남 그냥 input()만 받아도 됨
    max_v = 0
    print(str1, str2)
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')




'''
두 개의 문자열 str1과 str2가 주어진다. 
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, 
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 
길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

#1 2
#2 1
#3 3
'''