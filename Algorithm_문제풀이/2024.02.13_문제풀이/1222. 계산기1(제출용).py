T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    num = []
    plus = []

    for i in arr:
        if i.isdigit():
            num.append(i)
        elif i == '+':
            plus.append(i)
    
    result = num + plus
    stack = []
    for i in result:
        if i.isdigit():
            stack.append(i)
        if i == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b + a)
    print(f'#{tc} {stack.pop()}')











