


    
# # 성재형
# def pascal(N):
#     if N == 1:
#         return [1]
#     elif N == 2:
#         return [1, 1]
#     else:
#         arr = []
#         for i in range(0, N-2):
#             arr2 = pascal(N-1)
#             arr.append(arr2[i] + arr2[i+1])
#         return [1] + arr + [1]
 
# Test = int(input())
 
# for test in range(1, Test+1):
#     N = int(input())
#     print(f'#{test}')
#     for x in range(1, N+1):
#         num = pascal(x)
#         print(*num)


# # 지웅이형 풀이
# def my_pascal(N):
#     base_matrix = [[1], [1,1]]
#     if N == 1:
#         return [[1]] # N == 1인 경우
#     elif N == 2:
#         return [[1], [1,1]] # N == 2인 경우
#     else: # 3 이상의 N인 경우
#         before_layer = 1 # 이 경우 index 2부터 계산에 활용해야 하므로
#         for num in range(0,N-2): # 반복을 할껀데, Nsize의 경우 N==1, N==2를 제외한 숫자만큼 반복해야 한다.
#             append_pascal = [] # 삼각형 확장에 활용할 list
#             for i in range(before_layer): # 전 layer을 활용할 것이고
#                 append_pascal = append_pascal + [base_matrix[before_layer][i] + base_matrix[before_layer][i+1]] # 전 layer의 index만큼 이를 반복한다.
             
#             before_layer += 1 # 반복이 끝나면 층 index를 하나 올리고
#             append_pascal = [1] + append_pascal + [1] # 양쪽에 1을 세운다
#             base_matrix = base_matrix + [append_pascal] # 이를 base_matrix에 추가해 삼각형을 확장한다. 이후 이를 반복한다.
             
#         return base_matrix
 
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     result = my_pascal(N)
#     print(f"#{tc}")
#     for i in range(N):
#         print(*result[i])


# # 신희진 누나 풀이
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = list([0] * i for i in range(1,N+1))
#     for i in range(N):
#         arr[i][0],arr[i][-1] = 1,1
#     for i in range(1,N-1):
#         for j in range(0,i):
#             arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
 
#     print(f'#{tc+1}')
#     for i in arr:
#         print(*i)


# 내 풀이

import sys
sys.stdin = open('input4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list([0] * i for i in range(1, N+1))

    for i in range(N):
        arr[i][0], arr[i][-1] = 1, 1

    for i in range(1, N-1):
        for j in range(0, i):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
            
    print(f'#{tc}')
    for i in arr:
        print(*i)


