### **기본 지식 퀴즈**

1. **SQL과 Django ORM 비교하기**
    - 모든 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT * FROM books_book;`**
        - Django ORM: **`Book.objects.all()`**
2. **단일 객체 조회 방법**
    - 'id'가 5인 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT * FROM books_book WHERE id=5;`**
        - Django ORM: **`Book.objects.get(pk=5)`**
3. **복수 객체 조회 메소드**
    - **`first()`**와 **`last()`** 메소드를 사용하여 각각 첫 번째 책과 마지막 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - 첫 번째 책
            - SQL: **`SELECT * FROM books_book ORDER BY id ASC LIMIT 1;`**
            - Django ORM: **`Book.objects.all().first()`**
        - 마지막 책
            - SQL: **`SELECT * FROM books_book ORDER BY id DESC LIMIT 1;`**
            - Django ORM: **`Book.objects.all().last()`**

### **고급 퀴즈**

1. **조건부 조회**
    - 작가의 **`id`**가 1인 모든 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT * FROM books_book WHERE author_id=1;`**
        - Django ORM: **`Book.objects.filter(author_id=1)`**
2. **대소관계를 사용한 필터링**
    - 페이지 수가 100페이지를 초과하는 모든 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT * FROM books_book WHERE page_count > 100;`**
        - Django ORM: **`Book.objects.filter(page_count__gt=100)`**
3. **정렬과 제한**
    - 가격이 낮은 순으로 10권의 책을 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요. 만약 가격이 동일하다면, 최근에 출판된 책이 먼저 나오도록 하세요.
        - SQL: **`SELECT * FROM books_book ORDER BY price ASC, created_at DESC LIMIT 10;`**
        - Django ORM: **`Book.objects.all().order_by('price', '-created_at')[:10]`**

### **응용 퀴즈**

1. **집계 함수 사용하기**
    - 모든 책의 총 페이지 수를 구하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT SUM(page_count) FROM books_book;`**
        - Django ORM: **`Book.objects.aggregate(total_pages=Sum('page_count'))`**
2. **annotate 사용하기**
    - 각 카테고리별로 총 책의 수를 구하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT category, COUNT(*) FROM books_book GROUP BY category;`**
        - Django ORM: **`Book.objects.values('category').annotate(total_books=Count('id')).order_by('category')`**
3. **복잡한 쿼리 작성하기**
    - '프로그래밍' 카테고리의 책 중에서 가장 최근에 리뷰가 작성된 리뷰 5개를 조회하는 SQL 쿼리와 Django ORM 코드를 작성하세요.
        - SQL: **`SELECT * FROM books_review WHERE book_id IN (SELECT id FROM books_book WHERE category='programming') ORDER BY created_at DESC LIMIT 5;`**
        - Django ORM: **`Review.objects.filter(book__category='programming').order_by('-created_at')[:5]`**

### **심화 퀴즈**

### 문제 1: **`select_related`** 사용하기

다음 SQL 쿼리를 참고하여 동일한 결과를 반환하는 Django ORM 코드를 작성하세요. 이때, **`select_related`**를 사용하여 관련 작가 정보를 포함하여 모든 책을 조회하도록 합니다.

- SQL 쿼리:
    
    ```sql
    sqlCopy code
    SELECT books_book.*, auth_user.*
    FROM books_book
    JOIN auth_user ON books_book.author_id = auth_user.id;
    
    ```
    
- Django ORM 코드:
    
    - A) **`Book.objects.all()`**
    - B) **`Book.objects.select_related('author')`**
    - C) **`Book.objects.prefetch_related('author')`**
    - D) **`Author.objects.select_related('book')`**

### 문제 2: **`prefetch_related`** 사용하기

다음 상황에 맞는 Django ORM 코드를 작성하세요. 각 책과 그에 대한 모든 리뷰를 조회할 때, **`prefetch_related`**를 사용하여 리뷰를 효율적으로 불러오도록 합니다. 아래의 SQL 쿼리들은 이 작업을 수동으로 할 때의 예시입니다.

- SQL 쿼리 (책 조회):
    
    ```sql
    sqlCopy code
    SELECT * FROM books_book;
    
    ```
    
- SQL 쿼리 (해당 책의 리뷰 조회, 각 책에 대해 별도로 실행):
    
    ```sql
    sqlCopy code
    SELECT * FROM books_review WHERE book_id = ?;
    
    ```
    
- Django ORM 코드:
    
    - A) **`Book.objects.all()`**
    - B) **`Book.objects.select_related('reviews')`**
    - C) **`Book.objects.prefetch_related('reviews')`**
    - D) **`Review.objects.prefetch_related('book')`**

### **정답:**

- 문제 1의 정답: B) **`Book.objects.select_related('author')`**
- 문제 2의 정답: C) **`Book.objects.prefetch_related('reviews')`**