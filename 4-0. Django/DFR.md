## 목차

**1. REST API**   
-자원의 식별  
-자원의 행위   
-자원의 표현

**2. DRF with Single Model**   
-DRF  
-GET  
-POST  
-DELETE  
-PUT


---

### REST API

**API (Application Programming Interface)**   
두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘  
-> 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계


**Web API**   
웹 서버 또는 웹 브라우저를 위한 API  

현대 웹 개발은 직접 개발보다 여러 Open API를 활용하는 추세  

대표적인 Third Party Open API 목록  
-> Youtube, Google Map, Naver Papago, Kakao Map 등


**REST (Representational State Transfer)**  
API Sever를 개발하기 위한 일종의 소프트웨어 설계 '방법론'

API Sever를 설계하는 구조가 모두 다르니, 이렇게 맞춰서 설계하는게 어때? -> 규칙은 아님


**RESTful API**   
REST 원리를 따르는 시스템을 RESTful하다고 부름  

'자원을 정의'하고 '자원에 대한 주소를 지정'하는 전반적인 방법을 서술  


**REST API**   
REST라는 설계 디자인 약속을 지켜 구현한 API


**REST에서 자원을 사용하는 3가지 방법**   
1\. 자원의 '식별'   
\- URI   

2\. 자원의 '행위'   
\- HTTP Methods   

3\. 자원의 '표현'    
\- JSON 데이터   
\- 궁극적으로 표현되는 데이터 결과물

---

### 자원의 식별

**URI**  
URI (Uniform Resource Identifier) : 통합 자원 식별자   
인터넷에서 리소스(자원)를 식별하는 문자열   
-> 대표적인 URI는 웹 주소로 알려진 URL


**URL (Uniform Resource Locator)**   
웹에서 주어진 리소스의 주소 (네트워크 상 리소스가 어디 있는지를 알려주기 위한 약속)

**Schema (Protocol)**   
브라우저가 리소스를 요청하는데 사용해야 하는 규약   
URL의 첫부분은 브라우저가 어떤 규약을 사용하는지를 나타냄   

**Domain Name**   
요청 중인 웹 서버를 나타냄   
어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능 (편의를 위해 Domain Name 사용)

**Port**   
웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)  
HTTP 프로토콜의 표준 포트 (HTTP: 80, HTTPS: 443)  
-> 표준포트만 작성 시 생략 가능

**Path**   
웹 서버의 리소스 경로 (실제 위치가 아닌 추상화된 형태의 구조를 표현)

**Parameters**   
웹 서버에서 제공하는 추가적인 데이터  
'&' 기호로 구분되는 key-value 쌍 목록  
서버는 리소스 응답 전에 파라미터를 사용해 추가 작업 수행 가능

**Anchor**  
일종의 '북마크'를 나타내며, 브라우저 해당 지점에 있는 콘텐츠를 표시  
'#' 이후 부분은 '부분 식별자'라고 부르며 서버에 전송되지 않음

---

### 자원의 행위

**HTTP Request Methods**  
리소스에 대한 행위(수행하고자 하는 동작)를 정의

**대표 HTTP Request Methods**  
1\. GET  
\- 서버에 리소스의 표현을 요청   
\- GET을 사용하는 요청은 데이터만 검색해야 함

2\. POST  
\- 데이터를 지정된 리소스에 제출   
\- 서버의 상태를 변경   

3\. PUT  
\- 요청한 주소의 리소스를 수정

4\. DELETE  
\- 지정된 리소스를 삭제

**HTTP response status codes**   
특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄

100부터 500번대까지 존재함 (400번대: 클라이언트 에러, 500번대: 서버 에러)

---

### 자원의 표현

Django 서버는 기존에는 사용자에게 페이지(html)만 응답했으나 REST API 서버로 변환하면 JSON 데이터를 응답한다.

더 이상 Template 부분에 대한 역할을 담당하지 않으며 프론트-백이 분리되어 구성된다.

---

### DFR with Single Model

**DRF (Django REST framework)**   
Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리


**Serialization (직렬화)**   
여러 시스템에서 활용하기 위해 데이터 구조 & 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

-> 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정


**Serializer**   
Serialization을 진행하여 Serialized data를 반환해주는 클래스


**ModelSerializer**    
Django 모델과 연결된 Serializer 클래스  
-> 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞춰 Serialization을 진행


**ModelSerializer의 인자 및 속성**    
many 옵션 : Serialize 대상이 QuerySet인 경우 입력

data 속성 : Serialized data 객체에서 실제 데이터를 추출


**'api_view' decorator**   
DRF view 함수에서 '필수로 작성'되며, view 함수를 실행하기 전 HTTP 메서드를 확인  

기본적으로 GET 메서드만 허용, 다른 메서드 요청은 405 Method Not Allowed로 응답


**'partial' argument**   
부분 업데이트를 허용하기 위한 인자

기본적으로 serializer는 모든 필수 필드에 대한 값을 전달 받기 때문에 부분적으로 업데이트를 하기 위해서는 partial 인자 값이 True여야 한다.


**raise_exception**    
is_valid()의 선택 인자  

유효성 검사를 통과하지 못할 경우 ValidationError 예외를 발생시킴

DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리, 기본적으로 HTTP 400 응답을 반환


















