# 가장 큰 수는 어디에 들어 있을가...
N = 5
arr = [1, 3, 2, 5, 4]  #같은 숫자가 없는 경우

max_idx = 0     # 첫 번째 원소를 가장 큰 수의 위치로 가정
for i in range(1, N):
    if arr[max_idx] < arr[i]:    # arr[i]가 더 크면
        max_idx = i              # 최대값의 위치를 i로 변경

    # if arr[max_idx] <= arr[i]:    # <= 최대값이 여러개인 경우 가장 오른쪽 최대값을 선택
    #     max_idx = i               # 최대값의 위치를 i로 변경






