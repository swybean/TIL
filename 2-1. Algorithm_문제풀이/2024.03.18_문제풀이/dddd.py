def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
 
t = int(input())
 
for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    sorted_arr = quick_sort(arr)
    result = sorted_arr[n//2]
 
    print(f'#{test_case} {result}')

#####################################################

def quickSorting(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
  
    while left <= right:

        while left <= right and arr[left] <= arr[pivot]:
            left += 1
            
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
  
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
  
    quickSorting(arr, start, right - 1)
    quickSorting(arr, right + 1, end)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quickSorting(arr, 0, len(arr)-1)

    print(f'#{test_case}',arr[N//2])

