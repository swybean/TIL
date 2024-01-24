# **파이썬 OOP-1_8일차**

## **목차**
0. 절차 지향 프로그래밍
1. 객체 지향 프로그래밍
2. 객체
3. 클래스
4. 메서드
---


## **0. 절차 지향 프로그래밍 (Procedural Programming)**
> 프로그램을 "데이터"와 "함수(절차)"로 구성하는 방식의 프로그래밍 패러다임  

#### **0-1. 절차 지향 프로그래밍 특징**
> **"데이터"** 와 해당 데이터를 처리하는 **"함수(절차)"** 가 **분리**되어 있으며, 함수 호출의 흐름이 중요

> 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행

- 실제로 진행되는 내용이 무엇이 무엇인가가 중요
- 데이터를 재사용하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

#### **소프트웨어 위기(Software Crisis)**
> 하드웨어 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격   
> -> 절차 중간에 문제가 생기면 프로그램 전체에 문제가 생기는 경우 발생   
> -> 이런 이유로 '객체 지향 프로그래밍'이 나온 것

---

&nbsp;

## **1. 객체 지향 프로그래밍 (OOP, Object Oriented Programming)**
> **데이터**와 해당 데이터를 조작하는 **메서드(함수)** 를 **하나의 객체**로 묶어 관리하는 방식의 프로그래밍 패러다임

> 객체 간 상호작용과 메시지 전달이 중요

---
### **절차 지향 vs 객체 지향**
|  **절차 지향**  |  **객체 지향**  |
|------|-----------|
|데이터와 해당 데이터를 처리하는 함수(절차)가 분리|데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음|
|함수 호출의 흐름이 중요|객체 간 상호작용과 메시지 전달이 중요|
---

#### 교재 10쪽 그림 예시
전사가 공격을 하는 경우 문장이 짜이는 구조
> 절차지향 : 공격을 한다 (전사가)  
> 객체지향 : 전사가 베기를 한다.

---

&nbsp;

## **2. 객체 (Object)**
> 클래스에서 정의한 것을 토대로 메모리에 할당된 것

> **'속성'** 과 **'행동'** 으로 구성된 모든 것

> 파이썬에 존재하는 모든 것은 객체다.

> 클래스 : 파이썬에서 타입을 표현하는 방법 (후술)  
> 클래스를 만든다 == 타입을 만든다  
> 클래스도 객체다.

---

#### **객체 예시**
> **가수(클래스)** 를 예시로 보자면

> **속성(정보=변수)** : '직업: 가수', '생년월일: 1999.05.16', '국적: 대한민국'

> **행동(동작=메서드)** : '랩()', '댄스()', '소몰이()'

> **객체** : 아이유, BTS ...  
-> 클래스로 만든 객체를 **인스턴스**라고 한다.  

1. 아이유는 객체다 (O)
2. 아이유는 인스턴스다 (X)
3. 아이유는 가수의 인스턴스다 (O)

---

### **클래스와 객체** 

> '', 'hello', '파이썬' : 문자열 타입(클래스)의 객체(인스턴스)

> [1, 2, 3], [1], [], ['hi'] : 리스트 타입(클래스)의 객체(인스턴스)

> **하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.**

##### **예시**
```python
name = 'Alice'
print(type(name)) # <class 'str'>
```
> 변수 name의 타입은 str 클래스다.  
-> 변수 name은 **str 클래스의 인스턴스**이다.  
-> 우리가 사용해왔던 **데이터 타입은 사실 모두 클래스**였다.
-> 즉, 문자열 타입의 변수는 str 클래스로 만든 인스턴스다.

---

### **객체 (object)의 특징**
> **객체 (object) = 속성(arttribute) + 기능(method)**

1. 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?

2. 속성(arttribute) : 어떤 상태(데이터)를 가지는가?

3. 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

---

&nbsp;

## **3. 클래스 (Class)**
> 파이썬에서 타입을 표현하는 방법

> 객체를 생성하기 위한 설계도  
데이터와 기능을 함께 묶는 방법을 제공

---

### **클래스 구조**
```python
# 클래스 정의
class Person:  
    pass
# 함수와 다른점
# 1. 대문자로 시작한다.
# 2. Peson 뒤에 ( )를 생략 가능하다.
# 클래스는 Paskal Case를 사용
# 함수는 snake case를 사용

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute
``` 
> 클래스는 병사(인스턴스)를 생산한다.  
> 병사들이 나가서 메서드와 속성(변수)을 활용해서 코드를 실행한다.
---

### **클래스 기본 활용**
**1. 생성자 함수**
> 객체를 생성할 때 자동으로 호출되는 특별한 메서드

> _ _inin _ _ 이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당

> 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정

---

**2. 인스턴스 변수**
> 인스턴스(객체)마다 **별도로 유지되는 변수**

> 인스턴스마다 **독립적인 값**을 가지며, 인스턴스가 생성될 때마다 초기화됨

---

**3. 클래스 변수**
> 클래스 내부에 선언된 변수

> 클래스로 생성된 모든 인스턴스들이 **공유**하는 변수

**4. 인스턴스 메서드**
> 각각의 인스턴스에서 호출할 수 있는 메서드

> 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행


```python
class Person:
    blood_color = 'red'        # blood_color = 'red'가 클래스 변수
    
    def __inin__(self, name):  # 이 함수 2줄이 생성자 함수
        self.name = name       # self.name = name이 인스턴스 변수


    def singing(self):         # 이 함수 2줄이 인스턴스 메서드
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('iu')

# 인스턴스 변수
print(self.name)  # iu

# 클래스 속성(변수) 접근
print(singer1.blood_color)

# 인스턴스 메서드 호출
print(singer1.singing())  # iu가 노래합니다.

```

---

#### 강의 때 실습한 생성자 함수 코드
```python
class Person:
    # 속성
    blood_color = 'red'

    def __init__(self, name):
        self.name = name
# self는 인스턴스 자기자신을 의미함
# init을 넣으면 무조건 써야 된다.
# 안써도 되는거다..?

    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('iu')  
singer2 = Person('bts')  

# 메서드를 호출 (클래스에서 메서드는 init, singing 2개)
# 그런데 __ __ 이렇게 언더바가 붙은건 인스턴스가 사용 불가능한 것
print(singer1.singing()) #iu가 노래합니다.
print(singer2.singing()) #bts가 노래합니다.

print(singer1.blood_color) # red
print(singer2.blood_color) # red
```

---


### **이름 공간 (namespace)**
> 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성

> 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성

> 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색  
(인스턴스가 가지고 있지 않으면 클래스로 찾으러 감)

```python
# Person 정의
class Person:
    name = 'Unknown'

    def talk(self):
        print(self.name)

p1 = Person()            
p1.talk()  # Unknown
# p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수(unknown)가 출력됨

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # Unknown
p2.name = 'Kim'
p2.talk()  # Kim
# p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)가 출력됨

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
# Person 클래스의 값인 Kim으로 변경된 것이 아닌
# p2 인스턴스의 이름공간에 name이 Kim으로 저장됨
```

---

#### 강의 중 이름공간 실습 코드
```python
class Person:
    name = 'Unknown'

    def talk(self):  # talk은 인스턴스 변수 네임을 말하게 하는 명령
        print(self.name)

p1 = Person()            
p1.talk()  # Unknown
# 인스턴스 본인에게 name이 없어서 클래스 변수 name = 'Unknown'을 가지고 온 것


p2 = Person()
p2.name = 'Kim'
p2.talk()  # Kim
# Kim이라는 인스턴스 변수 네임을 가지게 되어서 Kim을 출력


print(Person.name)  # Unknown
print(p1.name)  # Unknown
print(p2.name)  # Kim
# p2만 자기의 네임이 있어서 Kim이 나온다.

p2.ssafy = 11
# p2라는 인스턴스에 ssafy라는 인스턴스 변수를 11로 할당한 것
print(p2.ssafy)  # 11
```

---

### **독립적인 이름공간을 가지는 이점**
> 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능

> 객체 지향 프로그래밍의 중요한 특성 중 하나로,  
클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장

> 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌 및 영향을 주지 않으면서 독립적으로 동작할 수 있음

> 코드의 가독성, 유지보수성, 재사용성 향상에 도움을 줌

> 절차 지향은 순서가 있고, 서로 영향을 줌.  
그렇기 때문에 유지보수가 힘들어진다.  
그러나 객체 지향은 독립적으로 동작하기에 위와 같은 장점이 있는 것

---

### **인스턴스 변수와 클래스 변수**

#### **클래스 변수 활용**
> 가수가 몇명인지 확인하고 싶은 경우  
-> 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정

```python
class Person:
    count = 0

    def __init__(self, name):
        Person.count +=1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2
```
---

#### **클래스 변수와 인스턴스 변수**
> 클래스 변수를 변경할 때는 항상 **클래스.클래스변수** 형식으로 변경

> self 붙은 애들이 인스턴스 변수이다.

```python
class Circle():
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)  # 3.14
print(c1.pi)  # 3.14  
print(c2.pi)  # 3.14

Circle.pi = 5  # 클래스 변수 변경
print(Circle.pi)  # 5
print(c1.pi)  # 5
print(c2.pi)  # 5

c2.pi = 5  # 인스턴스 변수 변경 (c2 인스턴스 변수 pi를 할당한 것)
print(Circle.pi)  # 3.14 (클래스 변수)
print(c1.pi)  # 3.14 (클래스 변수)
print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
```
---

&nbsp;

## **4. 메서드 (Method)**
> 종류 : 인스턴스, 클래스, 정적(스태틱)  

> 데코레이터가 없으면 인스턴스 메서드,  
데코레이터가 있으면 그에 따라 클래스 혹은 정적 메서드

### **4-1. 인스턴스 메서드 (instance method)**
> 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드  

>**인스턴스**의 상태를 조작하거나 동작을 수행  
(가지고 있는건 클래스지만, 인스턴스를 조작한다)

---

#### **인스턴스 메서드 구조**
> 클래스 내부에 정의되는 메서드의 기본

> **반드시 첫 번째 매개변수로 인스턴스 자신(self)** 을 전달받음

```python
class MyClass:

    def instance_method(self, arg1, ...):
        pass
```
---

#### **self 동작 원리**
```python
# upper 메서드를 사용해 문자열 'hello'를 대문자로 변경하기
'hello'.upper()

# 하지만 실제 파이썬 내부 동작은 이렇게 이루어진다.
str.uper('hello')
```
> str 클래스가 upper 메서드를 호출했고,  
그 첫번째 인자로 문자열 인스턴스가 들어간 것

> **인스턴스 메서드의 첫 번째 매개변수가 반드시 인스턴스 자기 자신인 이유**

> 'hello'.upper()은 str.upper('hello')를  
**객체 지향 방식의 메서드로 호출하는 표현**이다. (단축형 호출)

> 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 **객체 스스로 메서드를 호출**하여 코드를 동작하는 객체 지향적 표현이다.
---

&nbsp;

### **4-2. 생성자 메서드 (constructor method)**
> 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

> 인스턴스 변수들의 초기값을 설정

> _ _ init _ _으로 만든다.

#### **생성자 메서드 구조**
```python
class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
    
personal = Person()  # 인스턴스가 생성되었습니다.
```

```python
class Person:

    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')

person1 = Person('지민')  
# 인스턴스가 생성되었습니다. 지민
```
---

&nbsp;

### **4-3. 클래스 메서드 (class method)**
> 클래스가 호출하는 메서드

> 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

---

#### **클래스 메서드 구조**
> @classmethod 데코레이터를 사용하여 정의  
-> 데코레이터가 없으면 인스턴스 메서드가 된다.  
-> 인스턴스 메서드랑 구분하기 위해서 필요함

> 호출 시, 첫 번째 인자로 호출하는 클래스(cls)가 전달됨  
-> 클래스와 연결하기 위해서 필요함

```python
class MyClass:

    @classmethod  # 데코레이터
    def class_method(cls, arg1, ...):
        pass      
```

---

#### **클래스 메서드 예시**
```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
# {cls.count}가 아니라 {Person.count} 사용 가능
# 단, 클래스 상속(DAY9 강의 배움) 때 자식 클래스가 부모 클래스를 가져와서 쓰게 되기 때문에 안된다. 
# 지금은 클래스가 하나라서 되는 것.

person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 인구수는 2입니다.
```
---

&nbsp;

### **4-4. 스태틱 (정적) 메서드 (static method)**
> 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

> 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

---

#### **스태틱 메서드 구조**
> @staticmethod 데코레이터를 사용하여 정의

> 호출 시 필수적으로 작성해야 할 매개변수가 없음  
(필수 매개변수 없음)  
(호출은 클래스가 한다.)

> 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용  
(일반 함수 기능이 필요한 경우에 사용하는 것)

```python
class MyClass:
    @staticmethod
    def static_method(arg1, ...):
        pass
```
---

#### **스태틱 메서드 예시**
```python
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
# 얘네들의 역할은 '문자열 조작'이기에
# 인스턴스, 클래스 변수를 컨트롤하지 않는다.
# 스태틱 메서드는 클래스가 호출한다.

text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # dlrow, olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)  # Hello, world
```
---

### **메서드 정리**

1. 인스턴스 메서드
> 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행  
(self 필수 매개변수)

2. 클래스 메서드
> 인스턴스 상태에 의존하지 않는 기능을 정의  
(데코레이터 있음, cls 필수 매개변수)

> 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

3. 스태틱 메서드
> 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행 (데코레이터 있음, 일반함수기능으로 보기)

---

#### **각자의 역할**
1. 클래스가 사용해야 할 것**
> 클래스 메서드, 스태틱 메서드

2. 인스턴스가 사용해야 할 것
> 인스턴스 메서드
---

#### **클래스가 할 수 있는 것**
> 클래스는 모든 메서드를 호출 할 수 있음

> 하지만 **클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다.**

#### **인스턴스가 할 수 있는 것**
> 인스턴스는 모든 메서드를 호출 할 수 있음

> 하지만 **인스턴스는 인스턴스 메서드만 사용하도록 한다.**

---
### **할 수 있다 != 써도 된다**
> 각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 따라 설계된 것이다.

> 클래스와 인스턴스 각각 올바른 메서드만 사용해야 한다.

> 클래스 : 클래스, 스태틱  
인스턴스 : 인스턴스  
이렇게만 사용하자!!!!!!

## **5. 참고**

### **5-1. 매직 메서드**
> 인스턴스 메서드

> 특정 상황에 자동으로 호출되는 메서드

> Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드

> 스페셜 메서드 혹은 매직 메서드라고 불림

```python
class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'[원] radius: {self.r}'
    # 인스턴스를 print할 때 자동으로 출력된다.

    def area(self):
        return 3.14 * self.r * self.r

c1 = Circle(10)
c2 = Circle(1)

print(c1)  # [원] radius: 10
print(c2)  # [원] radius: 1
```
> def __init__(self, r):  

> def __str__(self):

> 위 2개가 가장 잘 쓰일 것이다.

---

### **5-2. 데코레이터 (Decorator)**
> 다른 함수의 코드를 유지한 채로 수정 & 확장하기 위해 사용되는 **함수**

##### **데코레이터 적용 예시**
```python
@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()

'''
함수 실행 전
원본 함수 실행
함수 실행 후
'''
```
---

### **절차지향과 객체지향은 대조되는 개념이 아니다**
> 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입

> 그를 통해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

---
# 오프라인  

다음주부터 6주간 알고리즘 수업한다.  
반복문 등은 자주 써서 숙달될거다.  
대신 클래스는 99% 안써서 다 까먹을거다.  
근데 그 다음 장고, DB 할 때는 클래스가 쏟아진다.

---
#### **클래스를 쓰는 이유?**
> 계산기 함수 만드는 코드 실습했음

```python
# 계산기 함수 만들기
# 결과값
# print(add_cal(3))  # 3
# print(add_cal(4))  # 7

result = 0

def add_cal(num):
    global result                 
    result = result + num
    return result

result = add_cal(3)
print(result)  # 3
print(add_cal(4))  # 4

# 이걸 7이 나오게 하려면 result = 0을 밖으로 빼고 함수안에 result를 global로 만들어야한다.
# 함수밖을 벗어나더라도 유지되도록 만드는 것

# add_cal2를 만들려면 글로벌 변수도 2개가 되어야하고 계산기 수가 늘수록 코드 비효율성 올라감

# 이것이 클래스가 필요한 이유
```

---

#### **init을 왜 쓰는 이유?**
> 실습하면서 설명해주신 코드

```python
class add_cal:
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2

cal_1 = add_cal()

print(cal_1.add(0, 3)) # 두 번째 방법으로 쓴 것

# 첫 번째 방법 : 클래스 이름, 메서드 이름, 인스턴스 이름, self, 인자 값 2개
# add_cal.add(cal_1, 0, 3)

# 좀 더 쉽게 관행적으로 많이 쓰는 방법 : 인스턴스 이름, 메서드 이름, 인자 값 2개
# cal_1.add(0, 3)

# 여기까지 쓴 코드가 init 없이 만든 것

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 만드는 것과 동시에 인스턴스에 어떤 값을 전달하고 싶을 때 쓰는 것이 init 함수
# 선언됨과 동시에 실행되도록 하는 것
# init 함수 써서 만드는 법

class add_cal:

    def __init__(self, start):
        self.start = start
        print("init functioned runned")
        # init 할 때 추가기능을 넣은 예시

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2

cal_1 = add_cal(0)
print(cal_1.start)
# 출력물
# init functioned runned
# 0

# 셀프 스타트랑 스타트는 완전히 다르다.
# 오른쪽에 먼저 값이 생기고 그 값을 셀프 스타트라는 변수이름으로 (매칭, 바인딩, 할당) 시킨것이다.
```
---

#### **init 연습**

```python
class Account:
    total_account = 0

    def __init__(self, name):
        self.name = name
        Account.total_account = Account.total_account + 1

    def show_count(self):
        print(f'가입한 고객의 이름은 {self.name}이고, 총 계좌수는 {Account.total_account}입니다.')

p1 = Account("sky")
p1.show_count()

p2 = Account("kkr")
p2.show_count()

p3 = Account("shj")
p3.show_count()

'''
출력값은

가입한 고객의 이름은 sky이고, 총 계좌수는 1입니다.
가입한 고객의 이름은 kkr이고, 총 계좌수는 2입니다.
가입한 고객의 이름은 shj이고, 총 계좌수는 3입니다.
'''
```
---

#### **메서드**
인스턴스 메서드를 제일 많이 쓴다.

클래스, 정적 메서드는 @데코레이터를 꼭 쓴다.

스태틱(정적) 메서드는 별로 안중요
(나중에 장고에 나옴)

공부 우선 순위 :  
인스턴스 메서드 -> 클래스 메서드 -> 스태틱 메서드

---

