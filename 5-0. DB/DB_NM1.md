**Many to many relationships (N:M or M:N)**     
한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우   
-> 양쪽 모두에서 N:1 관계를 가짐

**중개모델**    
Django에서는 'ManyToManyField'로 중개모델 자동 생성    

예시: 한 환자가 여러 의사에게 진찰을 받으려 할 때 외래키에 여러 의사를 넣을 수 없다.   
따라서 중개모델인 예약 테이블을 만들어 거기서 관리하는 것

**ManyToManyField( )**   
M:N 관계 설정 모델 필드   

**'through' argument**   
중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용


**M:N 관계 주의사항**     
M:N 관계로 맺어진 두 테이블에는 물리적 변화 없음  

ManyToManyField는 중개 테이블을 자동 생성    

ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음   
(단, 필드 작성 위치에 따라 참조와 역참조 방향 주의)  

N:1은 완전종속관계이지만, M:N은 종속관계가 아님    
(예시: 의사에게 진찰받는 환자, 환자를 진찰하는 의사처럼 2가지 형태 모두 표현 가능)

**ManyToManyField(to, \*\*options)**     
M:N 관계 설정 시 사용하는 모델 필드

**ManyToManyField 대표 인자 3가지**    
related_name, symmetrical, through


**related_name**    
역참조시 사용하는 manager name을 변경


**symmetrical**     
관계 설정 시 대칭 유무 설정   
ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용   
기본값 : True

1. True일 경우    
source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도   
source 모델 인스턴스를 자동으로 참조하도록 함 (대칭)    
-> 예시: 내가 당신의 친구라면, 자동으로 당신도 내 친구가 됨    

1. False일 경우   
True와 반대 (대칭되지 않음)


**through**    
사용하고자 하는 중개모델을 지정   
일반적으로 추가 데이터를 M:N 관계와 연결하려는 경우에 활용


**M:N에서의 대표 methods**    
add( ) : 지정된 객체를 관련 객체 집합에 추가 (이미 존재하는 관계에 사용하면 관계가 복제되지 않음)

remove( ) : 관련 객체 집합에서 지정된 모델 객체를 제거

**Article(M) - User(N)**    
0개 이상의 게시글은 0명 이상의 회원과 관련   
-> 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있다.   
-> 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.






