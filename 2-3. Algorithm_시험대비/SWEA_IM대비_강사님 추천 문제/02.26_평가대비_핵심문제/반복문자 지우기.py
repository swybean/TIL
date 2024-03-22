
T = int(input())
for tc in range(1, T+1):
    arr = input()
    stack = []

    for i in arr:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')



