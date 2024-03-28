# **Django_7일차** (3/27)
 
## **목차**

**1. Static files**
-Static files 제공하기

**2. Media files**
-이미지 업로드  
-업로드 이미지 제공

---

## **1. Static files**
서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (정적 파일)  
(이미지, JS, CSS파일 등)

**웹 서버와 정적 파일**  
웹 서버의 기본동작은 **특정 위치(URL)에 있는 자원**을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것  

-> "자원에 접근 가능한 주소가 있다"라는 의미  
-> 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함  
-> **정적 파일을 제공하기 위한 경로(URL)** 가 있어야 함

**static_url**  
기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL  
-> 실제 파일 & 디렉토리가 아니며, URL로만 존재

**Static files 제공하기**  
1. 기본 경로에서 제공하기  
articles/static/articles 경로에 이미지 파일 배치   
static tag를 사용해 이미지 파일에 대한 경로 제공  
{% load static %}  
-> \<!DOCTYPE html> 위에 적는걸 권장  
\<img src="{% static 'articles/sample-1.png' %}" alt="img">


2. 추가 경로에서 제공하기    


---

필기만함 (교재는 집에서 정리하기)  

static > media 파일  
다이어그램으로 보면 스태틱 안에 media가 들어있다.


원래 게시글 작성 테이블에 필드는  
id, title, content, creat, update 만 있었는데 image 필드를 추가해야한다.  
-> 단, 이미지가 들어가는 것은 아니고 이미지 경로가 들어간다.  
-> 이미지 필드의 부모필드는 CharField다.


form action은 기본적으로 텍스트 형태의 데이터만 보낼 수 있다.  
이미지를 보내려면 추가적으로 속성값을 해줘야 한다.   
method 속성 뒤에 enctype="multipart/form-data"를 추가해줘야 한다.