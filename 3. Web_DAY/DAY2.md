# **웹_2일차** (3/7)
 
---

## **목차**
1. CSS Box Model
-구성 요소  
-박스 타입  
-기타 display 속성
2. CSS Position
3. CSS Flexbox
-구성 요소  
-레이아웃 구성  
-flex-wrap 응용  
-정리

---

## **1. CSS Box Model**
> 모든 HTML 요소를 사각형 박스로 표현하는 개념

### **1-.1 구성 요소**

#### **구성 요소 종류**
> 내용 (content)  
> 안쪽 여백 (padding)  
> 테두리 (border)  
> 외부 간격 (margin)  

![CSS Box Model](./imgs/CSS_Box_Model.png)

![CSS Box Model](./imgs/CSS_Box_Model2.png)

---

#### **width & height 속성**
> 요소의 너비(width)와 높이(height)를 지정  
> 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함  
> CSS는 border가 아닌 content의 크기를 width 값으로 지정

![width & height](./imgs/width_height.png)

#### **box-sizing 속성**

**content 기준으로 설정**  
```
* {
    box-sizing: content-box;
}
```

**진짜 박스 기준으로 설정**
```
* {
    box-sizing: border-box;
}
```

---

### **1-2. 박스 타입**
> 종류 : Block & Inline
```
.index {
    display: block;
}

.index {
    display: inline;
}
```

#### **Normal flow**
> CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향

> 텍스트, 이미지 구분 없이 좌측 상단에서 시작

![Normal flow](./imgs/Normal_flow.png)




#### **block 타입 특징**
> 항상 새로운 행으로 나뉨  

> width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음  

> 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용가능한 공간을 모두 차지함  
(너비를 사용가능한 공간의 100%로 채우는 것)  

> 대표적인 block 타입 태그 : h1~6, p, div

#### **inline 타입 특징**  
> 새로운 행으로 나뉘지 않음 

> width와 height 속성을 사용할 수 없음  

> 수직 방향 : padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수 없음  

> 수평 방향 : padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음  

> 대표적인 inline 타입 태그 : a, img, span


---

### **1-3. 기타 display 속성**

#### **inline-block**
> inline과 block 요소 사이의 중간 지점을 제공하는 display 값  

> block 요소의 특징을 가짐  
(width 및 height 속성 사용 가능)  
(padding, margin, border로 인해 다른 요소가 밀려남)  

> 요소가 줄바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

#### **none**
> 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음  

---

### **1-4. [참고]**

#### **shortand 속성 - border**
> border-width, boreder-stlye, border-color를 한번에 설정하기 위한 속성

> border: 2px solid black;

#### **shortand 속성 - margin & padding**
> 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성

> margin: 10px 20px 30px 40px  
4개 : 상하좌우  
3개 : 상 / 좌우/ 하  
2개 : 상하 / 좌우  
1개 : 4방향 공통

#### **Margin collapsing (마진 상쇄)**
> 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상  

> 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함  

> 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정하기 위함

---


## **2. CSS Position**

### **CSS Layout**
> 각 요소의 **위치와 크기를 조정**하여 웹 페이지의 디자인을 결정하는 것  
(Display, Position, Float, Flexbox)


### **CSS Position**
> 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것  
(다른 요소 위에 올리기, 화면 특정 위치에 고정시키기 등)

#### **Position 유형**
> static, relative, absolute, fixed, sticky

> static : 기본값, 요소를 Normal Flow에 따라 배치  
> relative : 












