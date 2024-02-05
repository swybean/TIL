'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input())   # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))

max_v = 0   # 가장 큰 낙차
for i in range(N-1):    # i는 낙차를 구할 위치
    count = 0   # 오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1, N):   # for j: i+1 -> N-1
        if arr[i] > arr[j]:
            count += 1
    if max_v < count:   # 현재 낙차가 최대 낙차보다 크면
        max_v = count   # 바꿔라
print(max_v)
