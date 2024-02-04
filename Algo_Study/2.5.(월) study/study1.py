'''
동빈이네 전자 매장에는 부품이 N개 있다. 
각 부품은 정수 형태의 고유한 번호가 있다. 
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 
동빈이는 때를 놓치지않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
N = 5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
M = 3
[5, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력
한다. 구분은 공백으로 한다.

입력 조건 
• 첫째 줄에 정수 N이 주어진다. (1 < N < 1,000.000)
• 둘째 줄에는 공백으로 구분하여 이개의 정수가 주어진다. 
이때 정수는 1 보다 크고 1,000.000 이하이다.
• 셋째 줄에는 정수 M이 주어진다. (1 < M < 100,000)
• 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 
이때 정수는 1 보다 크고 1,000,000 이하이다.

출력 조건 
• 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다


'''


# 이진탐색을 위한 함수 제작
def binary_search(arr, target, start, end): 
    # 스타트지점이 끝지점보다 크거나 같은 동안 반복시작
    while start <= end: 
        mid = (start + end) // 2  # mid는 중간값으로 설정
# 목표를 찾으면 중간값의 인덱스로 설정하고 반환
        if arr[mid] == target:
            return mid
# 중간값보다 목표값이 작으면 왼쪽을
        elif arr[mid] > target: 
            end = mid - 1
# 중간값보다 목표값이 크면 오른쪽을 확인
        else:
            start = mid + 1
    return None

N = int(input())    # 가게 부품 개수 입력

arr = list(map(int, input().split()))   # 가게 부품 번호 입력

# 오름차순으로 정렬하기
for i in range(N):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

# 손님이 요청한 부품 개수 입력
M = int(input())

# 손님이 요청한 부품 번호 입력
bupum = list(map(int, input().split()))

# bupum리스트에서 i를 반복해서 찾기
for i in bupum:
    # 해당 부품이 존재하는지 함수 사용해서확인
    result = binary_search(arr, i, 0, N-1)
    # 있으면 yes 출력
    if result != None: 
        print('yes', end=' ')
    # 없으면 ni 출력
    else:
        print('no', end=' ')
