def pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -= 1
        return stack[top+1]

T = int(input())
for tc in range(1,T+1):
    a = input()
    size = len(a)
    stack = [0] * (size+1)
    top = 0
    for char in a:
        if top == -1:  # 왜 stack[top] ==0 으로 하면 안되는지??
            push(char,stack,size)

    if stack[top] != char:
        push(char,stack,size)

    elif stack[top] == char:
        pop()
print(f'#{tc} {top}')