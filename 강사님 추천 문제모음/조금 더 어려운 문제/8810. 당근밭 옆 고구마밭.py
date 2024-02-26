
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = list(map(int, input().split()))
                      
    goguma_box = []     # 오름차순으로 이루어진 고구마를 저장할 박스
    goguma_truck = []   # 박스를 저장할 트럭(박스들을 저장)
    goguma = 0          # 현재 밭의 고구마 개수
    for i in range(N):
        if goguma < farm[i]:    # 오른쪽 밭의 고구마 개수가 더 많으면
            goguma_box.append(farm[i])  # 박스에 저장
            goguma = farm[i]    # 현재 고구마 개수를 알기위해 고구마에 저장
        else:                   # 오른쪽 밭의 고구마 개수가 더 많지 않으면
            goguma_truck.append(goguma_box)   # 오름차순으로 이루어진 박스를 트럭에 저장
            goguma_box = []                   # 새로운 고구마 박스 생성  
            goguma_box.append(farm[i])        # 새로운 박스에 고구마 저장
            goguma = farm[i]
 
        if i == N-1:            # 마지막 밭 일때는
            goguma_truck.append(goguma_box)     # 현재 저장된 고구마 박스 트럭에 저장
 
    count = 0     # 길이가 1보다 큰 고구마 줄기 갯수 셀 변수
    length = 0    # 고구마 박스의 길이 저장
    result = 0    # 결과값
 
    for j in range(len(goguma_truck)):      
        if len(goguma_truck[j]) > 1:    # 트럭에 들어있는 박스의 길이가 1보다 클 때
            count += 1                  # 고구마 줄기 갯수 1 증가
            goguma_length = len(goguma_truck[j])    # 가장 긴 고구마 줄기 길이 구하기
            if length < goguma_length:
                length = goguma_length
 
    for k in range(len(goguma_truck)):  
        if len(goguma_truck[k]) == length:  # 가장 긴 고구마 줄기 중에 고구마 합이 가장 큰 것 구하기
            goguma_sum = sum(goguma_truck[k])
            if result < goguma_sum:
                result = goguma_sum
 
    print(f'#{test_case} {count} {result}')





 