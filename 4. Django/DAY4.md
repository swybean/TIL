# **Django_4일차** (3/25)
 
## **목차**

**1. ORM**  

**2. QuerySet API**  

**3. QuerySet API 실습**
-Create  
-Read  
-Update  
-Delete

---

## **1. ORM**
Object-Relational-Mapping  
객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

**ORM의 역할**  
djnago와 Database가 사용하는 언어가 다르기 때문에 소통불가    
(django = python, Database = SQL)

django에 내장된 ORM이 중간에서 이를 해석

---

## **2. QuerySet API**  
ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구  
-> API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

![QuerySet API](./img/QuerySet_API.png)

---

**QuerySet API 구문**  
예시 : Article.objects.all( )  

Article : Model class  
onjects : Manager  
all( ) : QuerySet API

뜻 : Article에 있는 모든(all) 데이터를 조회해라

![QuerySet API 구문 동작 예시](./img/QuerySet_API2.png)

우리가 처리해야하는건 1번, 4번 과정만 잘하면 된다!

---

**Query**  
데이터베이스에 특정한 데이터를 보여 달라는 **요청**  

"쿼리문을 작성한다.""  
-> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.  

파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달  

**QuerySet**  
데이터베이스에서 전달 받은 객체 목록 (데이터 모음)  
-**순회가 가능**한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음  
-> 순회가능 = 반복가능 : for문의 사용이 가능하다.  
-> 리스트처럼 다루면 된다.

Django ORM을 통해 만들어진 자료형  

단, 데이터베이스가 **단일한 객체**를 반환 할 때는 QuerySet이 아닌 **모델(Class)의 인스턴스로 반환**됨  

**정리**  
우리가 DB에 보내는 요청 : Query (쿼리)  
DB의 응답을 해석 가능하게 만들어 받는 것 : QuerySet  

**QuerySet API**  
python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것  
(CRUD : Create, Read, Update, Delete)

---


## **3. QuerySet API 실습**  

### **Create**

**사전 준비**  
ipython, django-extensions 설치 필요  

**Django shell**  
Django 환경 안에서 실행되는 python shell  
(입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침)  

**Django shell 실행**  
python manage.py shell_plus  


**데이터 객체를 만드는(생성하는) 3가지 방법**  
@@@@@@@@@@@@@교재 22쪽~ 참고해서 마저 완성하기
강의 다시보기 꼭 보면서 해야함@@@@@@@@@@@@@@@


**save( )**  
객체를 데이터베이스에 저장하는 메서드

---

### **Read**
**대표적인 조회 메서드**  
1. Return new QuerySets : all( ), filter( )  
all( ) : 전체 데이터 조회  
-> 결과값이 없더라도 QuerySet으로 준다.  
filter( ) : 특정 조건 데이터 조회

2. Do not return QuerySets : get( )  
get( ) : 단일 데이터 조회

**get( ) 특징**  
객체를 찾을 수 없으면 DoesNotExist 예외를 발생  
둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생  
-> 위와 같은 특징 때문에 **primary key와 같이 고유성(Uniqueness)를 보장하는 조회에서 사용**해야 함  

---

### **Update**
**데이터 수정**  
인스턴스 변수를 변경 후 save 메서드 호출

---

### **Delete**
**데이터 삭제**  
삭제하려는 데이터 조회 후 delete 메서드 호출

한 번 지운 pk값(id)는 **재사용 하지 않음**  
-> 1~4번까지 있는데 2, 4번을 지우고 새로 추가해도 5, 6번이 생기고 2, 4번이 다시 생기지 않는다.



### **[참고]**
**Field lookups**  
특정 레코드에 대한 조건을 설정하는 방법  

QuerySet aptjem filter(), exclude(), get()에 대한 키워드 인자로 지정

**ORM, QuerySet API를 사용하는 이유**  
데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함  

데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움












