# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 
# N = 원소 개수
# K = 원소의 합
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
         
    n = len(A)
    count = 0

    for i in range(1 << n):   # i : 각 부분집합을 표현  1<<n: 부분집합의 개수
        num_sum = 0     # 원소의 합
        jip_sum = 0     # 원소의 개수

        for j in range(n):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                num_sum += A[j]  # A 리스트의 j번 원소 더하기
                jip_sum += 1     # 원소의 개수를 1 추가한다.

        if num_sum == K and jip_sum == N:   #원소의 합, 개수가 N, K랑 일치하면
            count += 1      # count를 1 증가시킨다.

    print(f'#{test_case} {count}')




                
                






'''
T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N = arr[0]
    K = arr[1]

    n = 12

    for i in range(1<<n):   # 1<<n: 부분집합의 개수
        for j in range(n):  # 원소의 수만큼 비트를 비교
            if i & (1<<j):  # i의 j번 비트가 1인 경우

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N = arr[0]
    K = arr[1]

    n = len(A)

    for i in range(1<<n):   # 1<<n: 부분집합의 개수
        subset_sum = 0
        for j in range(n):  # 원소의 수만큼 비트를 비교
            if i & (1<<j):  # i의 j번 비트가 1인 경우
                subset_sum += A[j]  # A 리스트의 j번 원소 더하기
        if subset_sum == K:
            print("부분집합:", end=" ")
            for j in range(n):
                if i & (1 << j):
                    print(A[j], end=" ")
            print()
'''