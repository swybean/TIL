import sys
sys.stdin = open('input2.txt', 'r')



T= int(input())
for tc in range(1, T+1):
    txt = list(input())
    i = 0

    while i < len(txt)-1:
        if txt[i] == txt[i+1]:
            txt.pop(i)
            txt.pop(i)
            i = 0
        else:
            i += 1
    result = len(txt)
    print(f'#{tc} {result}')





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
T = int(input())
 
for tc in range(1, T+1):
    s = input()
    s = list(s)
    chk_re = 1
    i = 0
 
    while i < len(s)-1:
 
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = 0
        else:
            i += 1
 
    len_fix = len(s)
    print(f'#{tc} {len_fix}')
'''
