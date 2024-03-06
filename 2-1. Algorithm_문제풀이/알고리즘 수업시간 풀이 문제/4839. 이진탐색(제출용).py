T = int(input())

for test_case in range(1, T+1):
    
    N = list(map(int, input().split()))
    arr = list(N)

    l = 1
    r = arr[0]
    c = int((l+r)/2)

    A = arr[1]
    B = arr[2]

    start = 0   
    end = N - 1
    key = c

    while start <= end:     
        middle = (start + end) // 2 
        if arr[middle] == key:   
            return middle
        elif arr[middle] > key:   
            end = middle - 1      
        else:                    
            start = middle + 1
    return 0  



'''
마지막 껄 성공하면 그전꺼는 신경 안써도된다.

각각 미들값을 제외하고 검색하는데
문제는 미들값을 포함하고 검색을 한다. -> 일반적인 이진탐색 코드와 다르다. 일반 코드 쓰면 답이 안나옴

중요도가 떨어진다.
필수로 풀지 않아도된다. 이진탐색 연습이 목적이라면.
'''
