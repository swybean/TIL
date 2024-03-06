def f(i, k, s):   
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return min_v
    else:
        for j in range(i, k):      
            P[i], P[j] = P[j], P[i]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]
 
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