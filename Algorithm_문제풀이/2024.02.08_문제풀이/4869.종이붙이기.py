
import sys
sys.stdin = open('input1.txt', 'r')

# 내풀이
T = int(input())    # 테스트 케이스 개수 입력
for tc in range(1, T+1):    # 테스트케이스 반복
    N = int(input())
    
    d = [0] * 301  
    d[10] = 1   
    d[20] = 3   
    # 10과 20은 위에서 구했으니 30부터 시작
    # 30부터 시작하는 이유 : 가로길이는 10의 배수로 주어진다고 해서
    # 따라서 range(30, N+1, 10)은 30부터 N+1까지 10의 단위로 범위를 설정 한 것
    for i in range(30, N+1, 10): 
        # 10의 단위로 구하니까 i-1과 i-2가 아닌 i - 10, i - 20으로 설정
        d[i] = (d[i - 10] + 2 * d[i - 20])

    print(f'#{tc} {d[N]}')


import sys
sys.stdin = open('input1.txt', 'r')

# 성재형 풀이 나누기10 사용한거 따라해보기
    
T = int(input())    
for tc in range(1, T+1):    
    N = int(input())
    
    n = N // 10 # 가로 길이는 10의 배수니까 10으로 나눠서 한자리수로 계산하기 위함
    d = [0] * 31  # 범위도 10배 줄이고 +1 해서 31
    d[1] = 1   
    d[2] = 3   
    for i in range(3, n+1): 
        d[i] = (d[i - 1] + 2 * d[i - 2])

    print(f'#{tc} {d[n]}')



import sys
sys.stdin = open('input1.txt', 'r')

## 성재형 풀이
def tile(N):
    d = [0] * 1001
    d[1] = 1
    d[2] = 3
    for i in range(3, N+1):
        d[i] = d[i-1]+2*d[i-2]
    return d[N]

Test = int(input())
for test in range(1, Test+1):
    N = int(input())
    num = tile(N//10)
    print(f'#{test}', num)


