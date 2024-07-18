# 시간초과 떠서 실패
# N = int(input())

# arr = []    # 문자를 저장할 리스트 생성

# for _ in range(N):  
#     str1 = input()  # 문자 N만큼 반복 입력
#     if str1 not in arr:   # 만약 arr에 해당 문자가 없으면 추가하기 (중복 제외하기 위함)
#         arr.append(str1)

# # 버블 정렬을 사용하여 문자열을 글자 수가 적은 순서대로 정렬
# for _ in range(len(arr)):
#     for i in range(len(arr) - 1):
#         if len(arr[i]) > len(arr[i + 1]):
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         # 만약 글자수가 같다면 사전순으로 정렬 (파이썬에서는 부등호로 사전순 비교 가능)
#         if len(arr[i]) == len(arr[i + 1]):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print(arr)


N = int(input())

arr = []    # 문자를 저장할 리스트 생성

for _ in range(N):  
    str1 = input()  # 문자 N만큼 반복 입력
    if str1 not in arr:   # 만약 arr에 해당 문자가 없으면 추가하기 (중복 제외하기 위함)
        arr.append(str1)

arr.sort()          # 사전순 정렬
arr.sort(key=len)   # 글자수 정렬

for i in arr:
    print(i)