def f(i, k):
    if i == k:
        print('end')
    else:
        f(i+1, k)

f(0, 1000)  # 재귀호출이 너무 많다고 출력 안된다.




