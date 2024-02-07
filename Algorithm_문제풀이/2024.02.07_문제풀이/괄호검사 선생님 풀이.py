'''
ABCCB

ch = 방금 스택에 넣은 것을 저장할 변수

if 1) 스택이 비어있으면 push

if 2) 스택이 비어있지 않으면
스택의 탑원소(peek)과 비교하는데 (stack[-1])

2-1) 마지막원소와 다르면 
push

2-2) 마지막 원소와 같으면
pop해서 스택에 있던 것을 버린다 (비교대상이었던 다음 b, c는 애초에 넣지 않음)

'''

'''
# 괄호검사 선생님 풀이
        
T = int(input())
for tc in range(1, T+1):
    s = input()
    ans = 1
    
    for x in s:
        if x in '{}()': # 괄호인 경우
            # 스택이 비어있거나 여는 괄호면 푸시()
            # 닫는 괄호면
                # 1) 스택이 비어있으면 오류 break ans=0
                # 2) 팝()해서 짝이 맞지않으면 오류 break abs=0
                # 3) 짝이 맞으면 계속
    else:   # 주어진 입력에 대한 확인이 끝난경우
                #4) 스택이 비어있지 않으면(여는 괄호) 오류 ans=0 
'''

# 선생님 풀이
import sys
sys.stdin = open('input1.txt', 'r')

op = {')':'(', '}':'{'}   

T = int(input())
for tc in range(1, T+1):
    s = input()
    ans = 1
    stack = []
    
    for x in s:
        # if x in '{}()': # 괄호인 경우 (해당 if문에서 괄호를 제외한 문자는 걸러진다.)
        # 위에 if문을 살리려면 밑에 elif x in '})':를 else:로 바꿔야 한다.
        if x in '{(':   # 그중에서 여는 괄호면 push
            stack.append((x))
        # 닫는 괄호면 (위 if문 외에는 전부 닫는 괄호니까)
        elif x in '})':
            if not stack:   # 스택이 비어있으면 오류(break) ans=0
                ans = 0
                break
            else:   # 스택에 여는 괄호가 있으면   
                t = stack.pop()    
                if t != op[x]:  # pop()해서 짝이 맞지않으면 오류(break) ans=0
                    ans = 0
                    break
                # 3) 짝이 맞으면 계속

    else:   #주어진 입력에 대한 확인이 끝난경우
        if stack:   #4) 스택이 비어있지 않으면(여는 괄호가 있으면) 오류 ans=0 
            ans = 0        
    
    print(f'#{tc} {ans}')



        


