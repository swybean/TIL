# class 확인 실습 (교재 10쪽)
print(type('1'))
print(type([1, 2]))
print(help(str))
print(help(list))

#help(str, list) 해서 나온 목록 중 __로 
#시작하는 건 '매직 메서드'라고 한다.



def append():
    pass

append() # 호출
'''
리스트.append() # 메서드 호출
데이터타입 객체.메서드()'''

# append 라는 메서드는 리시트라는 객체에서만 사용이 가능하다. 
# str 등 다른 곳에서는 사용 불가



