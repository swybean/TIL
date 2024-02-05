# **파이썬 데이터 구조2_7일차**

## **복습**
1. Data Structure (데이터 구조)
2. 메서드 (str, list)

## **목차**
1. 비시퀀스 데이터 구조 (set, dict)
2. 해시 테이블 (Hash Table)
---


## **비시퀀스 데이터 구조**
> 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (set, dict 등)  

### **1. 세트 (set)**
> 고유한 항목들의 정렬되지 않은 컬렉션  
> (중복이 없고, 비시퀀스인(순서없는) 컬렉션)

#### **세트 메서드**

|  메서드  |  설명  |
|------|-----------|
|s.add(x)|세트 s에 항목 x추가. 이미 x가 있다면 변화 없음|
|s.clear( )|세트 s의 모든 항목을 제거|
|s.remove(x)|세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error|
|s.pop( )|세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거|
|s.discard(x)|세트 s에서 항목 x를 제거|
|s.update(iterable)|세트 s에 다른 iterable 요소를 추가|
---

&nbsp;



#### **세트의 집합 메서드**  **(중요!!!)**

|  메서드  |  설명  | 연산자  |
|------|------|------|
|set1.difference(set2)|set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환|set1 - set2|
|set1.intersection(set2)|set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환|set1 & set2|
|set1.issubset(set2)|set1의 항목이 모두 set2에 들어있으면 True를 반환|set1 <= set2|
|set1.issuperset(set2)|set1가 set2의 항목을 모두 포함하면 True를 반환|set1 >= set2|
|set1.union(set2)|set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환|set1 : set2|
---
> 메서드와 연산자는 결과값은 동일하다.  
(연산자 사용하는게 편하다.)
 ---

```python
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}

print(set1.difference(set2))    # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))      # False
print(set1.issuperset(set2))    # False
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7 , 9}

```
---

&nbsp;

### **2. 딕셔너리 (dictionary)**

> 고유한 항목들의 정렬되지 않은 컬렉션  
(중복이 없고, 비시퀀스인(순서없음) 컬렉션)

### **딕셔너리 메서드**
> **매우 중요!!! 반드시 알아야 함 기본이다.**

|  메서드  |  설명  |
|------|-----------|
|D.clear( )|딕셔너리 D의 모든 키/값 쌍을 제거|
|D.get(k[,default])|키 K에 연결된 값을 반환 (키가 없으면 None 혹은 기본값(default)을 반환)|
|D.get(k, v)|키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환|
|D.keys( )|딕셔너리 D의 키를 모은 객체를 반환|
|D.values( )|딕셔너리 D의 값을 모은 객체를 반환|
|D.items( )|딕셔너리 D의 키/값 쌍을 모은 객체를 반환|
|D.pop(k)|딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 오류)|
|D.pop(k, v)|딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 v를 반환)|
|D.setdefault(k)|딕셔너리 D에서 키 K와 연결된 값을 반환|
|D.setdefault(k, v)|딕셔너리 D에서 키 K와 연결된 값을 반환 / K가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환|
|D.update(other)|other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체  other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가|

---

#### **교재 보면서 강사님 온라인강의 실습**
```python
person = {'name': 'Alice', 'age': 25}


# 딕셔너리 클리어 실습
person.clear()
print(person)    # 빈 dict가 나옴 {}


# 딕셔너리 겟 실습
print(person['name'])
print(person.get('name'))  # 같은 코드 : print(person['name'])
print(person.get('country'))  # 키가 없을 경우에는 위 코드는 에러가 뜸
print(person.get('country', '키가 없다'))


# keys() 실습
print(person.keys()) # dict_keys(['name', 'age'])
# 여기서 위 프린트 출력물이 []로 묶여 있는걸 보고 깨달아야 한다.
# key의 모임이구나, 반복이 가능하구나 
for k in person.keys():
    print(k)  # name \n age

# values() 실습
print(person.values())

for v in person.values():
    print(v) 


# items() 실습
print(person.items())

for k, v in person.items():
    print(k, v) 


# .pop(key[,default]) 실습
print(person.pop('age'))   # 25
print(person)   # {'name': 'Alice'}
print(person.pop('country', None))   # None
print(person.pop('country'))   # KeyError


# .setdefault(key[,default]) 실습
print(person.setdefault('country', 'KOREA'))   # KOREA
print(person)   # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# .update([other]) 실습
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)
# {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=50)
print(person)
# {'name': 'Jane', 'age': 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person)
# {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
```
---


&nbsp;

### **3. 해시 테이블 (Hash Table)**
> **해시 함수**를 사용하여 **변환한 값**을 **색인(index)** 으로 삼아 **키(key)와 데이터(value)를 저장**하는 자료구조  

> 데이터를 효율적으로 저장하고 **검색**하기 위해 사용  


#### **해시 테이블 원리**
> 키를 해시 함수를 통해 해시 값으로 변환하고,  
이 해시 값을 인덱스로 사용하여 데이터를 저장 및 검색

> 데이터 검색이 매우 빠르게 이루어짐

```python
dict = {
    'Jhon':'521-1234'
    'Lisa': '521-8976'
    'Sandra': '521-9655'
}

# Lisa의 주소를 얻고 싶을 때
dict.get('Lisa') #를 보통 사용한다.

# 그런데 아래와 같은 경우일 때
list - [
    {'Jhon':'521-1234'},
    {'Lisa': '521-8976'},
    {'Sandra': '521-9655'}
]

# 이런 list 안에 데이터가 3개가 아닌 1만 개가 있다고 하면 한 방에 찾기 힘들다.

# 근데 위 dict 예시에서는 한 번에 리사를 찾을 수 있다.
# 키를 입력하면 해시 함수를 거쳐서 데이터로 가기 때문에.
# 순서는 상관없기 때문에 set, dict에서 쓰이는 것
# 해시 함수도 '함수'이기에 key가 input이고, 데이터가 output이다.
# 교재 42쪽 그림 추가하기 @@@@@@@@@@@@@@@@@@@
```


---

### **해시 (Hash)**
> **임의의 크기를 가진 데이터**를 **고정된 크기의 고유한 값**으로 변환하는 것  

> 이렇게 생성된 고유한 값은 주로 해당 데이터를 **식별**하는 데 사용될 수 있음    
 > -데이터를 **고유하게 식별**  
 > -일종의 "지문" 역할

> 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨 

---

### **해시 함수 (Hash Function)**
> **임의의** 길이의 데이터를 입력 받아 **고정된** 길이의 데이터(해시 값)을 출력하는 함수  

> 주로 해시 테이블 자료구조에 사용되며,  
**매우 빠른 데이터 검색**을 위한 컴퓨터 소프트웨어에서 유용하게 사용

---

#### **set의 요소 & dictionary의 키와 해시테이블 관계**
> 파이썬에서 **set의 요소**와 **dict의 key**는 **해시 테이블**을 **이용**하여 **중복되지 않는 고유한 값을 저장**함

> set 내 각 요소는 **해시 함수를 통해 해시 값으로 변환**되고, 이 **해시 값을 기반으로 해시 테이블에 저장됨**

> dict의 key는 고유해야 하므로, key를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장  
(따라서 dict의 key는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음)

---

#### **파이썬에서의 해시 함수**
> 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐  

> 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름  

---

#### **파이썬에서의 해시 함수 - 정수**
> 같은 정수는 **항상 같은 해시 값**을 가짐  
(정수 값 자체가 곧 해시 값)

> 해시 테이블에 정수를 저장할 때 효율적인 방법

> 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨
```python
print(hash(1)) # 1
print(hash(1)) # 1
```
---

#### **파이썬에서의 해시 함수 - 문자열**
> 문자열은 **가변적인 길이**를 갖고 있고,  
문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산  
(반환 값이 매번 다름)

> 이로 인해 **문자열의 해시 값은 실행 시마다 다르게 계산**   
(실행마다 문자열이 해시 테이블에 어떻게 배치되어서 어떤 인덱스(1번? 0번? 23번?)을 받을지 모르기 때문에)
```python
print(hash('a')) # 실행시마다 다름 
print(hash('a')) # 실행시마다 다름
```
---

#### **set의 pop 메서드의 결과와 해시 테이블의 관계**
> pop 메서드는 set에서 임의의 요소를 제거하고 반환

> 실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"(random)가 아니라 **"임의"라는 의미에서 "무작위"**  

> By "arbitrary" the docs don't mean "random"

> 해시 테이블에 나타나는 순서대로 반환하는 것

---

#### **hashable**
> hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체

> 대부분의 불변형 데이터 타입은 hashable

> 단, tuple의 경우 불변형이지만 해시 불가능한 객체(가변 데이터)를 참조할 때 tuple 자체도 해시 불가능해지는 경우가 있음

---

#### **hashable과 불변성 간의 관계**
> 해시 테이블의 키는 **불변**해야 함  
(객체가 생성된 후에 그 값을 변경할 수 없어야 함)

> 불변 객체는 해시 값이 변하지 않으므로 **동일한 값에 대해 일관된 해시 값**을 유지할 수 있음

> 단, **"hash 가능하다 != 불변하다"**

---

#### **가변형 객체가 hashable 하지 않은 이유**
> **값이 변경**될 수 있기 때문에 **동일한 객체에 대한 해시 값이 변경될 가능성**이 있음  
(해시 테이블의 무결성 원칙 유지 불가)

> 가변형 객체가 변경되면 해시 값이 변경되기 때문에,  
**같은 객체에 대한 서로 다른 해시 값**이 반환될 수 있음  
(해시 값의 일관성 원칙 유지 불가)

```python
#TypeError: unhashable type: 'list'
print(hash([1,2 , 3]))

#TypeError: unhashable type: 'list'
my_set = {[1,2,3], 1, 2, 3, 4, 5}

#TypeError: unhashable type: 'set'
my_dict = {{3,2}: 'a'}
```
---

#### **hashable 객체가 필요한 이유**
1. 해시 테이블 기반 자료 구조 사용  
1-1. set와 dict의 키  
1-2. 중복 값 방지  
1-3. 빠른 검색과 조회

2. 불변성을 통한 일관된 해시 값

3. 안정성과 예측 가능성 유지
---
&nbsp;

# 오프라인 수업

set은 잘 쓰면 엄청 편하고 좋다.

dict는 파이썬에서 두 번째로 중요한 것. (첫 번째는 list)  
-> 파이썬이 느린 이유는 선형 검색을 하기 때문.  
-> 해시를 통해서 검색을 빠르게 할 수 있음.  


박봉주 트랙대표(파이썬)
오전 11:45
https://docs.python.org/3/library/stdtypes.html#dict.update

## 오늘 과제 4레벨 꼭 잘 공부해두기. 월말이 이런식으로 나옴

