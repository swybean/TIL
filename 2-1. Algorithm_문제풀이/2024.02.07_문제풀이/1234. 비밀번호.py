import sys
sys.stdin = open('input3.txt', 'r')

T = 10
for tc in range(1, T+1):
    N, S = input().split()
    S = list(S)
    i = 0

    while i < len(S)-1:
        if S[i] == S[i+1]:
            S.pop(i)
            S.pop(i)
            i = 0
        else:
            i += 1
    result = S

    print(f'#{tc} ', *result, sep='')




