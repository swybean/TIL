# 이진 검색 할 배열
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 이진 검색을 위해서는 정렬된 상태의 데이터가 필요
arr.sort()
print(arr)

# 1. 이진 검색 - 반복문 버전
def binarysearch(target):
    # 제일 왼쪽, 오른쪽 인덱스 구하기 (low는 왼쪽, high는 오른쪽)
    low = 0
    high = len(arr) - 1
    # 탐색횟수
    cnt = 0

    # 해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low + high) // 2  # 가운데 숫자 설정
        print(f'mid = {mid} / arr[mid] = {arr[mid]}')
        cnt += 1

        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid, cnt
        
        elif arr[mid] > target:
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1
    # 못찾으면 =1 반환
    return -1, cnt

print(f'21 = {binarysearch(21)}')
# 21 = (1, 2) 
# 21이 sort된 arr에서 인덱스 1번 자리에 있고, 2번만에 찾았다는 뜻
print(f'324 = {binarysearch(324)}')
# 324 = (6, 2)
print(f'888 = {binarysearch(888)}')
# 888 = (-1, 4)





'''
재귀함수의 기본적인 틀
# 기저조건 (언제까지 재귀가 반복되어야 할까?)
# 다음 재귀 들어가기 전에 무엇을 해야할까?
# 다음 재귀함수 호출 (파라미터로 어떤 것들을 넘겨줘야 할까?)
# 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?
'''

# 2. 이진 검색 - 재귀 함수 버전
def binarysearch2(low, high, target):
    # 기저조건 (언제까지 재귀가 반복되어야 할까?)
    if low > high:
        return -1

    # 다음 재귀 들어가기 전에 무엇을 해야할까?
    # 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀함수 호출 (파라미터로 어떤 것들을 넘겨줘야 할까?)
    if target < arr[mid]:
        return binarysearch2(low, mid - 1, target)  # high = mid - 1 이라서
    elif target > arr[mid]:
        return binarysearch2(mid + 1, high, target) # low = mid + 1 이라서
    

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?
    # 이진 검색에서는 없다!

print(f'21 = {binarysearch2(0, len(arr) - 1, 21)}')
# 21 = 1
print(f'324 = {binarysearch2(0, len(arr) - 1, 324)}')
# 324 = 6
print(f'888 = {binarysearch2(0, len(arr) - 1, 888)}')
# 888 = -1
