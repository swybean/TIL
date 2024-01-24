# 1월 17일 파이썬 함수와 제어문1_3일차

## **지난 수업 복습**
1. 없음
---
## **오늘의 목차**  
1. 함수
2. 매개변수와 인자   
3. 함수와 Scope
4. 재귀 함수
5. 유용한 함수
6. Packing & Unpacking
---    

## **1. 함수 (Functions)**    
> **특정 작업**을 수행하기 위한 **재사용** 가능한 코드 묶음  


**함수를 사용하는 이유**  
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지  
- **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상  

예시
```python
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수 사용하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)
```
num1, num2가 아니라 다른 값을 넣어도 두 개의 합이 나온다. -> 재사용성이 높아지는 이유.  


---

### **1-1. 내장 함수 (Built-in function)**  
> - 파이썬이 기본적으로 제공하는 함수  
> (별도의 import 없이 바로 사용 가능)  
> - 가장 대표적인 내장 함수 : print()  

---

예시 : 절대값을 만드는 함수 abs  
```python
# abs 함수 호출의 반환 값을 result에 할당  
result = abs(-1)
print(result) # 1
```
---

### **1-2. 함수 호출 (function call)**
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것  
- 명령어 : function_name(arguments)
- 명령어 예시 : print(1)  
    -> function_name = print, (arguments) = (1)


### **1-3. 함수 구조**
```python
def make_sum(pram1, pram2)
    """이것은 두 수를 받아 
    두 수의 합을 반환하는 함수입니다.

    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2
```
return value : 반환값

""" 내용 """ : 여러줄 주석  
- 여러줄 주석은 함수에서 Docstring 이라는 역할을 한다.  
- 이 함수를 사용하는 가이드 역할  
- 기본적으로 주석, 하지 않아도 함수 사용에는 문제 없음  

---

### **1-4. 함수의 정의와 호출**

```python
# 함수 정의
def greet(name):
    """입력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello, ' + name
    return message

# 함수 호출
result = greet('Alice')
print(result) # Hello, Alice
```

---

- 함수 정의  
    함수 정의는 def 키워드로 시작 (define)  
    def 키워드 이후 함수 이름 작성  
    괄호 안에 매개변수를 정의할 수 있음  
    매개변수(parameter)는 함수에 전달되는 값을 나타냄  

- 함수 body  
    콜론(:) 다음에 들여쓰기 된 코드 블록  
    함수가 실행 될 때 수행되는 코드를 정의  
    Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서  

- 함수 반환 값  
    함수는 필요한 경우 결과를 반환할 수 있음  
    return 키워드 이후에 반환할 값을 명시  
    return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환  
    (필수는 아니다. 함수에 따라 사용하지 않아도 됨)  

- 함수 호출  
    함수를 호출하기 위해서는 함수의 이름과 필요한 인자(argument)를 전달해야 함  
    호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨  


매개 변수 : 정의할 때 매개변수라고 함 예시에서 'name'  
인자 : 호출할 때 인자라고 함, 예시에서 'Alice'  
-> 다음 파트에서 후술  



## **2. 매개변수와 인자**    
> - 매개변수 (parameter)  
> 함수를 **정의할 때**, 함수가 받을 값을 나타내는 변수    
> - 인자 (argument)  
> 함수를 **호출할 때**, 실제로 전달되는 것

---

예시 : 매개변수와 인자의 차이
```python
def add_numbers(x, y): # x와 y는 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자
print(sum_result)
```
위 예시 def add_numbers(x, y)에서 매개변수는 x와 y 2개이다.  
위 예시 sum_result = add_numbers(a, b)에서 인자는 a와 b 2개이다.  


### **2-1. 인자의 종류**

#### **1. 위치인자 (Positional Arguments)**
> - 함수 호출 시 인자의 위치에 따라 전달되는 인자
> - **위치인자는 함수 호출 시 반드시 값을 전달해야 함**  

예시
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
```
--- 

#### **2. 기본 인자 값 (Default Argument Values)**  
> - 함수 정의에서 매개변수에 기본 값을 할당하는 것  
> - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨  

예시
```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 안녕하세요, Bob님! 25살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
```
age = 30이 기본인자 값이다.
인자를 전달하면 기본인자 대신 전달한 인자가 출력된다.

---

#### **3. 키워드 인자 (Keyword Arguments)** 
>  - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자  
> - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음  
> - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달  
> - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**

예시
```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age = 35) 
# 안녕하세요, ave님! 35살이시군요.

greet(age = 35,'Dave') 
# positional argument follows keyword argument  
```
---

#### **4. 임의의 인자 목록 (Arbitrary Argument Lists)**
> - 정해지지 않은 개수의 인자를 처리하는 인자  
> - 함수 정의 시 매개변수 앞에 **'*'** 를 붙여 사용하며, 여러 개의 인자를 **tuple**로 처리  

예시
```python
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

"""
(1, 2, 3)
합계: 6
"""
calculate_sum(1, 2, 3)
```
---

#### **5. 임의의 키워드 인자 목록 (Arbitrary Keyword Argument Lists)**
> - 정해지지 않은 개수의 키워드 인자를 처리하는 인자  
> - 함수 정의 시 매개변수 앞ㅍ에 **' ** '** 를 붙여 사용하며, 여러 개의 인자를 **dictionary**로 묶어 처리  

예시
```python
def print_info(**kwargw):
    print(kwargw)

print_info(name='Eve', age=30)
# {'name': 'Eve', 'age': 30}
```
---

#### **함수 인자 권장 작성순서**
- 위치 -> 기본 -> 가변 -> 가변 키워드  
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함  
- **단, 모든 상황에 적용되는 절대적 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음**

예시
```python
def func(pos1, pos2, default_arg='default', *args, **kwargw):
    ...
```
---

실습 예시
```python
def func(pos1, pos2, age=30, *args, **kwargw):
    print(pos1, pos2, age, args, kwargw)

func(1, 2, 3, 4, 5) # 1 2 3 (4, 5) {}
```
@@강의 다시보기 예시 2도 있음@@@@@@@@@@@@

---

## **3. 함수와 Scope**   

### **3-1. Python의 범위(Scope)**  
> 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분  
> scope  
    global scope: 코드 어디에서든 참조할 수 있는 공간   
    local scope: 함수가 만든 scope (함수 내부에서만 참조 가능)  
> variable
    global variable : global scope에 정의된 변수
    local variable : local scope에 정의된 변수  

Scope 예시
```python
def func():
    num = 20
    print('local', num) # local 20

func()

print('global', num) # NameError: name 'num' is not defined
```
- num은 local scope에 존재하기 때문에 global에서 사용할 수 없음  
- 이는 변수의 **수명주기**와 연관이 있음  

---

### **3-2. 변수 수명주기(lifecycle)**
> 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨

1. 빌트인 스코프  
    파이썬이 실행된 이후부터 영원히 유지
2. 글로벌 스코프  
    모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지  
3. 로컬 스코프  
    함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지  

### **3-3. 이름 검색 규칙()**
> 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음  
> 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름  
1. 로컬 스코프 : 지역 범위 (현재 작업 중인 범위)
2. 에클로즈드 스코프 : 지역 범위 한 단계 위 범위
3. 글로벌 스코프 : 최상단에 위치한 범위
4. 빌트인 스코프 : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)
> **함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음**
---


LEGB Rule 예시
```python
print(sum) # <built-in function sum>
print(sum(range(3))) # 3

sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable
```
- sum이라는 이름의 global scope에서 사용하게 되면서 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨  
- sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문  
**※ sum 변수 객체 삭제를 위해 del sum을 입력 후 진행**

---

LEGB Rule 예시 2번
```python
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) # 10 2 500
    
    locla(500)
    print(a, b, c) # 10 2 3

enclosed()
print(a, b) # 1 2

```
---

### 3-4. 'global' 키워드
> - 변수의 스코프를 전역 범위로 지정하기 위해 사용
> - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용  

예시
```python
num = 0 # 전역 변수

def increment():
    global num # num를 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1
```
---

**주의사항**

1. global 키워드 선언 전에 접근 시  

예시
```python
num = 0

def increment():
    # SyntaxError: name 'num' is used prior to global declaration
    print(num)
    global num
    num += 1
```

2. 매개변수에 global 사용 불가  

예시
```python
num = 0

def increment(num):
    # "num" is assigned before global declaration
    global num
    num += 1
```

- global 키워드는 가급적 사용하지 않는 것을 권장  
- 함수로 값을 바꾸고자 한다면 항상 **인자**로 넘기고 함수의 **반환 값**을 사용하는 것을 권장

---

## **4. 재귀 함수**    

### **재귀함수**
> 함수 내부에서 자기 자신을 호출하는 함수

### **4-1. 재귀 함수 특징**  
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐  
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성  

---

#### 재귀 함수 예시 : 팩토리얼
> factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산   
> 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함  
> 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출  

```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120
```

---

#### 재귀 함수 예시 : 팩토리얼
> n!  
> n * (n - 1)!  
> n * (n - 1) * (n - 2)!  
> ...  

---

> 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2* 1  
=> 같은 문제를 다른 input을 통해서 해결  

---


@@@@@교재 47,48쪽 보고 전부 다시 쓰기@@@@@@@@@@@@

---
#### **※ 재귀함수 중요 포인트**
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록  




## **5. 유용한 함수**    

### **5-1. 유용한 내장 함수**
> **map과 zip 함수 알아보기**

#### **map** 
> - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환  
> - 명령어 : map(function, iterable)  
> => map(함수 이름, 반복 가능한 친구(시퀀스))

**주의사항**
- map 함수로 만든 것은 mpa 덩어리라 바로 사용 불가
- 변환 필요하다.  
- 아래 예시에서 list로 변환한 것처럼  

**map 예시**
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at 0x00000239c9150760>
print(list(result)) # ['1', '2', '3']
```
**map 실습** (직접 해보기)
```python
numbers = input().split()

# 실습1
print(numbers) # ['1', '2', '3', '4', '5']

# 실습2
return = map(int, numbers) 

print(result) 
# ['1', '2', '3', '4', '5']
# <map object at 0x00000239c9150760>

# 실습3
return = map(int, numbers) 

print(result) 

print(list(result))
# [1, 2, 3, 4, 5]

# print(list(result))를 풀어서 써보면
# result = list(map(int, input().split()))
```
---

#### **zip** 
> - 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환  
> - 명령어 : zip(*iterables)  



**zip 예시**
```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x000001c76de58700>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]
```

---


### **5-2. lambda 함수**
> 이름 없이 정의되고 사용되는 익명 함수  

#### **lambda 함수 구조**
> - 명령어는 < lambda 매개변수: 표현식 >
> - lambda 키워드  
    람다 함수를 선언하기 위해 사용되는 키워드
> - 매개변수  
    함수에 전달되는 매개변수들  
    여러 개의 매개변수가 있을 경우 쉼표로 구분  
> - 표현식  
    함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성  

#### **lambda 함수 예시**
> 간단한 연산이나 함수를 **한 줄**로 표현할 때 사용
> 함수를 매개변수로 전달하는 경우에도 유용하게 활용

```python
# 예시1
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result) # 8

# 예시2
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) # 8
```

---

**lambda 함수 강의 실습**
```python
numbers = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

# 제곱을 만들어 주는 함수
result = list(map(func, numbers))
print(result) # [1, 4, 9, 16, 25]

# 위 함수를 람다 함수로 해보기
result2 = list(map(lambda x: x**2, numbers))
pirnt(result2) # [1, 4, 9, 16, 25]
```

---


## **6. Packing & Unpacking**    

### **6-1. Packing**
> - 여러 개의 값을 하나의 변수에 묶어서 담는 것  
> - 가변 인자할 때 하나의 Tuple로 묶인 것이 패킹의 예시이다.

**패킹 예시**
> 변수에 담긴 값들은 튜플 형태로 묶임
```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

---

**'*'을 활용한 패킹(1/2)**
> *b는 남은 요소들을 리스트로 패킹하여 할당
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
```

---

**'*'을 활용한 패킹(2/2)**
> Q: pirnt 함수에서 임의의 가변 인자를 작성할 수 있었던 이유

> A: 인자 개수에 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리

```python
def my_func(*objects):
    print(objects) # (1, 2, 3, 4, 5)
    print(type(object)) # <class 'tuple>

my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

---

**Packing 강의 실습**
```python
# 실습1
print(1, 2, 3)
print(4, 5, 6)

# 실습2
print(1, 2, 3, end=" ")
print(4, 5, 6)

#직접 해보고 결과 비교해보기
```

---

### **6-2. Unpacking**
> 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

**언패킹 예시**
> 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당  

예시
```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e) # 1 2 3 4 5
```

---

**'*'을 활용한 언패킹**
> *는 리스트의 요소를 언패킹
```python
names = ['alice', 'jane', 'peter']
print(*names) # alice jane peter
```

---

#### '**' 을 활용한 언패킹
> **는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹  
```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict) # 1 2 3
```

---

#### (*, **) 패킹 / 언패킹 연산자 정리
- '*'  
    패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜프로 묶는 역할  
    언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달

- '**'  
    언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할


---
---


# !오프라인 수업 내용!  

## 기본 지식 설명

**2학기 프로젝트**  
기획, 기획의도가 중요하다.  
친절한 유아이, 서비스 등  
테크닉은 기본  

---


**마크다운 사용방법 추가 설명**  
이미지 사용방법  
- 기존 사용하던 방법 : ![이미지](주소)  

---

> 로컬에 있는 이미지를 넣는 방법들
- 방법1
1. 정리본.md와 같은 폴더 내에 img1.png 로 넣기  
2. 정리본 내에서 이미지 삽입할 때
3. ![이미지이름](img1.png) 같이 파일이름을 쳐서 넣기  
4. ![이미지이름](.)을 치면 이미지 목록이 다 나온다.   
    그 중에서 골라서 넣기  

---

- 방법2
- 이미지가 자식폴더에 있는 경우
1. 정리본.md가 있는 파일 내에 이미지 보관용 파일 images 파일을 만들기
2. 해당 파일에 img1, img2 ... 등 전부 넣어두기
3. 정리본 내 이미지 삽입할 때
4. ![이미지이름](./)를 치면 폴더 목록이 나온다.  
5. 거기서 images 폴더 골라서 해당 폴더 내 이미지 중 선택  

- 번외: 이미지가 형제폴더에 있는 경우
1. ![이미지이름](./../) 치고 형제폴더 선택
1-1. (./../) 가 상위 폴더로 옮겨가는 것
2. 그 다음부터는 위동  

-> 점심 먹고 다시 실습 하면서 알려주신다고 함.

---

**깃 랩 온실 추가 설명**  
실습 & 과제 풀 때 사용  

> hw_2 hw_3 hw_4 ... 등 폴더들을 한 폴더로 넣고 싶은 경우 혹은 나의 깃허브에 넣고 싶은 경우
- 가정
1. 깃허브에 나의 원격 레포 만들기
2. 실습 10개를 pythonDay01 폴더에 넣고
3. 데탑에 있는 .git 폴더에 넣기
4. 데탑에 있는 .git 폴더를 나의 레포랑 연결시키기

- 방법
1. 실습을 다 풀고 깃랩에 제출까지 하기
2. 실습에 있는 .git 폴더들을 다 지운다.
3. 깃 관리 안받는 순수폴더로 만들고
4. 데탑 레포로 옮기고 내 깃허브로 옮기기

---

## 함수

- 변수는 데이터를 재사용하기 위해 만든 것  

- 함수는 코드를 재사용하기 위해 만든 것  
-> 코드를 어딘가 저장해두고 다시 재사용하는 것  
-> def는 '다시 쓰는 코드야'라는 뜻 (이건 뒤에 나올 코드를 재사용할거야 라는 뜻)  

---

> 나중에 다시 자세히 배움
> - 모듈 : 다른 함수에서 쓰인 코드를 또다른 함수에서 다시 쓰고 싶기에 만들어진 것  
> - 임포트 : 내가 만든 코드를 내가 아닌 타인도 사용하게 만든 것  

---

#### 함수호출  
핵심 : 해당 함수의 코드를 실행하는거다.  

코드를 수행할 때 코드에 사용되는 값들을 함수를 고르면서 같이 전달해주는 것 = 매개변수 & 인자  

---

#### 매개변수 & 인자
- 매개변수, 인자는 아직 통일되지 않은 용어  
-> 별로 중요하지는 않은 잡지식인듯  

- 매개변수와 인자의 차이점은 중요! 잘 알아두기  
-> 매개변수 : 재사용할 때 쓰이는거  
-> 인자 : 함수를 실행할 때 실제로 들어가는 데이터 값

---

#### 인자의 종류  

##### 위치인자  
- 입력해야되는 데이터가 예를 들어 1000개가 넘어가면 위치인자에 맞게 데이터를 입력하기가 힘들다.

- 때문에 나온 것이 키워드 인자이다.  

##### 키워드인자  
- 함수 호출 시 인자의 이름과 값을 함께 전달하는 것  


##### 기본 인자 값
- 매개변수에 기본값을 할당하는 것  
- 함수 호출 시 인자 전달 없으면 기본값 활용  
- 위치인자와 달리 순서가 달라도 작동한다.  

##### 위치인자 + 키워드인자 같이 쓸 때 주의사항  
- 예시 : def functuon(위치, 위치, *, 키워드, 키워드 ...)  
- *는 위치인자가 끝나고 키워드 인자가 시작한다는 뜻으로 쓰인다.  

##### global  
- 실무에서 쓰면 욕먹어요.  
- 알고리즘 수업에서는 많이 쓰일 것이다.  
- ### **알고리즘에서 엄청 중요하다 공부 많이 열심히 숙달해두기!!!!!!!!!!!!!!!!!!!**

##### 재귀 함수
- 알고리즘에서 배워라

##### 맵 함수
- 맵 함수 실제 코드 안에는 for 반복문이 들어가 있다.  
- 실제로 쓸 수 있어야 한다.

##### 집 함수
- 알고리즘 ,데이터 분석에서 많이 쓰인다.  
- 두 그룹의 요소 개수가 다른 경우 실습해보기

##### 람다 함수
- lambda는 def func가 합쳐진 뜻
- 이런 방식으로 함수를 한 줄로 표현하는 것

##### 패킹 & 언패킹
- 언패킹 : 담겨있는 아이들을 하나하나 이름을 줘서 나누어 주는 것  


