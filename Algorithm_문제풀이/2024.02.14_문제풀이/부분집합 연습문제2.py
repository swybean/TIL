'''
교재 60쪽 연습문제2
{1,2,3,4,5,6,7,8,9,10} powerset 중 원소의 합이 10인 부분집합을 구하시오.


0과 1로 이루어진 비트를 생성
(0은 미포함, 1은 포함)
(예시: 원소 4, 6만 1이고, 나머지 원소는 0인 비트를 찾으면 그게 합이 10인 부분집합이다.)

A = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 이 들어간 비트
bit[i] = A[i]의 포함여부를 나타냄

'''

# 부분집합 중 특정 합을 만족하는 부분집합 구하는 코드

def f(i, k, t): # k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우를 찾기
    if i == k:  # 모든 원소에 대해 결정하면 
        ss = 0  # 부분집합의 합
        for  j in range(k):     
            if bit[j] == 1:     # 1이면, A[i]가 포함된 경우
                ss += A[j]      # A[j]가 포함된거니까 합에다가 더해줘
        # 모든원소에 대한 확인이 끝났고 그 합이 t이면
        if ss == t:
            for  j in range(k):
                if bit[j] == 1:
                    print(A[j], end=' ')
            print()     # 부분집합 출력
    else: 
        for j in range(1, -1, -1):
            bit [i] = j
            f(i+1, k, t)
            # else문 다른 버전
            # bit[i] = 1
            # f(i+1, k)
            # bit[i] = 0
            # f(i+1, k)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N   # bit[i] = A[i]가 부분집합에 포함되는지 표시
f(0, N, 10)




######################################################
# 부분집합 중 특정 합을 만족하는 부분집합 구하는 코드 버전2

def f(i, k, s, t): # k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우를 찾기
    global cnt
    cnt += 1
    if s == t:  # 목표값이면
        for  j in range(k):
            if bit[j] == 1:
                print(A[j], end=' ')
        print()     # 부분집합 출력
    elif i == k:    # 모든 원소를 고려했으나 s!=t인 경우
        return
    elif s > t:     # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N   # bit[i] = A[i]가 부분집합에 포함되는지 표시
cnt = 0
f(0, N, 0, 10)
print(f'cnt:', cnt)





############################
# 부분집합 만드는 코드 기본버전

def f(i, k):
    if i == k:  # 모든 원소에 대해 결정하면 
        ss = 0  # 부분집합의 합
        for  j in range(k):
            if bit[j] == 1:     # A[i]가 포함된 경우
                print(A[j], end= ' ')
                ss += A[j]
        print(ss)
    else: 
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
        # else문 for 사용한 버전
        # for j in range(1, -1, -1):
        #     bit [i] = j
        #     f(i+1, k)

N = 3
A = [1, 2, 3]
bit = [0] * N   # bit[i] = A[i]가 부분집합에 포함되는지 표시
f(0, N)




