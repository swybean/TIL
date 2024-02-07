# 1 1 0 0 0 1 0 

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    S = list(input())
    sss = []

    for i in S:
        if i == '(' or i == '{':
            sss.append(i)

        if i == ')' or i == '}':
            if sss == []:
                break
            else:
                sss.pop()
            
    if sss == []:
        print(f'#{tc}', '1')
    else:
        print(f'#{tc}', '0')

# 괄호 짝 순서도 중요함 순서 조건도 추가
        
T = int(input())
for tc in range(1, T+1):
    S = list(input())
    sss = []
    result = 1

    for i in S:
        if i == '(' or i == '{':
            sss.append(i)

        if i == ')' or i == '}':
            if sss == []:
                break
            else:
                sss.pop()
            
    if sss == []:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')
        


'''
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 16개의 테스트케이스 중 3개가 맞았습니다.)

런타임 에러가 발생하였습니다. 런타임 에러로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
Error Message :
Runtime Error!


2차 오답
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 16개의 테스트케이스 중 9개가 맞았습니다.)






# 팝 프롬 엠티 리스트
())) 같은 경우 ()제거됐는데 )나왔다고 빈리스트에서 또 뭔갈 제거하려고 해서 오류남

추가 tc, T 값 7로 증가시켜야함
())
(()
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))

선생님 추가 문제
4
())
(()
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))

추가문제까지 출력값은
1
1
0
1
0
1
0
'''
# or i == ')' or i == '{' or i == '}'