# 내 풀이

# T = int(input())

# for test_case in range(1, T+1):

#     N = int(input())
#     a = list(map(int, input()))  # a = [4, 9, 6, 7, 9]
#     nums = 0
#     card_num = 0


#     for i in range(0, N):
#         for j in range(i):
#             if a[j] > a[j + 1]:   
#                 a[j], a[j + 1] = a[j + 1], a[j]      # a = [4, 6, 7, 9, 9]
#         for b in a:
#             if a.count(b) > nums:
#                 nums = b
#                 card_num = a.count(b)

#     print(f'#{test_case} {nums} {card_num}')





### 선생님 풀이

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))  # a = [4, 9, 6, 7, 9]


### 설명
'''
최대값의 인덱스를 찾는 방법 - 공부하기
배열 A가 있다고 치면 (i -> N)
max_v = A[0]
for i : 1 -> N-1
    if max_v < A[i]:
        max_v = A[i]

max_idx = 0
for i : 1 -> N-1:
    if A[max_idx] <= A[i]:
        max_idx = i
'''




 
