T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    a = len(A)
    result = 0  # 원소의 개수, 합이 일치하는 부분집합의 개수를 저장할 변수

    for i in range(1 << a): # A의 모든 부분집합을 순회하자, (1 << a)가 A의 모든 부분집합을 의미
        ele_cnt = 0 # 부분집합 원소의 개수
        ele_sum = 0 # 부분집합 원소의 합

        for j in range(a):      # a까지 순회하면서 각 숫자가 부분집합에 포함되는지 확인
            if i & (1 << j):    # 현재 부분집합에 j번째 숫자가 포함되는지를 확인
                ele_cnt += 1    # 포함된다면 개수 1증가
                ele_sum += A[j] # 포함된다면 합에 추가
        
        if ele_cnt == N and ele_sum == K:   # 부분집합의 원소의 개수와 합이 N, K와 일치한다면
            result += 1                     # result 1 증가
    
    print(f'#{tc} {result}')

