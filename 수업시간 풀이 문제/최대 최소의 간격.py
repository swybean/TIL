T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0   # 맨 앞을 최솟값 위치로 지정
    max_idx = 0   # 맨 앞을 최댓값 위치로 지정

    # 인덱스 정보를 가져와서 값을 확인하기 때문에 for x in ~ 이렇게 쓰면 안된다.!

    for i in range(N):    # len(arr) 쓰지말자. 정보를 추가로 가져오는거니까 이미 입력된 정보인 N 쓰기
        if arr[min_idx] > arr[i]:   # 지금까지의 최솟값보다 arr[i]가 더 작으면
            min_idx = i     
            # 문제에서 가장 작은 수가 여러 개이면 먼저 나오는 위치를 기준으로 하라고 해서 > 로 비교
        if arr[max_idx] <= arr[i]:  # 지금까지의 최댓값보다 arr[i]가 더 크면
            max_idx = i    
             # 문제에서 가장 큰 수가 여러 개이면 마지막으로 나오는 위치를 기준으로 하라고 해서 <= 로 비교
    
        # ans = abs(max_idx - min_idx)  # 내장함수 허용될 경우에만 절대값 함수 abs 사용
    ans = max_idx - min_idx if max_idx > min_idx else min_idx - max_idx
    print(f'#{test_case} {ans}')


