
# 분할하는 함수
def msort(m):
    # 원소가 하나만 남은 경우
    if len(m) == 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = msort(left)          # 왼쪽 절반 분할
    right = msort(right)        # 오른쪽 절반 분할
    
    return merge(left, right)   # 다시 합친 결과 리턴

# 병합하는 함수
def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = j = 0   # i : 왼쪽 배열에서 교환할 위치, j :오른쪽 배열에서 비교할 위치

    while i < len(left) and j < len(right):  # 양쪽에 비교할 원소가 있는 경우
        if left[i] < right[j]:
            result[i + j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1

    while i < len(left) :       # left의 원소만 남은 경우
        result[i+j] = left[i]
        i += 1

    while j < len(right):
        result[i+j]= right[j]   # right의 원소만 남은 경우
        j += 1

    return result

arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = msort(arr)
print(arr)      # [2, 8, 10, 16, 22, 30, 31, 69]
print(arr[3])   # 16