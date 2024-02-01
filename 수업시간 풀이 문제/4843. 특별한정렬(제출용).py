
T = int(input())
 
for tc in range(1, T+1):
    N= int(input())
    arr = list(map(int, input().split()))
 
    for i in range(N):
        if i % 2 == 0:
            max_index = i
            for j in range(i+1,N):
                if arr[j] >= arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
 
        else:
            min_index = i
            for j in range(i+1,N):
                if arr[j] <= arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
 
    print(f'#{tc}', end= ' ')
    for i in range(10):
        print(arr[i], end = ' ')
    print()

