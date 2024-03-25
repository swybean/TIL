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


**QuerySet API 구문**  
Article.objects.all( )  

Article : Model class  
onjects : Manager  
all( ) : QuerySet API

![QuerySet API 구문 동작 예시](./img/QuerySet_API2.png)


**Query**  





