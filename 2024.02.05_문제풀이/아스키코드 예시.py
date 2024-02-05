import sys
sys.stdout = open('newline.txt', 'w') 
# newline이라는 이름의 txt 파일에 출력값을 저장해서 생성한다.

print('a\nb')


'''
\n은 아스키 코드에서 0D 0A (CR LF)로 보인다.
CR : Carriage Return
LF : Line Feed

a\nb 이거는 아스키 코드로 보면
61 0D 0A 62 0D 0A로 나오는 것이다.



'''




