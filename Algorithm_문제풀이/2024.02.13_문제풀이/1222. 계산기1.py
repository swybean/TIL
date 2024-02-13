T = 10

# 테스트 케이스 순회
for tc in range(1, T+1):
    N = int(input())    # 문자열 계산식 길이 N 입력
    arr = list(input()) # 문자열 계산식 입력
    num = []    # 숫자를 저장할 리스트 num 생성
    plus = []   # 연산자를 저장할 리스트 plus 생성

    # arr에서 i를 순회
    for i in arr:
        # i가 숫자라면 num 리스트에 저장
        if i.isdigit():
            num.append(i)
        # i가 연산자 +라면 plus 리스트에 저장
        elif i == '+':
            plus.append(i)
    
    result = num + plus # num, plus를 합친 리스트 result 생성
    stack = []          # 빈 stack 생성
    # result에서 i를 순회
    for i in result:
        # i가 숫자라면 stack에 추가
        if i.isdigit():
            stack.append(i)
        # i가 연산자 +라면
        if i == '+':
            # 가장 최근에 삽입된 2개의 숫자를 꺼내서 더한다.
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b + a)
    # 테스트케이스 번호와 스택에 남은 마지막 숫자(최종합계)를 출력한다.
    print(f'#{tc} {stack.pop()}')
