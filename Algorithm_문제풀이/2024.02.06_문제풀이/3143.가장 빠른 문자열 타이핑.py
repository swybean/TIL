import sys
sys.stdin = open('input1.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     A, B = list(map(str, input().split()))
#     N = len(A)
#     M = len(B)
#     Bnum = 0

#     for i in range(N):
#         if B in A:
#             Bnum += 1
#             Anum = N - (M * Bnum)
#             total = Bnum + Anum
    
#         print(total)



    
T = int(input())
 
for tc in range(1, T + 1):
    A, B = map(str,input().split())
    result = A.replace(B, ' ')
    print(f'#{tc} {len(result)}')
