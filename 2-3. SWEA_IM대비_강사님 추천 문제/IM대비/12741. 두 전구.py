T = int(input())

result = []

for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())
    jungu = min(B, D) - max(A, C)

    if jungu < 0:
        jungu = 0
    result.append(jungu)
 
for test_case in range(1, T+1):
    print(f'#{test_case} {result[test_case-1]}')