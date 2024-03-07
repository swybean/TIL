# 시퀀스 데이터 구조 - 문자열 실습 (18쪽)
"""
my_str = 'banana'
"""

# find
"""
print(my_str.find('a'))
print(my_str.find('z'))
"""
# a와 z가 있는 인덱스 위치를 반한해준다.
# 결과값은 a는1, 
# z는 없기 때문이 -1이 반환되어 나옴


# index
"""
print(my_str.index('a'))
print(my_str.index('z'))
"""
# a의 결과값은 1 나옴
# z는 없기 때문에 오류가 나옴

# isalpha
"""
string1 = 'Hello'
string2 = '123'
print(string1.isalpha())
print(string2.isalpha())
"""

# string1은 True,
# string2는 False 가 나옴

# ~~~~~~~~~~~끝~~~~~~~~~~~
# ~~~~~~조작 메서드 시작~~~~~~~


# 문자열 조작 메서드

# 1번. repalc(old, new[,count])
# [,count]는 선택인자라는 뜻
# 넣어도 되고 안넣어도 된다 라는 뜻
# '베커스-나우르 표기법' 참고하기

"""
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) 
"""

# 결과 : Hello, Python!


# 2번. 리스트 값 추가 및 삭제 메서드

my_list = [1,2,3]

# append
"""
my_list.append(4)
print(my_list)
"""

# extend
"""
my_list.extend([4, 5, 6])
print(my_list)
"""







