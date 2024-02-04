T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    min_sum = sum(arr[:M])
    max_sum = 0
 
    for i in range(N - M + 1):
        current_sum = sum(arr[i:i + M])
 
        if current_sum < min_sum:
            min_sum = current_sum
 
        if current_sum > max_sum:
            max_sum = current_sum
 
    result = max_sum - min_sum
   
    print(f'#{test_case} {max_sum - min_sum}')



'''
while문 사용한 풀이 (유안누나)

T = int(input())
 
 
a = 1
while a < T+1:
    N, M = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
 
    result = []
    for i in range(N):
        sum = 0
        for j in range(M):
            if i+M-1 < N:
                sum += N_list[i+j]
 
        if sum != 0:
            result.append(sum)
 
    max = 0
    min = result[0]
    for i in result:
        if i> max:
            max = i
        if i <min:
            min = i
    print(f'#{a} {max-min}')
    a +=1
'''