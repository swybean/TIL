# 1월 16일 파이썬 기본문법_2일차

### **지난 수업 복습**
1. Data Types 
2. Text Sequence Types (str 문자열)  
---
### **오늘의 목차**  
1. Sequence Types  
2. Non-sequence Types
3. Other Types
4. Collection
5. Type Conversion
6. 연산자
---

## **1. Sequence Types**  

> 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형  
> str, list, tuple, range  

**복습 : Sequence Types 특징**  
1. 순서(Sequence)  
    값들이 순서대로 저장 (정렬x)  
    -> **순서만 있을뿐 정렬은 안된다! 중요**
2. 인덱싱(Indexing)  
    각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음  
3. 슬라이싱(Slicing)  
    인덱스 범위를 조절해 부분적인 값을 추출할 수 있음  
4. 길이(Length)  
    len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음  
5. 반복(Iteration)  
    반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음  

---

### **1-1. 리스트 (list)**  
> 여러 개의 값을 순서대로 저장하는 **변경 가능**한 시퀀스 자료형   
> ※ 문자열과 차이점 : 변경 가능 (가변성)  
> ※ 그 외 특징은 동일하다.  

**리스트 표현**  
- 0개 이상의 객체를 포함하며 데이터 목록을 저장  
-> 빈 리스트도 존재 가능 (예시 1번)  
- 대괄호 (**[ ]**)로 표기  
- 데이터는 어떤 자료형도 저장할 수 있음  
- 예시

```python
my_list_1 = []  
my_list_2 = [1, 'a', 3, 'b', 5]  
my_list_3 = [1, 2, 3, 'python', ['hello', 'world', '!!!']]  
```

---

**리스트의 시퀀스 특징**
```python
#순서
my_list = [1 'a', 3, 'b', 5]  

#인덱싱  
print(my_list[1]) # a  

#슬라이싱  
print(my_list[2:4]) # [3, 'b']  
print(my_list[:3]) # [1, 'a', 3]  
print(my_list[3:]) # ['b', 5]   
print(my_list[0:5:2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list)) # 5  
```
---

**중첩된 리스트 접근**  
: 출력 값 예상해보기
```python
my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]

print(len(my_list))  
print(my_list[4][-1])
print(my_list[-1][1][0])  
```

: 출력 값 확인
```python
my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]

print(len(my_list)) # 5
print(my_list[4][-1]) # !!!
print(my_list[-1][1][-]) # w
```
---

**리스트는 가변(변경 가능)**  
예시
```python
my_list = [1, 2, 3]
my_list[0] = 100

print(my_list) # [100, 2, 3]
``` 
---

### **1-2. 튜플 (Tuple)**  
> 여러 개의 값을 순서대로 저장하는 **변경 불가능**한 시퀀스 자료형   

**튜플 표현**  
- 0개 이상의 객체를 포함하며 데이터 목록을 저장
- 소괄호(**( )**)로 표기
- 데이터는 어떤 자료형도 저장할 수 있음
- 예시
```python 
my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)
```
---
**튜플의 시퀀스 특징**  
```python
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1]) # a

# 슬라이싱 
print(my_tuple[2:4]) # (3, 'b')
print(my_tuple[:3]) # (1, 'a', 3)
print(my_tuple[3:]) # ('b', 5)
print(my_tuple[0:5:2]) # (1, 3, 5)
print(my_tuple[::-1]) # (5, 'b', 3, 'a', 1)

# 길이
pritn(len(my_tuple)) # 5
```
---
**튜플은 불변 (변경 불가)**  
```python
my_tuple = (1, 'a', 3, 'b', 5)

# TypeError: 'tuple' object does not support item assigment
my_tuple[1] = 'z'
```
---

**튜플은 어디에 쓰일까?**  
- 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등 **개발자가 직접 사용하기보다 '파이썬 내부 동작'에서 주로 사용됨**  

예시
```python
x, y = (10, 20)

print(x) # 10
print(y) # 20

# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호 생략 가능
x, y = 10, 20
```
---

### **1-3. range**
> 연속된 정수 시퀀스를 생성하는 **변경 불가능**한 자료형  

**range 표현**  
- rnage(n)  
    0부터 n-1까지의 숫자의 시퀀스  
- range(n, m)  
    n부터 m-1까지의 숫자 시퀀스  

예시
```python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)
```
---

**range 표현**  
- 주로 반복문과 함께 사용 예정  
- 주로 리스트로 형 변환해서 사용  

예시
```python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능

print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
---


## **2. Non-Sequence Types**  


### **2-1. 딕셔너리 (dict)**  
> key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형    
> key : value 구성으로 이루어짐  
> 딕셔너리에 순서는 존재하지 않는다.  
> 인덱스로 접근이 불가능하다.  
> 딕셔너리의 모든 값은 key를 통해서 접근하고 얻어낸다.  

**딕셔너리 표현**
- key는 변경 불가능한 자료형만 사용 가능  
    (str, int, float, tuple, range ...)  
- value는 모든 자료형 사용 가능  
- 중괄호 (**{ }**)로 표기 
 
예시
```python
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3,]}

print(my_dict_1) # {}
print(my_dict_2) # {'key': 'value'}
print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}
```
---

**딕셔너리 사용**  
key를 통해 value에 접근  

예시  
```python
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3,]

# 값 변경
my_dict['apple'] = 100
print(my_dict) # {'apple: 100, 'list': [1, 2, 3]}  
```
--- 
**중복이 안된다**  
예시
```python
my_dict = {'apple': 12, 
           'list': [1, 2, 3], 
           'apple':100}

# apple이 중복된 상황

print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}

# 마지막으로 작성한 'apple': 100이 출력된다.
```
---



### **2-2. 세트 (set)**  
> 순서와 중복이 없는 변경 가능한 자료형  

**세트 표현**  
- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호 (**{ }**)로 표기   
- 빈 세트를 만들 때 **set()** 을 사용해야 한다.  
    -> dict에서 **{ }** 를 이미 사용하고 있기 때문에  
    -> 출력도 **set()** 으로 나온다.

예시  
```python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) # set()
print(my_set_2) # {1, 2, 3}
print(my_set_3) # {1}
```

**세트의 집합 연산**  
예시
```python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_2) # {3}  
```
---

## **3. Other Types** 
### **3-1. None**  
> 파이썬에서 **'값이 없음'** 을 표현하는 자료형  

**None 표현**  
```python
variable = None

print(variable) # None
```
---
### **3-2. Boolean** 
> 참(True)와 거짓(False)을 표현하는 자료형  

**불리언 표현**  
- 비교 / 논리 연산의 평가 결과로 사용됨
- 주로 조건 / 반복문과 함께 사용  


## **4. Collection**
> 여러 개의 항목 또는 요소를 담는 자료 구조  
    -> Sequence와 Non-sequence의 공통점     
    -> (변경 가능 여부 & 순서 여부)  
    -> 시퀀스 / 비시퀀스 차이는 순서 여부   
> str, list, tuple, set, dict  

**컬렉션 정리**  
- 컬렉션 변경가능여부 순서여부  
- 표만드는법찾아서 교재참고해서 만들기  






---

**불변과 가변의 차이**
```python
# 불변

my_str = 'hello'
my_str[0] = 'z'
# TypeError: 'str' object does not support item assignment
```
---
```python
# 가변

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list) # [100, 2, 3]
```
---

## **5. Type Conversion**  

**한줄 정리**  
- 암시적 형변환 : 파이썬이 자동으로 형변환
- 명시적 형변환 : 개발자가 직접 형변현  
-> 암시적을 제외한 모든 경우를 포함  


### **5-1. 암시적 형변환 (Implicit Type conversion)** 
> 파이썬이 자동으로 형변환을 하는 것  
> Boolean과 Numeric이 만나면 Boolean이 변경된다. 

**암시적 형변환 예시**
- Boolean과 Numeric Type에서만 가능   
```python
print(3 + 5.0) # 8.0
print(True + 3) # 4
print(True + False) # 1
```

---

### **5-2. 명시적 형변환 (Explicit Type conversion)**   
> 개발자가 직접 형변환을 하는 것   
> 암시적 형변환이 아닌 경우를 모두 포함  

**명시적 형변환 예시**  
- str -> integer : 형식에 맞는 숫자만 가능  
- integer -> str : 모두 가능  

예시
```python
print(int('1')) # 1

print(str(1) + '등') # 1등

print(float('3.5')) # 3.5

print(int(3.5)) # 3

#ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))
```
---

## **6. 연산자**  

### **6-1. 산술연산자**   
- ( - ) : 음수부호  
- ( + ) : 덧셈
- ( - ) : 뺄셈 
- ( * ) : 곱셈
- ( / ) : 나눗셈 
- ( // ) : 정수 나눗셈 (몫)
- ( % ) : 나머지
- ( ** ) : 지수 (거듭제곱)

---
### **6-2. 복합연산자**  
> 연산과 할당이 함께 이루어짐  
> 꼭 복합연산자를 사용할 필요는 없지만 알고는 있어야 한다.

- a += b  
: a = a + b

- a -= b  
: a = a - b

- a *= b  
: a = a * b

- a /= b  
: a = a / b

- a //= b  
: a = a // b

- a %= b  
: a = a % b

- a **= b  
: a = a ** b

---

**복합 연산자 예시**  
```python
y = 10
y -= 4
print(y) # 6

z = 7
z *= 2
print(z) # 14

w = 15
w /= 4
print(w) # 3.75

q = 20
q //= 3
print(q) # 6
``` 
---

### **6-3. 비교 연산자**
> 모든 결과는 True & False만 나온다.  
> 부등호 먼저 쓰고 = 쓰기  
> 프로그래밍에서 같음은 == 이다.  
> is : 같음
> is not : 같지 않음

---
**is 비교 연산자**  
- 메모리 내에서 같은 객체를 참조하는지 확인  
- == 는 동등성(equality), is는 식별성(identity)   
    -> 즉, is는 주소를 비교한다.  
- 값을 비교하는 == 와 다름  
- is : 같음  
- is not : 같지 않음  

```python
print(1 == True) # True 암시적 형변환이 일어났다

print(1 is True) # False 메모리 주소가 전혀 다르기 때문 

# 버그를 찾을 때는 is 를 사용하는게 좋다
# == 사용하면 찾기 힘들기 때문이다.
```

---

예시  
```python 
print(3 > 6) # False
print(2.0 == 2) # True
print(2 != 2) # False
print('HI' == 'hi') # False

# SyntaxWarning
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문
# is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용
print(2.0 is 2) # False
```
---

### **6-4. 논리 연산자**  
> and : 논리곱 , 두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가  
> or : 논리합, 두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가  
> not : 논리부정, 단일 피연산자를 부정

예시
```python
print(True and False) # False

print(True or False) # True

print(not True) # False

print(not 0) # True
```
---

예시2 : 비교 연산자와 함께 사용
```python
num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False


name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True
```



#### **단축평가**  
> 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작  

예시 : 0은 False다. 
```python
vowels = 'aeiou'

print(('a' and 'b') in vowels)
print(('b' and 'a') in vowels)

print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)

print(5 or 3)
print(3 or 0)
print(0 or 3)
print(0 or 0)
```
---

예시 결과
```python
vowels = 'aeiou'

print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0
```
---
**단축평가 동작**  
- and  
1. 첫번째 피연산자가 False인 경우, 전체 표현식은 False로 결정.  
두번째 피연산자는 평가되지 않고 그 값을 무시  
2. 첫번째 피연산자가 True인 경우, 전체 표현식의 결과는 두번째 피연산자에 의해 결정.  
두번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환  

- or  
1. 첫번째 피연산자가 True인 경우, 전체 표현식은 True로 결정.  
두번째 피연산자는 평가되지 않고 그 값을 무시  
2. 첫번재 피연산자가 False인 경우, 전체 표현식의 결과는 두번째 피연산자에 의해 결정.  
두번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환  

---

**단축평가 이유**
> 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함  

---

### **6-5. 멤버십 연산자** 
> 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인  

in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인  
not in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인  

---

### **6-6. 시퀀스형 연산자**
- +와 *는 시퀀스 간 연산에서 산술 연사자일때와 다른 역할을 가짐  
- ( + ) : 결합 연산자  
- ( * ) : 반복 연산자

예시  
```python
# Gildong Hong 
print('Gildong' + 'Hong')

# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])

# [1, 2, 1, 2]
print([1, 2] * 2)
```
---

## **연산자 우선순위 정리**  
- 암기 필요는 없으나 얼른 숙달하기  
@@ 피티 92쪽 보고 정리하기@@@@@@@@@@@@

우선순위|연산자|내용|
|---|---|---|
|높음|( )|소괄호 grouping|
|  |[ ]|인덱싱, 슬라이싱|
||**|거듭제곱|
||+, -|단항 연산자 양수/음수|
||*, /, //, %|산술 연산자|
||+, -|산술 연산자|
||<, <=, >, >=, ==, !=|비교 연산자|
||is, is not|객체 비교|
||in, not in|멤버십 연산자|
||not|논리 부정|
||and|논리 AND|
||or|논리 OR|


---


# !오프라인 수업 내용!  

**1. 단축평가 추가 설명**

예시 결과
```python
vowels = 'aeiou'

print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0
```
논리 연산자 결과는 원래 무조건 T/F로만 나와야 한다.  

print가 붙은 단축평가에서는  
결과값이 아닌 평가한 피연산자 값을 기준으로 생각한다.  

예시 : print(('a' and 'b') in vowels) # False  
'a' and 'b'에서 단축평가하면 마지막 평가가 b다.  
따라서 이것의 리턴값은 b이다.  
b가 vowels에 없기 때문에 False가 나온 것이다.  

print(('b' and 'a') in vowels) # True  
단축평가하면 마지막 평가는 a다.  
따라서 이것의 리턴값은 a이다.  
a가 vowels에 있기 때문에 True가 나온 것이다.  


먄약 'a' or 'b'면 a가 True면 b는 평가할 필요가 없기에 평가 후 리턴값은 a이다.  

---

**전부**  
- 리스트에서 변경뿐만이 아니라 추가하거나 제거하는 기능도 있다.  
- 추후 배울 예정 (일단 알려주면 append?를 사용)  

---

- 튜플은 불변(변경 불가)이어도 인덱싱과 슬라이싱은 된다.  
- 슬라이싱 : 해당 부분을 복사해서 가져오는거라 원본은 그대로 남아있기에 가능한 것  

--- 

- range 조금 어렵다  
- 굉장히 많이 쓰여서 설명을 안 할 수도 없다.   
- **정수** 시퀀스를 생성하는 것  
- 결과값에 대해서 얘기를 해보겠다.  
- range(스타트넘버, 엔드넘버, 스텝)  으로 구성  
- range(0, 4) = 0, 1, 2, 3
- 근데 list(0, 1, 2, 3, 4)를 하면 [0, 1, 2, 3, 4,]
- 둘이 같은데 굳이 구분해서 써야할까?  
- 메모리와 관련되어 있다.  
- 10의 10승 같은 큰 정수를 만든다고 치면  
- 리스트는 해당 정수를 모두 만들어버리고 메모리에 전부 다 올린다.  
- 그러면 컴퓨팅 파워와 어마어마한 비용이 든다.  
- 이걸 막는게 range 이다.  
- range는 여기부터~여기까지 만드는구나라는 정보만 올리고 필요한 정수가 생기면 해당 정수만 만들어서 메모리에 가져다 쓰고 버린다.  
- 비용이 훨씬 더 적게 든다. (range가 만들어진 이유)
- **range가 만들어진 목적 : 메모리의 효율적 사용, 타이핑을 줄이기**

---
- 피피티 range 부분 찾아보기 맨위 유알엘, 노란박스 ,글 순서대로 있는 부분  
- "많은 경우에 range() 가 돌려준 객체는 리스트인 것처럼 동작하지만 ... 함수 list() 도 그런 것입니다"  

---

- set을 사용하는 이유
- 예를 들어 백만개의 정보에서 중복이 있는지 찾을 때 사용  
- 새로운 정보를 추가할 때도 기존 정보에 중복이 있다면 추가되지 않는다.
- 이렇게 중복되지 않는 자료구조를 만들 때 사용한다.  

---

# 실습 과제 풀이  
## 2986. 딕셔너리 활용하기
```python
title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.
data = {'과목': 'python', '구분': '실습', '단계': 2, '문제번호': 3251, '이름': None, '일차': 22}

print(data)


data['단계'] = str(data['단계']) + '단계'
# str(data['단계'])로 2를 불러와서 문자열로 바꾼뒤
# '단계'를 추가해서 '2단계'가 출력되도록 한다.

data['이름'] = title

data['일차'] = 22
data['일차'] -= 20


print(data)
```

---

## 1676. 도서 목록 정리하기2 레벨4
```python
information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]


information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]


for key, value in information.items() :
    print(key, ':', value)
# 첫줄은 information에 있는 items(키+벨류)를 키, 벨류로 나누라는 뜻이다.
# print 줄은 찢어둔 key, value를 이용해서 (key, :, value) 순으로 출력하라는 뜻이다.

```
---
## 1677. 깊은 복사와 indexing 접근 레벨5
```python
catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

backup_catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

catalog[-1][0] = '성공을 향한 한 걸음'
catalog[-1][1] = '내 삶의 변화'
catalog[-1][2] = '목표 달성의 비밀'



''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(backup_catalog == catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

```