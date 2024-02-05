import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

N = list(map(int, input().split()))

for i in range(T):
    for j in range(i + 1, T):
        if N[i] < N[j]:
            N[i], N[j] = N[j], N[i]  



print(N[T//2])




