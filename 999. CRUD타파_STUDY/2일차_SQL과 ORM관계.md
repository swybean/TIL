
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    page_count = models.IntegerField()
```


문제 1번  
작성된 Book 클래스와 동일한 테이블을 생성할 수 있는 SQL문을 작성하시오. 
```SQL
-- 테이블 생성 
CREATE TABLE Book(
    -- 타이틀, 문자열(200자 제한), NULL값 불가능
    title VARCHAR(200) NOT NULL,
    -- 내용, 텍스트
    description TEXT NOT NULL,
    -- 쪽수, 정수형, NULL값 불가능
    page_count INTEGER NOT NULL
);
```
CREATE TABLE : 테이블을 생성하는 문  
필드명, 데이터 타입, 제약조건 순으로 쓴다.

title은 필드명, 데이터타입은 문자열 200자 제한, 제약조건으로는 NULL값 불가능.

description은 필드명, 데이터타입은 텍스트, 제약조건은 NULL값 불가능.

page_count는 필드명, 데이터타입은 정수형, 제약조건은 NULL값 불가능.

NOT NULL 제약조건을 넣은 이유?  
데이터의 무결성을 보장하기 위해서.  
데이터가 누락되거나, 부적절한 값이 들어가면 데이터의 일관성과 정확성이 떨어지기 때문이다.   

사용자는 항상 유해하고, 나쁘고, 바보라 이상한 값을 넣을 것이라고 생각하고 제약조건을 설정해줬다.



문제 2번   
제목 : ‘장고 입문’, 내용 ‘장고를 공부하자’, 그리고 페이지 수는 350을 가지는 레코드 작성을 위한 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
INSERT INTO Book(title, description, page_count)
VALUE ('장고 입문', '장고를 공부하자', 350);
```

ORM
```python
book = Book.objects.create(title='장고 입문', description='장고를 공부하자', page_count=350)
```


문제 3번   
 book 테이블에 저장된 모든 레코드를 조회하는 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
SELECT * FROM Book;
```
Book 테이블의 모든 레코드를 조회한다.

ORM
```python
book = Book.objects.all()
```
book에 Book 테이블에 담긴 모든 정보를 할당한다.




문제 4번    
페이지 수를 350 페이지 이상 가지는 레코드를 조회하시오.

SQL문
```SQL
SELECT * FROM Book
WHERE page_count >= 350;
```

ORM
```python
book = Book.objects.filter(page_count__gte=350)

# __get= : 이게 ORM에서 사용하는 '~이상'을 의미하는 조건 연산자이다.
```



문제 5번    
‘장고 입문’ 제목을 가진 레코드의 페이지 수를 500 으로 바꾸는 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
UPDATE Book
SET page_count = 500
WHERE title = '장고 입문';
```

ORM
```python
Book.objects.filter(title='장고 입문').update(page_count=500)
```


문제 6번  
'장고 심화', 내용 '장고를 마스터하자', 그리고 페이지 수는 450을 가지는 레코드 작성을 위한 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
INSERT INTO Book(title, description, page_count)
VALUE ('장고 심화', '장고를 마스터하자', 450);
```

ORM
```python
book = Book.objects.create(title='장고 심화', description='장고를 마스터하자', page_count=450)
```



문제 7번  
저장된 데이터의 평균 페이지 수를 구하는 SQL 문을 작성하시오 (힌트: 집계함수를 활용한다)

SQL문
```SQL
SELECT AVG(page_count) FROM Book;
```



문제 8번  
'장고 심화' 제목을 가진 레코드를 삭제하는 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
DELETE FROM Book
WHERE title = '장고 심화';
```

ORM
```python
Book.objects.filter(title='장고 심화').delete()
```



문제 9번  
book 을 제거하는  SQL 문을 작성하시오.

SQL문
```SQL
-- Book 테이블의 모든 레코드를 지우는 법
DELETE FROM Book;

-- Book 테이블 자체를 지우는 방법
DELETE TABLE Book;
```




문제 10번  
username 필드를 갖는 user 테이블을 생성하는 SQL 문과 ORM 을 작성하시오.

SQL문
```SQL
CREATE TABLE User(
    username VARCHAR(50) NOT NULL
);

```

ORM
```python

```













