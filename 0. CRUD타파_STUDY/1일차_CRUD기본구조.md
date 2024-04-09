```python
# Create 로직을 구현하기 위해서는 view 함수 2개가 필요
# new : 사용자 입력 데이터를 받을 페이지를 렌더링
# create : 사용자가 입력한 데이터를 받아 DB에 저장

# def create(request):를 작성해보기 전에 알아보자

		# HTTP는 네트워크 상에서 데이터를 주고 받기 위한 통신규약이다.
		# HTTP request methods는 데이터(리소스)에 어떤 요청(행동)을 원하는지 나타내는 것이다.
		# request는 클라이언트가 서버로 보내는 HTTP 요청에 대한 정보를 담고 있는 객체이다.
		# 이에 서버가 응답하는 것을 response라고 한다.

		# request는 view함수의 첫번째 매개변수이다.
		# request 객체에는 클라이언트로부터 받은 모든 요청 정보가 포함되어 있다. (데이터, URL, HTTP method 등)		
		
		# method의 종류로는 GET과 POST가 있다.
		
		## GET과 POST는 개발자들끼리 코드를 볼 때, 직관적으로 알기 쉽게 하기 위해서 구분하는 것이다.
		## 무엇을? -> GET은 DB 변경을 주지 않는 데이터이고, POST는 DB에 영향을 주는 데이터라는 것을.
		## 즉, GET으로도 리소스를 변경(생성, 수정, 삭제)을 할 수 있다. 근데 하지 말자. 약속이다.
		
		## GET은 특정 리소스를 '조회'할 때만 사용한다.
		## 즉, 리소스(데이터, 정보 등)를 가져오는데 사용한다.
		## 특징으로 사용자 입력 데이터가 URL에 노출된다.
		### HTTP GET 요청 : 데이터를 가져오는데 사용하는 것으로 요청한 데이터는 URL에 포함되어 전송
		
		
		## POST는 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 요청일 때 사용한다.
		## 데이터는 HTTP Body에 담겨 보내지기에 노출되지 않으며 POST는 DB에 직접적인 변화를 준다.
		## 예를 들어 로그인&회원가입(사용자가 웹 폼을 통해 데이터를 제출), 게시글&댓글 작성(서버에 변경사항을 전송)
		
		
		## POST는 매니저의 한 종류이다. DB를 관리하는 느낌이라
		## POST는 나중에 form을 사용해서 함수 시작 시 메서드가 POST인지, GET인지 구분하는 if문을 사용한다.
		## 그냥 사용하면 403 Forbidden 오류가 뜬다. -> CSRF 토큰이 없기 때문이다.
		
		## HTTP response status code : 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것
		## 400번대는 클라이언트 잘못, 500번대는 서버 잘못으로 에러가 발생한 것이다.
		## 403 Forbidden : 서버에 요청은 전달됐지만, '권한' 때문에 거절됐다는 뜻
		
		## CSRF는 사이트 간 요청 위조이다. 
		## 사용자가 본인 의지와 무관하게 웹 페이지를 공격하게 만드는 공격 방법 등이다.
		## 이를 방지하기 위해 CSRF 토큰을 form, post를 사용할 때는 항상 넣어줘야 한다.
		## CSRF 토큰은 해당 웹페이지가 Django가 만든 웹페이지가 맞는지 확인하는 것이다.
		
		# 사용자가 입력한 데이터가 어디에 들어있다. -> 어디 = request 객체
		# request.GET은 request 객체 안에 GET이라는 속성 값에 Query Dict라는
		# 독특한 타입이 딕셔너리 형태로 들어있다.
		
		# Query는 무엇일까?
		## DB로부터 정보를 검색하게나 필터링하기 위해 사용되는 요청 및 명령
		## 보통 특정 조건을 만족하는 레코드를 검색하는데 사용
		## 레코드 : DB에서 행
		
		# Query Set은 무엇일까?
		## 장고에서 DB로부터 정보를 가져오는데 사용되는 객체
		## Query의 결과로 반환되는 것이다.
		
		# Query Dict은 뭐지??
		## HTTP GET 요청의 쿼리 문자열(Query String)을 파싱하여 파라미터 이름과 값을 저장하는 딕셔너리 형태의 객체
		### 파싱 : 주어진 문장 또는 데이터 구문을 해석하는 과정
		### 쿼리 문자열 : URL에서 물음표(?) 이후 오는 데이터를 의미
		### -> 보통 웹페이지에서 GET 요청을 보낼 때 사용, 클라이언트가 서버로 데이터를 전달하는데 사용
		### -> key=value 형식으로 데이터 전달, 여러개 파라미터는 &로 구분

		
		
		# GET만 사용해서 데이터를 생성하는 코드 만들어보기
		# 함수 코드 작성방법 3가지 및 이해하기
		def create(request):
		
				### 공통 사항 ###
				title = request.GET.get('title')
				# title이라는 변수에 할당한다. 무엇을?
				## request라는 객체 안에 있는 GET이라는 속성에 Key 값이 title인 value를 할당한다.
				
				content = request.GET.get('content')
				# content라는 변수에 할당한다. 무엇을?
				## request라는 객체 안에 있는 GET이라는 속성에 Key 값이 content인 value를 할당한다.  
		
				#################################################
		
				### 1번 방법 ###
				article = Article()
				# 이걸 인스턴스라고 한다.
				# article은 인스턴스인데, 아무런 값도 없는 인스턴스이다.
				# 인스턴스에 값을 넣어주면 그냥 값을 가진 인스턴스이고,
				# save() 메서드를 써서 저장(INSERT)까지 하면 레코드가 된다.
				
				article.title = title
				# article 레코드 title 속성에 위에서 변수 title에 할당했던 값을 다시 할당해준다.
				
				article.content = content
				# article 레코드 content 속성에 위에서 변수 content에 할당했던 값을 다시 할당해준다.
				
				article.save()
				# 빈 레코드 속성에 모든 값을 다 할당한 다음에 저장해준다.
				
				#################################################
				
				### 2번 방법 ### 
				article = Article(title=title, content=content)
				# 1번 방법에서 save 메서드 사용하는 부분을 제외한 모든 과정을 한 줄의 코드로 합친 것
				
				article.save()
				# 그리고 나서 레코드를 저장한다.
				
			  ## 2번 방법을 사용하는 것을 강력 추천하심 왜냐?
			  ## 1번은 너무 번거롭고, 3번은 코드 한줄에 SQL의 INSERT 구문까지 한 번에 하는 것이라 바로 저장된다.
			  ## 따라서, 할당한 뒤 저장하기 전에 '유효성 검사' 등을 할 타이밍이 없다.
			  ## 2번 방법은 save 메서드를 사용하기 전에 할당만 한 뒤 유효성 검사 등을 할 수 있기 때문이다.
				
				#################################################
				
				### 3번 방법 ###
				Article.objects.create(title=title, content=content)
				# 2번 방법에서 save 구문까지 할당과 동시에 한 번에 이뤄지게 하는 코드
				# objectes는 모델 클래스에 대한 '쿼리 매니저'(QuerySet Manager)다.
				# -> 쿼리 매니저를 사용하면 해당 모델에 대한 DB 쿼리를 실행할 수 있다.
				
				# Article.objects.create()는 Article 모델에 대한 쿼리 매니저 objects를 사용해서 
				# 새로운 레코드를 생성하는 메서드이다. (생성 후 바로 DB에 저장한다.)
				
				# title=title에서 구분하기
				## 앞에 있는 title은 DB의 필드이고 (즉, 필드이름이 title인 필드)
				## 뒤에 있는 타이틀이 title = request.GET.get('title') << 이거에 해당하는 값 title이다.
				## -> 즉, title 필드에 저장할 값
				
				#################################################
				
				### 렌더링 하기 ###
				return render(request, 'articles/create.html')
				# 해당 템플릿을 렌더링하여 응답한다.
				## 렌더링은 무엇?
				## 웹 개발에서 서버 측에서 클라이언트로 보내는 HTML, CSS, JavaScript 및 기타 웹 콘텐츠를 생성하는 과정
				## 즉, 서버가 데이터와 템플릿을 결합하여 최종 HTML 문서를 생성하는 과정

```


```python
# 1번 방법 코드
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

	article = Article()		
	article.title = title
	article.content = content	
	article.save()

    return render(request, 'articles/create.html')

# 2번 방법 코드
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/create.html')

# 3번 방법 코드
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

