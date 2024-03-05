
arr = list(map(int, (input())))  # 문자열
N = len(arr)

result = 0  # 결과값
now = 0     # 연산한 값 저장할 변수

for i in range(1):
    if arr[i] < 2 or arr[i+1] < 2:
        now = arr[i] + arr[i+1]
    elif arr[i] >= 2 and arr[i+1] >= 2:
        now =  arr[i] * arr[i+1]

for i in range(2, N):
    if arr[i] >= 2:
        now = now * arr[i]
    elif arr[i] < 2:
        now = now + arr[i]

print(now)



