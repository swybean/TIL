
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def make_money(i, n, change) :  # i : 교환횟수, n : 카드 수, change : 지정교환 횟수
    global max_v
    if i == change :
        money = 0       # 카드 숫자(string) -> 금액(int)
        for x in reword :
            money = money * 10 + int(x)
        if max_v < money :
            max_v = money
    else :      # 교환 횟수가 남았으면,
        for p in range(n-1) :           # 교환할 카드 중 왼쪽 인덱스 p
            for q in range(p+1, n) :    # 교환할 카드 중 오른쪽 인덱스 q
                reword[p], reword[q] = reword[q], reword[p]
                if (i, int(''.join(reword))) not in check :
                    check.append((i, int(''.join(reword))))
                    make_money(i+1, n, change)
                reword[p], reword[q] = reword[q], reword[p]
 
 
t = int(input())  # 테스트 케이스 개수 받기
 
for tc in range(1, t + 1):
    reword, change = input().split()  # 숫자판 reword / 변경 횟수 change
    reword = list(reword)  # 숫자판을 리스트화
    N = len(reword)  # 숫자판 길이(숫자 개수) N
    max_v = 0  # 최대 상금을 저장할 변수 생성
    check = []  # 같은 교환횟수에서 같은 숫자가 나오면 가지치기
    make_money(0, N, int(change))
 
    print(f'#{tc} {max_v}')