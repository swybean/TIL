T = 10
 
for tc in range(1, T+1):
    N = int(input())  # 테스트 케이스의 길이
    arr = input()    # 문자열 계산식
    
    stack = []  # 연산자를 저장할 스택
    postfix = ''  # 후위 표기식을 저장할 변수

    # 연산자의 우선순위를 정의
    precedence = {'+': 1, '*': 2}

    # 문자열 계산식을 순회하면서 후위 표기식으로 변환
    for i in arr:
        if i.isdigit():  # 피연산자인 경우 바로 후위 표기식에 추가
            postfix += i
        else:  # 연산자인 경우
            # 스택이 비어있지 않고, 스택의 top에 있는 연산자의 우선순위가 더 높은 경우
            while stack and precedence.get(stack[-1], 0) >= precedence.get(i, 0):
                postfix += stack.pop()  # 스택의 top에 있는 연산자를 pop하여 후위 표기식에 추가
            stack.append(i)  # 현재 연산자를 스택에 push

    # 스택에 남아 있는 모든 연산자를 후위 표기식에 추가
    while stack:
        postfix += stack.pop()

    # 후위 표기식을 계산하여 결과를 출력
    stack = []
    for token in postfix:
        if token.isdigit():  # 피연산자인 경우 스택에 push
            stack.append(int(token))
        else:  # 연산자인 경우 피연산자들을 pop하여 연산 후 결과를 스택에 push
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                result = num1 + num2
            else:   # 연산자가 *인 경우
                result = num1 * num2
            stack.append(result)

    # 스택에 남아있는 결과가 최종 계산 결과
    result = stack.pop()

    print(f"#{tc} {result}")

