def push(n):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0] * 10    # 최대 10개 push


top += 1            # push(10)
stack[top] = 10

top += 1            # push(20)
stack[top] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])

# 10, 20, 30 순으로 넣었으나 출력은 30, 20, 10 순으로 나옴