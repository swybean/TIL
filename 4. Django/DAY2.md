# **Django_2일차** (3/13)
 
## **목차**
**1. Template System**  
-템플릿 상속

**2. HTML form (요청과 응답)**  
-form 활용

**3. Django URLs**  
-변수와 URL

---

## **1. Template System**

### **Django Template system**  
데이터 **표현을 제어**하면서, **표현**과 관련된 부분을 담당  
-> **표현**을 담당하는 것!!

#### Django Template Language (DTL)
Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템  

#### DTL Syntax (DTL 문법)
1. Variable   
render 함수의 세번째 인자로 **딕셔너리** 데이터를 사용  
딕셔너리 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨  
dot(.)을 사용하여 변수 속성에 접근할 수 있음  

2. Filters   
표시할 변수를 수정할 때 사용 (변수 + | + 필터)  
chained(연결)이 가능하며 일부 필터는 인자를 받기도 함  
약 60개의 built-in template filters를 제공

3. Tags  
반복 또는 논리를 수행하여 제어 흐름을 만듦  
일부 태그는 시작 & 종료 태그가 필요  
약 24개의 built-in template tags를 제공  

4. Comments   
DTL에서의 주석  
시작부분에 {% comment %}, 종료부분에 {% endcomment %}를 쓰면 중간에 있는 것들이 주석처리된다.  

### **템플릿 상속**

#### 기존 템플릿 구조의 한계   
모든 템플릿에 bootstrap을 적용하려면 모든 템플릿에 bootstrap CDN을 작성해야 한다.  
-> 부모 템플릿에 CDN을 작성하고 자식 템플릿들이 상속 받으면 템플릿마다 CDN을 작성하지 않아도 된다.

#### 템플릿 상속 (Template inheritance)   
**페이지의 공통요소**를 포함하고,   
**하위 템플릿이 재정의 할 수 있는 공간**을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축  

**extends tag**  
자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림  
( 반드시 자식 템플릿 최상단에 작성되어야 함, 1개만 가능)  

**lock tag**  
하위 템플릿에서 재정의 할 수 있는 블록을 정의  
(상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것)

---

## **2. HTML form (요청과 응답)**

#### 데이터를 보내고 가져오기
Sending and Retrieving form data  
HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

**form element**  
사용자로부터 할당된 데이터를 서버로 전송  
웹에서 사용자 정보를 입력하는 여러 방식 (text, password, checkbox 등)을 제공  

**form의 핵심 속성 2가지**   
데이터를 **어디(action)** 로 **어떤 방식(method)** 으로 요청할지

1. **action**  
입력 데이터가 전송될 URL을 지정 (목적지)  
만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐  

2. **method**  
데이터를 어떤 방식으로 보낼 것인지 정의  
데이터의 HTTP request methods (GET, POST)를 지정  
기본적으로는 GET 방식 사용  
POST는 주로 로그인 때 사용 -> URL에 ID, PW 입력값이 노출되지 않아야 하기 때문에


**input element**  
사용자의 데이터를 입력 받을 수 있는 요소  
type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

**name attribute**  
입력한 데이터에 붙이는 이름 (key)   
input의 핵심 속성  
데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음  

**Query String Parameters**  
사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법  
문자열은 앰퍼샌드('&')로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표('?')로 구분됨  

예시 : http://hose:port/path?**key=value&key=value**


#### HTTP request 객체  
form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음 (view 함수의 첫 번째 인자)

**BASE_DIR**  
setting에서 경로지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수  

#### DTL 주의사항  
Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭만 같을뿐 **Python 코드로 실행되는 것이 아니며 Python과는 관련 없음**  

프로그래밍적 로직이 아니라 표현을 위한 것임을 명심!!

프로그래밍 로직은 되도록 view 함수에서 작성 및 처리할 것  

공식문서를 참고해 다양한 태그와 필터 사용해보기




## **3. Django URLs**  

**URL dispatcher**  
운항 관리자, 분배기  
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결 (매핑)


**현재 URL 관리의 문제점**  
템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해야 한다.  

**Variable Routing**  
URL 일부에 변수를 포함시키는 것  
(변수는 view 함수의 인자로 전달 할 수 있음)

**Path converters**  
URL 변수의 타입을 지정  
(str, int 등 5가지 타입 지원)


**Trailing Slashes**  
Django는 URL 끝에 '/'가 없다면 자동으로 붙임

기술적인 측면에서 foo.com/bar와 foo.com/bar/는 서로 다른 URL이다.  

그래서 Django는 검색엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택한 것  

그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의









