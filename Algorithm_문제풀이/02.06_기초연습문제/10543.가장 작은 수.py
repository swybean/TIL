import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = max(arr)

    for i in arr:
        if i < min_num:
            min_num = i
            result = min_num

    print(f'#{tc} {result}')
            

#### 지양의 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = arr[0]  # 최솟값을 배열의 첫 번째 원소로 초기화합니다.
    min_index = 0  # 최솟값의 인덱스를 저장할 변수를 초기화합니다.
    
    for i in range(1, N):  # 배열의 두 번째 원소부터 순회합니다.
        if arr[i] < min_num:  # 현재 원소가 최솟값보다 작으면
            min_num = arr[i]  # 최솟값을 갱신하고
            min_index = i  # 최솟값의 인덱스를 갱신합니다.

    print(f'#{tc} {min_index}')