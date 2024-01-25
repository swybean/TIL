# **파이썬 OOP-1_8일차**

## **목차**
1. 상속
2. 에러와 예외
3. EAFP & LBYL
---





## **1. 상속 (Inheritance)**
> 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

### **1-1. 상속이 필요한 이유**

#### **1. 코드 재사용**
> 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음

> 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

#### **2. 계층 구조**
> 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음

> 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

#### **3. 유지 보수의 용이성**
> 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지보수가 용이해짐

> 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

---

### **1-2. 클래스 상속**

#### **1. 상속 없이 구현하는 경우**
> 학생 / 교수 정보를 나타내기 어려움  

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.
```
> 메서드 중복 정의
```python
    class Professor:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')

    class Student:
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

        def talk(self): # 중복
            print(f'반갑습니다. {self.name}입니다.')
```
---

#### **2. 상속을 사용한 계층구조 변경**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    # ( )안에 상위 클래스 이름을 넣기
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    # ( )안에 상위 클래스 이름을 넣기
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

print(p1.department)  # 컴퓨터공학과
print(s1.gpa)  # 3.5

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.
```
---

#### **super( )**
> 부모 클래스 객체를 반환하는 내장 함수

##### **super( ) 사용 예시**

###### **사용 전**
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

```

###### **사용 후**
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        # 부모클래스의 init 메서드 호출
        self.student_id = student_id

```
---

### **1-3. 다중 상속**
> 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것

> 상속받은 모든 클래스의 요소를 활용 가능함

> 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**됨

#### **다중 상속 예시**
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('김싸피')  
# 생성자 함수를 찾아 Dad, Mom을 갔는데 없으니 Person까지 올라간다.
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
# Dad한테만 있는 것이기 때문에 Dad에 가서 가져온다.
print(baby1.gene)  # xy
'''Dad, Mom 둘 다 있음
FirstChild(Dad, Mom) Dad가 먼저 있으니까 상속 순서가 Dad가 빠르다.
따라서 Dad에 있는 gene 값을 가지고 온다.'''
```
> 밑에 나오는 다이아몬드 문제의 예시이다.

---

### **1-4. 다이아몬드 문제 (The diamond problem)**
> 두 클래스 B와 C가 A에게 상속되고, 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함

> B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의하지 않은 경우라면  

> D는 B의 메서드 중 어떤 버전을 상속하는가?  
> 아니면 C의 메서드 버전을 상속하는가?

---

#### **파이썬에서의 해결책**
> MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성

> 부모 클래스로부터 상속된 속성들의 검색을 **깊이 우선**으로, **왼쪽에서 오른쪽**으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음

> 그래서, 속성 D에서 발견되지 않으면, B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾고, 이런 식으로 진행됨

```python
class D(B, C):
    pass
```
---

### **1-5. MRO (Method Resolution Order)**
> 메서드 결정 순서

#### **mro( ) 메서드**
> 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

> 기존 과정 : 인스턴스 -> 클래스 순으로 이름공간 탐색

> 상속관계 과정 : 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

---

#### **MRO가 필요한 이유**
> 부모 클래스들이 여러 번 액세스 되지 않도록,  
각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 **순서를 보존**하고,  
각 부모를 오직 한 번만 호출하고,  
부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 **단조적인 구조 형성**

> 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움

> 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며,  
코드의 재사용성과 유지보수성이 향상

---

#### **super( )**
> 부모 클래스 객체를 반환하는 내장 함수

> 다중 상속 시 MRO를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출

---

##### **super( ) 사용 예시 1번**
```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA의 생성자 함수를 가져온다.
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA의 show_value 함수를 가져온다.
        print(f'Value from Child: {self.value_c}')



child = Child()  # Value from ParentA: ParentA
child.show_value()  # Value from Child: Child
print(child.value_a)  # ParentA
print(child.value_c)  # Child
print(child.value_b)  # Error
'''ParentB의 생성자 함수를 통해 만들어져야지만 value_b가 나오는데
ParentA의 생성자 함수를 썼기 때문에 Error가 나온다.'''
```

##### **super( ) 사용 예시 2번**
```python
class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')

class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')
        
class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')

obj = D()
'''
출력값
A Constructor
B Constructor
C Constructor
D Constructor

D B C A 순으로 검색하며 올라가지만
마지막으로 검색한 것부터 반환되며 출력되기에
출력값은 A C B D 순으로 나온다.
'''

print(D.mro())  # mro 순서 출력하는 방법
'''
[<class '__main__.D',
<class '__main__.B',
<class '__main__.C',
<class '__main__.A',
<class 'object'>]
'''
```
---

#### **super( ) 2가지 사용 사례**

##### **1. 단일 상속 구조**
> 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음

> 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super( )를 사용하면 코드 수정이 더 적게 필요

##### **2. 다중 상속 구조**
> **MRO를 따른 메서드 호출**

> 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

---




&nbsp;








## **2. 에러와 예외**

### **2-1. 버그 (bug)**
> 소프트웨어에서 발생하는 **오류** 또는 **결함**

> 프로그램의 예상된 동작과 실제 동작 사이의 불일치



#### **버그의 기원**
> 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견

> Mark II라는 컴퓨터 회로에 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것

> "버그"라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작

---

### **2-2. 디버깅 (Debugging)**
> 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

> 프로그램의 **오작동 원인을 식별하여 수정**하는 작업

#### **디버깅 방법**

#### **1. print 함수 활용**
: 특정 함수 결과, 반복/조건 결과 등 나눠서 생각  
(코드를 bisection으로 나눠서 생각)

#### **2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용**
: breakpoint, 변수 조회 등

#### **3. Python tutor 활용**
: 단순 파이썬 코드인 경우

#### **4. 뇌 컴파일, 눈 디버깅 등**

---

### **2-3. 에러 (Error)**
> 프로그램 실행 중에 발생하는 예외 상황

---

#### **파이썬의 에러 유형**
> 에러 = 문법 에러 + 예외

#### **1. 문법 에러 (Syntax Error)**
> 프로그램의 구문이 올바르지 않은 경우 발생  
(오타, 괄호 및 콜론 누락 등의 문법적 오류)

#### **2. 예외 (Exception)**
> 프로그램 실행 중에 감지되는 에러

---

#### **문법 에러 예시**

##### 문법 오류 (Invalid syntax)
```python
while # SyntacError: invalid syntax
```

##### 잘못된 할당 (assign to literal)
```python
5=3 # SyntaxError: cannot assign to literal
```

##### EOL (End of Line)
```python
print('hello
# SyntaxError: EOL while scanning string literal
```

##### EOF (End of File)
```python
print(
# SyntaxError: unexpexted EOF while parsing
```
---

### **2-4. 예외 (Exception)**
> 프로그램 실행 중에 감지되는 에러

#### **내장 예외 (Built-in Exception)**
> 예외 상황을 나타내는 예외 **클래스**들

> 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용

---

#### **내장 예외 종류**

**ZeroDivisionError** : 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
```python
10/0 # ZeroDivisionError: division by zero
```

**NameError** : 지역 또는 전역 이름을 찾을 수 없을 때 발생
```python
print(name_error)
# NameError: name 'name_error' is not defined
```

 **TypeError**
```python
# 타입 불일치
'2' + 2  
# TypeError: can only concatenate str (not "int") to str

# 인자 누락
sum()
# TypeError: sum() takes at least 1 positional argument (0 given)

# 인자 초과
sum(1, 2, 3)
# TypeError: sum() takes at most 2 arguments (3 given)

# 인자 타입 불일치
import random
random.sample(1,2)
# TypeError: Population must be a sequence.
# For dicts or sets, use sorted(d).
```

**ValueError** : 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우 발생
```python
int('1.5') 
# ValueError: invalid literal for int() with base 10: '3.5'

range(3).index(6)
# ValueError: 6 is not in range
```

**IndexError** : 시퀀스 인덱스가 범위를 벗어날 때 발생
```python
empty_list = []
empty_list[2]
# IndexError: list index out of range
```

**KeyError** : 딕셔너리에 해당 키가 존재하지 않는 경우
```python
person = {'name': 'Alice'}
person['age']  # KeyError: 'age'
```

**ModuleNotFoundError** : 모듈을 찾을 수 없을 때 발생
```python
import hahaha
# ModuleNotFoundError: No module named 'hahaha'
```

**ImportError** : 임포트 하려는 이름을 찾을 수 없을 때 발생
```python
from random import hahaha
# ImportError: cannot import name 'hahaha' from 'random'
```

**Keyboardinterrupt** : 사용자가 Control-C 또는 Delete를 누를 때 발생 (무한루프 시 강제 종료하는 방법)
```python
while True:
    continue
'''
Traceback (most recent call last):
    File "...", line 2, in <module>
        continue
KeyboardInterrupt
'''
```

**IndentationError** : 잘못된 들여쓰기와 관련된 문법 오류
```python
for i in range(10):
print(i)
# IndentationError: expected an indented block
```

---










### **2-5. 예외 처리**
> **try와 except**   
파이썬에서는 **try** 문과 **except** 절을 사용하여 예외 처리

---

#### **try-except 구조**
> try 블록 안에는 예외가 발생할 수 있는 코드를 작성

> except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성

> 예외가 발생하면 프로그램 흐름은 try 블록을 즉시 중단하고 빠져나와 해당 예외에 대응하는 except 블록으로 이동

```python
try:
    # 예외가 발생할 수 있는 코드

except 예외종류:
    # 예외 처리 코드
```
---

#### **예외 처리 예시**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# 0으로 나눌 수 없습니다.
```

```python
try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
'''
숫자입력 : a
숫자가 아닙니다.
''' 
```
---

#### **복수 예외 처리 연습 문제**
> 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오.    
(발생 가능한 에러가 무엇인지 예상해보기)
```python
num = int(input('100으로 나눌 값을 입력하시오 : '))
print(100 / num)
```
> int('a') : 문자열을 int로 형변환 (ValueError)

> 100 / 0 : 0으로 숫자를 나눔 (ZeroDivisionError)

---

#### **복수 예외 처리 연습 문제 풀이**
> 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오.  
(발생가능한 에러를 모두 명시하거나 & 별도로 작성하기)

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오 :' 
    ))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')
```

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오 :' 
    ))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
```

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
except ValueError:
    print('숫자 넣어')
except ZeroDivisionError:
    print('0으로 나누기가 될 것 같아?')
except:
    print('알수없는 에러가 발생했습니다.')
```


---

#### **내장 예외의 상속 계층구조 주의**
> 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오. : '))
except BaseException:
    print('숫자를 넣어주세요.')

# 이 아래 두 블록에 도달하지 못함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
```
> 내장 예외 클래스는 상속 계층구조를 가지기 때문에    
except 절로 분기 시 **반드시 하위 클래스를 먼저 확인 할 수 있도록 작성**해야 함

---

### **2-6. as 키워드**
> as 키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음
```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')
# list index out of range가 발생했습니다.

# error는 변수명이라 바꿔도 됨.
```

---




&nbsp;





## **3. EAFP & LBYL** (참고)
> 예외처리와 값 검사에 대한 2가지 접근 방식

### **EAFP**
> Easier to Ask for Forgiveness than Permission  
(용서가 허락보다 쉽다 -> 일단 실행하고 예외 생기면 나중에 처리하자)

> **예외처리를 중심**으로 코드를 작성하는 접근 방식 **(try-except)**



### **LBYL**
> Look Before You Leap  
(도약하기 전에 확인하라 -> 우리가 평소에 사용하는 작성 방식)

> **값 검사를 중심**으로 코드를 작성하는 접근 방식 **(if-else)**

---

#### 접근 방식 비교
```python
# EAFP
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# LBYL
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```

#### 강의 시간에 실습한 비교
```python
# 딕셔너리에서 키를 조회할 때
# 키가 없다는 상황
my_dict = {}

# try-except (EAFP)
try:
    result = my_dict['a']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# if-else (LBYL)
if 'a' in my_dict:
    result = my_dict['a']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```
---

&nbsp;

|  EAFP  | LBYL  |
|------|-----------|
|일단 실행하고 예외를 처리|실행하기 전에 조건을 검사|
|코드를 실행하고 예외가 발생하면 예외처리를 수행|코드 싫애 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식|
|코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리|코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음|
|예외 상황을 예측하기 어려운 경우에 유용|예외 상황을 미리 방지하고 싶을 때 유용|

---
&nbsp;

---
### Python 수업 종료  
: 공식문서 9.5.1까지 진도 나간 것  
공식문서 코드들 퀄리티 높다. (한 번씩 따라써보기 추천)

---
### 월말고사 정보
2시간  
10문제+  
레벨1~5  
샘플문제 오늘 나감  

---

### ASCII 설명  
space(공백)도 문자다.  



















