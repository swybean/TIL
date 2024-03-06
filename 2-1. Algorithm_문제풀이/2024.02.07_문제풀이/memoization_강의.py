'''
def fibo(n):
    global cnt
    cnt +=1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
print(fibo(7), cnt) #13, 41
'''

'''
memo 위한 모두 0인 배열할당
memo[0] =0, memo[1] =1 할당
'''

def fibo_memo(n):
    global cnt
    cnt += 1
    if n != 0 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]

n= 7
cnt = 0
memo = [0] *(n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n), cnt) #13, 13