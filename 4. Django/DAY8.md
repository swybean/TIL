# **Django_8일차** (3/28)
 
## **목차**
**Authentication System 1**

**1. Cookie & Session**  
-쿠키

**2. Authentication System**  

**3. Custom User model**  
-User Model 대체하기

**4. Login & Logout**  

**5. Template with Authentication data**  
-템플릿과 인증 데이터

---

## **1. Cookie & Session**

우리가 서버로 부터 받은 페이지를 볼 때, 우리는 서버와 서로 연결되어 있는 상태가 아니다.

**HTPP**   
HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약  
-> 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초  

**HTTP 특징**  
1. 비연결 지향 (connectionless)  
서버는 요청에 대한 응답을 보낸 후 연결을 끊음
2. 무상태 (stateless)  
연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음  

**상태가 없다는 것**  
예시 : 장바구니에 담은 상품 유지 불가능, 로그인 상태 유지 불가능  
-> 상태를 유지하기 위한 기술이 필요  

**쿠키 (Cookie)**  
서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각    

-> 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증 & 추적 & 상태 유지 등에 사용되는 데이터 저장 방식

-> 서버로부터 쿠키를 받고, 같은 서버에 다른 페이지로 재요청시마다 저장해 놓았던 쿠키를 함께 전송


**쿠키 사용 원리**  
1. 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장

2. 이렇게 쿠키를 저장해 놓았다가, 동일서버에 재요청 시 저장된 쿠키를 함께 전송  

쿠키는 두 요청이 동일한 브라우저에 들어왔는지 아닌지를 판단할 때 주로 사용됨  
-> 이를 통해 사용자의 로그인 상태를 유지할 수 있음   
-> 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 때문


**쿠키 사용 목적**  
1. 세션 관리 (Session management)  
로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화 (Personalization)  
사용자 선호, 테마 등의 설정

3. 트래킹 (Tracking)  
사용자 행동을 기록 및 분석

**세션 (Session)**  
서버 측에서 생성되어 클라이언트-서버 간의 상태를 유지  

-> 상태 정보를 저장하는 데이터 저장 방식  

-> 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄


**세션 작동 원리**  
1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장

2. 생성된 session 데이터에 인증할 수 있는 session id를 발급

3. 발급한 session id를 클라이언트에게 응답
4. 클라이언트는 응답 받은 session id를 쿠키에 저장 

5. 클라이언트가 다시 동일 서버에 접속하면 요청과 함께 (sesiion id가 저장된)쿠기를 서버에 전달  

6. 쿠키는 요청 시마다 서버에 함께 전송되므로 서버에서 session id를 확인해 로그인되어있다는 것을 알도록 함


**정리**  
서버 측에서는 세션 데이터 생성 후 저장, 해당 데이터에 접글할 수 있는 세션 ID를 생성    
-> 세션 데이터에 '기한' 설정 가능  
-> 일정시간이 지나면 자동 로그아웃되는 것 (SWEA)

이 ID를 클라이언트 측으로 전달하고, 클라이언트는 쿠키에 이 ID를 저장

이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송  

로그아웃하면 서버가 session 데이터 삭제

-예시 : 로그인 상태 유지를 위해 로그인 되었다는 사실을 입증하는 데이터를 매 요청마다 계속해서 보내는 것  

**쿠키와 세션의 목적**
서버와 클라이언트 간의 '상태'를 유지


### **[참고]**

**쿠키 종류별 수명(lifetime)**  
1. Session cookie
현재 세션(current session)이 종료되면 삭제됨  
브라우저 종료와 함께 세션이 삭제됨

2. Persistent cookies
Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨  

**세션 in Django**  
Django는 'database-backed sessions' 저장 방식을 기본 값으로 사용  

session 정보는 DB의 django_session 테이블에 저장됨  

Django는 요청 안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄  

Django는 우리가 session 메커니즘에 대부분을 생가하지 않게 많은 도움을 줌



---



## **2. Authentication System**  
사용자 인증과 관련된 기능을 모아 놓은 시스템

**Authentication (인증)**  
사용자가 자신이 누구인지 확인하는 것 (신원 확인)

**실습 사전준비**  

두번째 app으로 accounts 생성 및 등록  
-> auth와 관련한 경로&키워드들은 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 **accounts라는 이름을 사용하는 것을 권장**


---


## **3. Custom User model** 

**User model 대체하기**  
django가 기본적으로 제공하는 User name이 아닌 직접 작성한 User model을 사용하기 위해서  

**User 클래스를 대체하는 이유**  
지금까지는 별도의 User 클래스 정의 없이 내장된 auth 앱에 작성된 클래스를 사용했음

별도 설정 없이 사용할 수 있어 간편하지만, 개발자가 **직접 수정할 수 없는 문제가 존재**


**대체하기**   
1. AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성  
-기존 User 클래스도 AbstractUser를 상속받기 때문에 이것만 하면  
-커스텀 User 클래스도 기존 User 클래스와 완전히 같은 모습을 가지게 됨

2. django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 User 모델로 지정  
-수정 전 기본값은 'auth.User'

3. admin site에 대체한 User 모델 등록  
-기본 User 모델이 아니기 때문에 등록하지 않으면 출력되지 않기 때문

**AUTH_USER_MODEL**  
Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정

### **※주의※**  
프로젝트 중간에 AUTH_USER_MODEL 변경 불가능  
-> 데이터베이스 초기화 후 진행해야 함

**프로젝트 시작할 때 반드시 User 모델을 대체해야 한다**  
Django는 새 프로젝트를 시작하는 경우 커스텀 User 모델을 설정하는 것을 강력하게 권장  

커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 **필요한 경우 나중에 맞춤 설정할 수 있기 때문**  

**User 모델 대체 작업은 프로젝트의 모든 migrations, 첫 migrate를 실행하기 전에 해야 한다!!!!!**


---

## **4. Login & Logout**  

**Login**  
Session을 Create하는 과정

**AuthenticationForm( )**  
로그인 인증에 사용할 데이터를 입력 받는 built-in form  
-> modelform이 아니다!

**form과 modelform의 공통점과 차이점**    
공통점 : 사용자 입력 데이터를 받는 역할  
차이점 : form은 받은 데이터를 DB에 저장 안한다. vs modelform은 DB에 저장한다.


**login(request, user)**  
AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

**get_user( )**  
AuthenticationForm의 인스턴스 메서드  
-> 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

---

**Logout**  
Session을 Delete하는 과정

**logout(request)**  
현재 요청에 대한 Session Data를 DB에서 삭제  
클라이언트 쿠키에서도 Session Id를 삭제


---

## **5. Template with Authentication data**  

**Template with Authentication data**  
템플릿에서 인증 관련 데이터를 출력하는 방법

**현재 로그인 되어있는 유저 정보 출력하기**  
user라는 context 데이터를 사용할 수 있는 이유는?  
-> django가 미리 준비한 context 데이터가 존재하기 때문 (context processorts)  

**context processorts**  
템플릿이 렌더링 될 때 호출 가능한 context 데이터 목록  

작성된 context 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨  

django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것

---

## **[참고]**  

**'AbstractUser' class**  
관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스

몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

DB 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨



