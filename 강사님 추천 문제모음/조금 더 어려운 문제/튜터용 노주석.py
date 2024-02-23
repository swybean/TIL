T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()      
    result = 987654321  
    for i in range(N-2):
        for j in range(i+1, N-1):
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                small = len(carrot[:i+1])
                middle = len(carrot[i+1:j+1])
                big = len(carrot[j+1:N])
                if small <= N//2 and middle <= N//2 and big <= N//2:
                    minus = max(small, middle, big) - min(small, middle, big)
                    if result > minus:
                        result = minus
                else:
                    result = -1
            else:
                result = -1
    else:
        result = -1
                    
    print(f'#{test_case} {result}')