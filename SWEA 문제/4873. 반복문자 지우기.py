T = int(input())
for test_case in range(1, T+1):
    arr = input()

    stack = []

    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{test_case} {len(stack)}')
