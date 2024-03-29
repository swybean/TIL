# 파이썬 데이터 구조1_6일차  



## 목차
1. Data Structure
2. 시퀀스 데이터 구조
3. 복사
---


## 1. 데이터 구조
> 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str, list, dict 등)  

#### 자료 구조
> 컴퓨터 공학에서는 '자료 구조'라고 함  
> 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것


#### 데이터 구조 활용
> 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기

---

### 1-1. 메서드
> 객체에 속한 함수  
> 객체의 상태를 조작하거나 동작을 수행

#### 메서드 특징
> **메서드는 클래스(class) 내부에 정의되는 함수**  
> (클래스는 파이썬에서 '타입을 표현하는 방법)

> **메서드는 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재**

#### 메서드 호출 방법
> 데이터 타입 객체.메서드( )  
> 예시 : 'hello'.capitalize( )  
'hello'가 객체, capitalize( )가 메서드

```python
# 문자열 메서드 예시
print('hello'.capitalize( )) # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
```

---

## 2. 시퀀스 데이터 구조


### 2-1. 문자열
#### 문자열 조회/탐색 및 검증 메서드


|메서드|설명|
|------|---|
|s.find(x)|x의 첫 번째 위치를 반환. 없으면 -1을 반환|
|s.index(x)|x의 첫 번째 위치를 반환. 없으면 오류 발생|
|s.isalpha( )|알파벳 문자 여부 (단순 알파벳이 아닌 유니코드 상 Letter)|
|s.isupper( )|대문자 여부|
s.islower( )|소문자 여부|


#### 주의사항
> s. 뒤에 is로 시작하는 메서드들은 리턴값이 Boolean(True, False)으로만 나온다. 

> s.isalpha( ), s.isupper( ), s.islower( )

---

#### 문자열 조작 메서드 (새 문자열 반환)
> 문자열 원본은 변경 불가능 하기 때문에  
 새로운 문자열을 **반환하는(만드는) 것**이다.


|  메서드  |  설명  |
|------|-----------|
|s.replace(old, new[,count])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars])|공백이나 특정 문자를 제거|
|s.split(sep=None, masplit=-1)|공백이나 특정 문자를 기준으로 분리|
|'separator'.join([iterable])|구분자로 iterable을 합침|
|s.capitalize( )|가장 첫 번째 글자를 대문자로 변경|
|s.title ()|문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환|
|s.upper( )|모두 대문자로 변환|
|s.lower( )|모두 소문자로 변환|
|s.swapcase( )|대<->소문자 서로 변경|

---


### 2-2. 리스트
#### 리스트 값 추가 및 삭제 메서드

|메서드|설명|
|------|---|
|L.append(x)|리스트 마지막에 항목 x를 추가|
|L.extend(m)|iterable(반복 가능한) m의 모든 항목들을 리스트 끝에 추가 (+=와 같은 기능)|
|L.insert(i, x)|리스트 인덱스 i에 항목 x를 삽입|
|L.remove(x)|리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거, 항목이 존재하지 않을 경우 ValueError|
|L.pop|리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거|
|L.pop(i)|리스트의 인덱스 i에 있는 항목을 반환 후 제거|
|L.clear( )|리스트의 모든 항목 삭제 (빈 리스트로 만든다.)|

---

---

#### 리스트 값 추가 및 삭제 메서드

|메서드|설명|
|------|---|
|L.index(x, start, end)|리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환|
|L.reverse( )|리스트의 순서를 역순으로 변경 (정렬X)|
|L.sort( )|**원본** 리스트를 **오름차순**으로 정렬 (매개변수 이용가능)|
|L.count(x)|리스트에서 항목 x의 개수를 반환|
---


## ※ 추가 정보  

##### 내림차순 정렬 하는 방법
> L.sort(revers=True) : 내림차순 정렬

---

##### 튜플 정렬하는 방법 -> 중요!
> 튜플(tuple)은 sort 메서드가 없다.  

> 따라서 함수 sorted()를 사용해야 한다.
###### 온라인 실습 예시 
###### (1442. 튜플 요소 추가와 정렬 Lv3)
```python
def sort_tuple(num):
    new_tuple = ()
    new_tuple = sorted(num)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)

```
---


## 3. 복사


### 3-1. 데이터 타입과 복사
> 파이썬에서는 데이터에 분류에 따라 복사가 달라짐  
> "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸  


#### 변경 가능한 데이터 타입의 복사
```python
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
```

#### 변경 불가능한 데이터 타입의 복사
```python
a = 20
b = a
b = 10

print(a) # 20
print(b) # 10
```
---

### 3-2. 복사 유형
1. 할당 (Assignment)
2. 얕은 복사 (Shallow copy)
3. 깊은 복사 (Deep copy)


#### 할당 복사 리스트 예시
> 할당 연산자(=)를 통한 복사는 해당 객체에 대한 **객체 참조를 복사**

```python
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)
# [1, 2, 3], [1, 2, 3]

copy_list[0] = 'hi'
print(original_list, copy_list)
# ['hi', 2, 3] ['hi', 2, 3]
```
---

#### 얕은 복사 리스트 예시
> 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
```python
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]

b[0] = 100
print(a, b) # [1, 2, 3] [100, 2, 3]
```


#### 얇은 복사의 한계
> 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우  

> a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨  
```python
a = [1, 2, [1, 2]]
b = a[:]
print(a, b) 
# [1, 2, [1, 2]] [1, 2, [1, 2]]

b[2][0] = 100
print(a, b) 
# [1, 2, [100, 2]] [1, 2, [100, 2]]
```
> 여기서 리스트 내부리스트인 [1, 2]는 주소가 새로 생성되지 않고 a, b가 모두 같은 주소를 바라보고 있기 때문이다.  
그래서 b를 변경해도 a의 출력도 변경된것.

---

#### 깊은 복사 리스트 예시
> 내부에 중첩된 모든 객체까지 새로운 주소를 참조하도록 함  
```python
import copy # 깊은 복사는 모듈 copy 제공

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_lsit)

deep_copied_list[2][0] = 100

print(original_list) # [1, 2, [1, 2]]
print(deep_copied_list) # [1, 2, [100, 2]]
```
---
### ※ 중요 !!!!
#### 얕은 복사와 깊은 복사의 차이점  
> 내부에 변경 가능한 객체(리스트 등)이 있는 경우 주소를 새로 생성하는지 여부  
> 얕은 복사 : 새 주소 생성 X  
> 깊은 복사 : 새 주소 생성 O

---

### 3-3. 참고

#### 문자열에 포함된 문자들의 유형을 판별하는 메서드  
> 모두 is로 시작하기에 결과값도 Boolean (True/False)로만 나온다.

##### 1. isdecimal()
> 문자열이 모두 숫자문자(0~9)로만 이루어져 있어야 True

> 외우지말고, 이런게 있구나만 하기  
    필요할때 구글링해서 찾아쓰기

##### 2. isdigit()
> isedcimal( )과 비슷하지만, 유니코드 숫자도 인식 (원숫자)

##### 3. isnumeric()
> isdigit( )과 유사하지만, 몇가지 추가적인 유니코드 문자들을 인식  
(분수, 지수, 루트 기호도 숫자로 인식)

---
강의 끝

---

# 오프라인 수업 내용

메서드 암기 잘해두기. -> 나중에 배울 지식의 기초가 된다.

얕은 복사, 깊은 복사 자세히 잘 공부하기.

면접 볼 때 참여한 프로젝트에서 내가 한 기능 외 다른 기능도 해봤다고 거짓말하지 말기. -> 금방 탄로남.



