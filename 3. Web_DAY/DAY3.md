# **웹_3일차** (3/8)
 


## **목차**
**1. Bootstrap**  
-Reset CSS  
**2. BOotstrap 활용**  
-Typography  
-Colors  
-Component  
**3. Semantic Web**  
-Semantic in HTML  
-Semantic in CSS  

---

## **1. Bootstrap**
> CSS 프론트엔드 프레임워크 (Toolkit)  
> 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함  

> 기본 사용법 : \<p class="mt-5">Hello, world!\</p>  
> m : property    
> t : sides  
> 5 : size  

|Property||
|:------:|:---:|
|m|margin|
|p|padding|


|Sides||
|:------:|:---:|
|t|top|
|b|bottom|
|s|left|
|e|right|
|y|top, bottom|
|x|left, right|
|blank|4 sides|


|Size|||
|:------:|:---:|:---:|
|0|0 rem|0px|
|1|0.25 rem|4px|
|2|0.5 rem|8px|
|3|1 rem|16px|
|4|1.5 rem|2px4|
|5|3 rem|48px|
|auto|auto|auto|


[Bootstrap 공식 문서](https://getbootstrap.com/)

---

### **1-1. CDN**
> Content Delivery Network  
> 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

> 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화  
(웹 페이지 로드 속도를 높임)  

> 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

---

### **1-2. Reset CSS**
> 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트  
> (HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계)

#### **Reset CSS 사용배경**
> 모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음 
> User agent stylesheets : 모든 문서에 기본 스타일을 제공하는 기본 스타일 시트  

> 문제 : 해당 설정이 브라우저마다 상이하다.  
> 모든 브라우저에서 웹사이트가 동일하게 보이게 만들어야 하는 개발자에게 골치 아픈 일  
> 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자!  

#### **Normalize CSS**
> Reset CSS 방법 중 대표적인 방법  
> 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법  

> bootstrap은 bootstrap-reboot.css 라는 파일명으로 normalize.css를 자체적으로 커스텀해서 사용하고 있음

---



## **2. Bootstrap 활용**

### **2-1. Typography**
> 제목, 본문 텍스트, 목록 등

#### **Display headings**
> 기존 Heading보다 더 눈에 띄는 제목이 필요할 경우 (더 크고 약간 다른 스타일)

#### **Inline text elements**
> HTML inline 요소에 대한 스타일  

#### **List**
> HTML list 요소에 대한 스타일 

---

### **2-2. Colors**

#### **Bootstrap Color system**
> Bootstrap이 지정하고 제공하는 색상 시스템  

> Colors : Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

---

### **2-3. Bootstrap Component**
> Bootstrap에서 제공하는 **UI 관련 요소**  
(버튼, 네비게이션 바, 카드, 폼, 드롭다운 등)

> 대표 Component : Alerts, Badges, Buttons, Cards, Navbar

#### **장점**
> 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는데 유용하게 활용


### **[참고] Bootstrap을 사용하는 이유**
> 가장 많이 사용되는 CSS 프레임워크  
> 사전에 디자인된 다양한 컴포넌트 및 기능  
(빠른 개발과 유지보수)  
> 손쉬운 반응형 웹 디자인 구현  
> 커스터마이징(customizing) 용이  
> 크로스 브라우징(Cross browsing) 지원  
(모든 주요 브라우저에서 작동하도록 설계되어 있음) 


---

## **3. Semantic Web**
> 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식  

---

### **3-1. Semantic Web in HTML**

#### **HTML 요소가 의미를 가진다는 것**
> \<h1>Heading\</h1> : "페이지 내 최상위 제목"이라는 의미를 제공하는 요소  
(브라우저의 의해 스타일이 지정됨)


#### **HTML Semantic Element**
> 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소  
(검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록)

> 대표 Semantic Element : header, nav, main, article, section, aside, footer

---

### **3-2. Semantic Web in CSS**

#### **CSS 방법론**
> CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

#### **OOCSS**
> Object Oriented CSS  
> 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론  

#### **OOCSS 기본 원칙**
> **구조와 스킨을 분리**  
> 1. 구조와 스킨을 분리함으로써 재사용 가능성을 높임   
> 2. 모든 버튼의 **공통**구조를 정의 + **각각**의 스킨(배경색, 폰트색)을 정의

> **컨테이너와 콘텐츠를 분리**  
> 1. 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용  
> 2. 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함  
> 3. 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

---

## **[참고]**

#### **책임과 역할**
HTML : 콘텐츠의 구조와 의미  
CSS : 레이아웃과 디자인  

#### **의미론적인 마크업이 필요한 이유**
> **검색엔진 최적화 (SEO)**  
검색엔진이 해당 웹사이트를 분석하기 쉽게 만들어 검색순위에 영향을 줌  

> **웹 접근성 (Web Accessibility)**  
웹사이트, 도구, 기술이 고령자 및 장애를 가진 사용자들이 사용할 수 있도록 설계 및 개발하는 것  
ex) 스크린 리더를 통해 전맹 시각장애 사용자에게 웹 글씨를 읽어줌







