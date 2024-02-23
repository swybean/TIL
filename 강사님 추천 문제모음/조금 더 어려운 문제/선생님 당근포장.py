T = int(input())
for tc in range(1,T+1):
    N, M=map(int, input().split())
    matrix = [0] + list(map(int,input().split()))
 
    distance = 0
    current = 0
    my_cart = 0
 
    while current <= N:
        if matrix[current] == 0:
            current += 1
            distance += 1
            continue
 
        while matrix[current] != 0 and my_cart != M:
            my_cart += 1
            matrix[current] = matrix[current] - 1
                 
        if my_cart == M:
            distance += current
            current = 0
            my_cart = 0
     
        if my_cart != M and matrix == [0] + [0]*N:
            distance += (current-1)
 
    print(f"#{tc} {distance}")