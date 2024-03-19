
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
  
    container.sort(reverse=True)
    truck.sort(reverse=True)

    result = 0
    c_index = 0
    t_index = 0
  
    while c_index < len(container) and t_index < len(truck):
        if truck[t_index] >= container[c_index]:
            result += container[c_index]
            c_index += 1
            t_index += 1
        else:
            c_index += 1
  
    print(f'#{tc} {result}')








'''
3
3 2
1 5 3
8 3

5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5

10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

#1 8
#2 45
#3 84
'''