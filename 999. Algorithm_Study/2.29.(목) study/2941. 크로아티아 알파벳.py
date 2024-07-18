coratia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str1 = input()  # 문자열 입력
result = 0      # 알파벳 개수 셀 변수
i = 0           # 인덱스 변수

while i < len(str1):
    if str1[i:i+3] in coratia:
        result += 1
        i += 3
    elif str1[i:i+2] in coratia:
        result += 1
        i += 2
    else:
        result += 1
        i += 1
    
print(result)


'''
ljes=njak
lj e s= nj a k
답 : 6

'''
