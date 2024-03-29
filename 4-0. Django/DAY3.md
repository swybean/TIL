# **Django_3일차** (3/14)
 
## **목차**
**1. Django URLs**  
-App과 URL  
-URL 이름 지정  
-URL 이름 공간

**2. Django Model**  
-Model  
-Migrations  
-Admin site

---

## **1. Django URLs**

**URL dispatcher**  
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결 (매핑)

**App URL mapping**  
각 앱에 URL을 정의하는 것  
-> 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함

**2번째 앱 pages 생성 후 발생할 수 있는 문제**  
view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하는 경우  
해결방법 : **URL을 각자 app에서 관리하자**

**include( )**  
프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수  
URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

## **URL 이름 지정**

**URL 구조 변경에 따른 문제점**  
기존 'articles/' 주소가 'articles/index/'로 변경됨에 따라 해당 주소를 사용하는 모든 위치를 찾아가 변경해야 함  
-> 해결방법 : URL에 이름을 지어주고 이름만 기억하자!

**Naming URL patterns**  
URL에 이름을 지정하는 것  
(path 함수의 name 인자를 정의해서 사용)

**URL 표기 변화**  
a 태그의 href 속성값 뿐만 아니라 form의 action속성처럼 url을 작성하는 모든 위치에서 변경  

**'url' tag**  
{% url 'url name' arg1 arg2 %}  
주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환  

## **URL 이름 공간**  

**URL 이름 지정 후 남은 문제**  
articles 앱의 url 이름과 pages 앱의 url 이름이 같은 상황  
단순히 이름만으로는 완벽하게 분리할 수 없음  
해결방법 : **이름에 성(key)을 붙이자**

**app_name 속성 지정**  
app_name = 'articles' 같이 app_name 변수 값 설정  

**URL tag의 최종 변화**  
{% url 'index' %} -> {% url 'articles:index' %}

---



## **2. Django Model**  

**Django Model**  
DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공   
-> 테이블 구조를 설계하는 청사진(blueprint)  

**model 클래스 살펴보기**  
작성한 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦 (교재 30쪽 그림)  
-> **id 필드는 Django가 자동 생성**

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

# title, content : 필드 이름  
# CharField, TextField : 데이터 타입
# (max_length=10) : 제약 조건 (길이 10자 제한)
```

1django.db.models 모듈의 Model이라는 부모 클래스를 상속 받음  

Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스  

개발자는 가장 중요한 **테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록** 하기 위한 것  
(상속을 활용한 프레임워크의 기능 제공)

1. 클래스 변수명  
테이블의 각 "필드(열)의 이름"  

2. model Field 클래스  
테이블 필드의 "데이터 타입"  

3. model Field 클래스의 키워드 인자 (필드 옵션)  
테이블 필드의 "제약조건" 관련 설정  

**제약 조건**  
데이터가 올바르게 저장되고 관리하도록 하기 위한 규칙   


---


**Migrations**  
model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법  


**Migrations 과정**  
model class (설계도 초안) -> migration 파일 (최종 설계도) -> db.sqlite3 (DB)  

DB가 설계도 초안을 이해하지 못하기 때문에 Django가 최종 설계도로 만들어줘서 DB에 보내줘야 한다.

**Migrations 핵심 명령어 2가지**  
python manage.py makemigrations  
-> model class를 기반으로 최종 설계도(migration) 작성  

python manage.py migrate  
-> 최종 설계도를 DB에 전달하여 반영

**migrate 후 DB 내에 생성 된 테이블 확인**  
Articles 모델 클래스로 만들어진 articles_article 테이블

**이미 생성된 테이블에 필드를 추가하려면**  
이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본값 설정이 필요  
-> 빈 필드는 추가로 못 넣는다. 무조건 기본값이 있어야 함

python manage.py makemigrations를 치면 아래 2줄이 나온다. 둘 중에서 하나를 골라야 함
  
1번 : 현재 대화를 유지하면서 직접 기본 값을 입력하는 방법   
2번 : 현재 대화에서 나간 후 models.py에 기본값 관련 설정을 하는 방법 

1번 방법 권장

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# created_at와 update_at 줄이 추가하는 것
```

---

### **Model Field**  
DB 테이블의 **필드(열)** 을 정의하며, 해당 필드에 저장되는 **데이터 타입**과 **제약조건**을 정의


**CharField( )**  
길이의 제한이 있는 문자열을 넣을 때 사용  
(필드의 최대 길이를 결정하는 max_length는 필수 인자)

**TextField( )**  
글자의 수가 많을 때 사용  

**DateTimeField( )**  
날짜와 시간을 넣을 때 사용 

**auto_now**  
데이터가 **저장될 때마다** 자동으로 현재 날짜 시간을 저장

**auto_now_add**  
데이터가 **처음 생성될 때만** 자동으로 현재 날짜 시간을 저장

---

**Automatic admin interface**  
Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공  
-> 데이터 확인 및 테스트 등을 진행하는데 매우 유용

1. admin 계정 생성  
> python manage.py createsuperuser  

email은 선택사항이기 때문에 입력하지 않고 진행 가능  
비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기  

2. DB에 생성된 admin 계정 확인하기

3. admin에 모델 클래스 등록  
admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능  

4. admin site 로그인 후 등록된 모델 클래스 확인  

5. 데이터 생성, 수정, 삭제 테스트

6. 테이블 확인

---

**데이터베이스 초기화**  
1. migration 파일 삭제  
2. db.sqlite3 파일 삭제  
**아래 파일과 폴더는 지우지 않도록 주의**  
\_\_init__.py  
migrations 폴더


**Migrations 기타 명령어**  
1. python manage.py showmigrations  
migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어  
[X] 표시가 있으면 완료되었다는 의미  

2. python manage.py sqlmigrate articles 0001  
해당 migrations 파일이 SQL언어(DB에서 사용하는 언어)로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어


**첫 migrate 시 출력 내용이 많은 이유는?**   
Django 프로젝트가 동작하기 위해 미리 작성되어 있는 기본 내장 app들에 대한 migrate 파일들이 함깨 migrate 되기 때문이다.

**SQlite**  
데이터베이스 관리 시스템 중 하나  
Django의 기본 데이터베이스로 사용됨  
(파일로 존재하며 가볍고 호환성이 좋음)

**CRUD**  
소프트웨어가 가지는 기본적인 데이터 처리 기능  
Create : 저장  
Read : 조회   
Update : 갱신  
Delete : 삭제  







