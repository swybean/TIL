'''
0과 1의 개수를 비교
더 적은 숫자를 찾음
(만약 1이 더 적다면)

전체 순환하면서 arr[i]가 1인 인덱스 번호를 저장
해당 인덱스 번호를 전부 0으로 바꿈
'''

arr = list(map(int, input()))   # 문자열 입력
N = len(arr)

zero_count = 0
one_count = 0

for i in range(N):
    if arr[i] == 0:
        zero_count += 1
    elif arr[i] == 1:
        one_count += 1

counts1 = 0
if zero_count > one_count:
    for i in range(N-1):
        if arr[i] != arr[i+1]:
            if arr[i+1] == 1:
                counts1 += 1
    result = counts1

counts0 = 0
if zero_count < one_count:
    for i in range(N-1):
        if arr[i] != arr[i+1]:
            if arr[i+1] == 0:
                counts0 += 1
    result = counts0

print(result)


