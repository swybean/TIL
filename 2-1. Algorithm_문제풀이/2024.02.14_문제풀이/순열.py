# P[1, 2, 3]의 모든 원소를 사용한 순열
# 123, 132, 213, 231, 312, 321 로 총 6가지 경우가 있다.




#######################
# 순열을 만드는 기본 코드
def f(i, k):
    if i==k:
        print(*P)
    else:
        for j in range(i, k):           # P[i] 자리에 올 원소P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <- P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구

N = 3
P = [1, 2, 3]
f(0, N)


'''
입력값
3
212
585
722

출력값
3 1
'''



######################
# SWEA 문제 풀이 코드

def f(i, k, s):     # i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i==k:
        # print(*P)
        s = 0                   # 선택한 원소의 합
        for j in range(k):      # j행에 대해
            s += arr[j][P[j]]   # j행에서 P[j]열을 고른 경우 합 구하기
        if min_v > s:
            min_v = s
    else:
        for j in range(i, k):           # P[i] 자리에 올 원소P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <- P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
f(0, N)
cnt = 0
print(min_v)



####################
# 백트래킹 사용한 버전

def f(i, k, s):     # i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i==k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):           # P[i] 자리에 올 원소P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <- P[j]
            f(i + 1, k, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, 0, N)
print(min_v, cnt)



############################

def f(i, k, s):     # i-1까지 선택한 합
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return min_v
    else:
        for j in range(i, k):       # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])   # 백트래킹을 위한
            P[i], P[j] = P[j], P[i]     # 교환전 복구

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    f(0, N, 0)
    print(f'#{tc} {min_v}')

# s = 현재까지 구한 숫자들의 합
# k = N
'''
P의 인덱스 번호는 행의 순서
P의 인덱스 번호의 해당하는 값은 열의 순서
'''



