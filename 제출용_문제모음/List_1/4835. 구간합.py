
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    maximum = 0
    minimum = 99999999

    for i in range(N - M + 1):  
        if arr[i] + arr[i+1] + arr[i+2] > maximum:
            maximum = arr[i] + arr[i+1] + arr[i+2]

        if arr[i] + arr[i+1] + arr[i+2] < minimum:
            minimum = arr[i] + arr[i+1] + arr[i+2]
        result = maximum - minimum
    
    print(f'#{test_case} {result}')



'''

# 선생님 풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    # min_v = 1000000
    # max_v = 0
    s = 0               # 구간의 합
    for i in range(M):  # 첫 구간의 합
        s += arr[i]
 
    min_v = max_v = s
 
    for i in range(N-M):    # 이미 계산된 구간의 합에서 제외할 맨 앞 원소
        s -= arr[i]
        s += arr[i+M]       # 현재 구간 다음 원소를 구간에 추가
        if min_v > s:
            min_v = s
        if max_v < s:
            max_v = s
 
    print(f'#{tc} {max_v-min_v}')

    

# 탁호준님 풀이
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 정수의 개수, M은 구간의 개수
    nums = list(map(int, input().split())) #N개의 정수 입력 받기, 입력받은정수는 1~10,000
 
    max_sum = N #최대 구간합을 저장할 변수
    min_sum = 10000*N #최소 구간합을 저장할 변수
 
    #M개의 값을 더하기 시작할 위치 선정
    for i in range(N-M+1):
        sum = 0 #M개의 값을 더할 변수
        #이웃한 M개의 값 더하기
        for j in range(M):
            sum += nums[i+j]
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum
    #최대 구간합과 최소 구간합의 차 출력
    print(f'#{tc} {max_sum-min_sum}')    


'''