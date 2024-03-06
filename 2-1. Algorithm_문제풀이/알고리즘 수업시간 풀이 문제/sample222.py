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
