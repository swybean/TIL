import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    txt = input()
    N = len(txt)
    ans = 1                
    for i in range(N//2):  
        if txt[i] != txt[N-1-i]:   
            ans = 0
            break
    print(f'#{tc} {ans}')  

  

  