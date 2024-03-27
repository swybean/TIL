# **Django_5일차** (3/26)
 
## **목차**

**Django Form**  

**1. Django Form**
-Form Class  
-Widgets

**2. Django ModelForm**

**3. Handling HTTP request**
-View 함수 구조 변화

---

## **1. Django Form**

**HTML 'form'**  
지금까지 사용자로부터 데이터를 받기 위해 활용한 방법  
-> 문제점 : 비정상적 & 악의적인 요청 필터링 불가능  
-> 유효한 데이터인지에 대한 확인이 필요

**유효성 검사**  
수집한 데이터가 정확하고 유효한지 확인하는 과정

**유효성 검사 구현**  
입력 값, 형식, 중복, 범위, 보안 등 많은 것을 고려해야 함  
이런 기능을 직접 개발하지 않고 Django가 제공하는 Form을 사용

### **Form Class**

**Django Form**  
사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구  
-> 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공  

즉, Django가 데이터의 유효성 검사까지 내부적으로 알아서 처리해주는 것  
-> 개발자는 어떻게 보내고 저장할지만 생각하면 된다.

### **Widget**

**Widgets**  
HTML 'input' element의 **표현**을 담당

**Widget 사용**  
Widget이란 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

---

## **2. Django ModelForm**

**Form**  
사용자 입력 데이터를 DB에 저장하지 않을 때 (로그인 등)  

**ModelForm**  
사용자 입력 데이터를 DB에 저장해야 할 때 (게시글 작성, 회원가입 등)

**Meta class**  
Model Form의 정보를 작성하는 곳  

**fields 및 exclude 속성**  
exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음  

우리가 쓴 __all__은 모든 필드를 가져오는 것  
-> 근데 한두개만 빼면 되면 exclude를 사용하는 것이 더 편하고 빠르다.

**is_valid()**  
여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환  

**save()**  
데이터베이스 객체를 만들고 저장

**save() 메서드가 생성과 수정을 구분하는 법**  
키워드 인자 instance 여부를 통해 생성, 수정을 결정한다.  

**Django Form 정리**  
사용자로부터 데이터를 수집하고 처리하기 위한 강력한 도구  
-> HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

---

## **3. Handling HTTP request**

**new & create view 함수간 공통점 및 차이점**  
공통점 : 데이터 생성을 구현하기 위함
차이점 : new함수는 GET 요청만 들어오지만, create함수는 POST 요청만 들어온다.  
-> 즉, 공동의 목적을 가지고 있지만 받아내는 메서드 자체가 분리되어 있다.  

따라서 2개의 view 함수를 하나로 합칠 수 있다.  













