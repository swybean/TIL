# 피보나치 수열 탑다운(재귀함수) 방식
d = [0] * 100

def fibo(x):
    # 종료 조건 (1또는 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


# 호출되는 함수 확인 코드
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)

# 피보나치 수열 보텀업(반목문) 방식

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0] * 100
# 첫 번째, 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
# 피보나치 함수 반복문으로 구현 (보텀업 방식)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])

