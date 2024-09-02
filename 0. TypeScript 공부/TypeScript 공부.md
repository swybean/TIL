# TypeScript (타입스크립트)

### 타입스크립트란?

동적 타이핑(Dynamic typing)을 지원하는 자바스크립트를 사용하는 개발환경에서 타입(type)과 관련된 버그를 예방하기 위한 언어이다.

**※ Dynamic typing**  
시작과 동시에 런타임 시작 단계에서 변수 유형 검사를 수행하며, 런타임 시작 단계에서 타입을 구분 짓고 사용하는 특징을 가진 것

-> 자바스크립트는 동적 타이핑을 지원하기 때문에 `3 * '5'`와 같은 연산도 런타임 시작 단계에서 `'5'`를 `number`로 구분 짓고 `3 * 5`로 알아서 연산하기 때문에 종종 원치않는 오류가 발생한다.

-> 이러한 문제를 극복하기 위해 등장한 것이 타입스크립트(TypeScript)

-> 타입에 대한 에러를 미리 예방하기 위해 사용하는 것!

---

### 타입스크립트 타입 종류

일반적인 형태 : `let 변수명 : 타입명 = 값`

**타입스크립트의 원시 타입**  
`string`, `number`, `boolean`, `symbol`, `null`, `undefined`, `object`

**다른 중요한 타입스크립트 타입**  
`unknown` : 최상위 타입  
`never` : 하위 타입  
`객체 리터럴` : { property: Type }  
`void` : 리턴 타입으로 사용하기 위해 의도된 undefined의 서브타입  
`T[]` : 수정가능한 배열들 ( Array\<T>로 사용가능)  
`[T, T]` : 고정된 길이지만 수정 가능한 튜플  
`(t: T) => u` : 함수

---

### 타입스크립트 기본 타입

**Boolean (불리언)** : 참/거짓(true/false) 값

```typescript
let isDone: boolean = false;
```

---

**Number (숫자)** : 부동 소수 값

```typescript
let decimal: number = 6;
let hex: nember = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```

---

**String (문자열)** : 텍스트 데이터 타입

```typescript
let color: string = "blue";
color = "red";

// 템플릿 문자열을 사용하면 여러 줄에 걸쳐 문자열을 작성 가능 및 표현식을 포함 가능
let fullName: string = `Bob Bobbington`;

let age: number = 37;

let sentence: string = `Hello, my name is ${fullName}. I'll be ${
  age + 1
} years old next month.`;

// 위는 아래 sentence 선언과 동일
let sentence: string =
  "Hello, my name is " +
  fullName +
  ".\n\n" +
  "I'll be " +
  (age + 1) +
  " years old next month.";
```

---

**Array (배열)**

```typescript
// 배열 요소들을 나타내는 타입 뒤에 []를 쓰는 방법
let list: number[] = [1, 2, 3];

// 제네릭 배열 타입을 사용하는 방법
let list: Array<number> = [1, 2, 3];
```

---

**Tuple (튜플)**  
요소의 타입과 개수가 고정된 배열을 표현 가능  
단, 요소들의 타입이 모두 같을 필요는 없음.

```typescript
// 튜플 타입으로 선언
let x: [string, nunber];

// 초기화
x = ["hello", 10]; // 성공
x = [10, "hello"]; // 실패

// 정해진 인덱스에 위치한 요소에 접근하면 해당 타입이 나타남
// 성공
console.log(x[0].substring(1));
// 오류, 'number'에는 'substring'이 없습니다.
console.log(x[1].substring(1));

// 정해진 인덱스 외 다른 인덱스에 있는 요소에 접근하면, 오류가 발생하며 실패

// 오류 '[string, number]' 타입에는 프로퍼티 '3'이 없습니다.
x[3] = "world";

// '[string, number]' 타입에는 프로퍼티 '5'가 없습니다.
console.log(x[5].tostring());
```

---

**Enum (열거)**  
집합에 더 나은 이름을 붙여줄 수 있음

```typescript
enum Color {
  Red,
  Green,
  Blue,
}
let c: Color = Color.Green;
```

기본적으로 enum은 0부터 시작해서 멤버들의 번호를 매김  
멤버 중 하나의 값을 수동으로 설정하여 번호 변경 가능

```typescript
// 0 대신 1부터 시작해 번호를 매기도록 변경
enum Color {
  Red = 1,
  Green,
  Blue,
}
let c: Color = Color.Green;
```

```typescript
// 모든 값을 수동으로 설정
enum Color {
  Red = 1,
  Green = 2,
  Blue = 4,
}
let c: Color = Color.Green;
```

enum의 유용한 기능 : 매겨진 값을 사용해 enum 멤버의 이름을 알아낼 수 있음

```typescript
enum Color {
  Red = 1,
  Green,
  Blue,
}
let colorName: string = Color[2];

console.log(colorName); // Green
```

---

**Any**  
알지 못하는 타입을 표현해야 할 때, 타입 검사를 하지 않고 그 값들이 컴파일 시간에 검사를 통과하길 원할 때 사용

```typescript
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // 성공, 분명한 Boolean입니다.
```

any 타입은 컴파일 중 점진적으로 타입검사를 하거나 하지 않을 수 있음

Object가 비슷한 역할을 할 수 있다고 생각할 수 있지만!  
-> Object로 선언된 변수들은 오직 어떤 값이든 그 변수에 할당할 수 있게 해주지만 실제로 메서드가 존재하더라도, 임의로 호출할 수 없음

```typescript
let notSure: any = 4;
// 성공, isItExists는 런타임에 존재할 것입니다.
notSure.ifItEcists();
// 성공, toFixed는 존재합니다. (컴파일검사는 하지 않음)
notSure.toFixed();

let prettySure: object = 4;
// 오류 : 프로퍼티 'toFixed'는 'Object'에 존재하지 않습니다.
prettySure.toFixed();
```

any 타입은 타입의 일부만 알고 전체를 알지 못할 때 유용함  
-> 예시 : 여러 다른 타입이 섞인 배열을 다룰 수 있음

```typescript
let list: any[] = [1, true, "free"];
list[1] = 100;
```

---

**Void**  
어떤 타입도 존재할 수 없음을 나타냄 (any의 반대 타입)  
보통 함수에서 반환값이 없을 때 반환 타입을 표현하기 위해 사용

```typescript
function warnUser(): void {
  console.log("This is my warning message");
}
```

void를 타입 변수로 선언하는 것은 유용하지 않다.  
-> 변수에는 null, undefined만 할당할 수 있음

```typescript
let unusable: void = undefined;
unusable = null; // 성공, '--strictNullChecks'를 사용하지 않을 때만
```

---

**Null and Undefined**  
null과 undefined는 다른 모든 타입의 하위 타입  
-> null과 undefined를 number 같은 타입에 할당할 수 있다는 것을 의미

하지만!  
--strictNullChecks를 사용하면, null과 undefined는 오직 any와 각자 자신들 타입에만 할당 가능  
(예외 : undefined는 void에 할당 가능)

---

**Never**  
절대 발생할 수 없는 타입을 나타냄  
모든 타입에 할당 가능한 하위 타입  
다만, 다른 어떤 타입도 never에 할당할 수 없음

```typescript
//never를 반환하는 함수는 함수의 마지막에 도달할 수 없다.
function error(message: string): never {
  throw new Error(message);
}

// 반환 타입이 never로 추론된다.
function fail() {
  return error("Something failed");
}

// never를 반환하는 함수는 함수의 마지막에 도달할 수 없다.
function infiniteLoop(): never {
  while (true) {}
}
```

---

**Object (객체)**  
원시 타입이 아닌 타입을 나타냄  
number, string, boolean, bigint, symbol, bull, undefined가 아닌 나머지를 의미

```typescript
declare function create(o: object | null): void;

create({ prop: 0 }); // 성공
create(null); // 성공

create(42); // 오류
create("string"); // 오류
create(false); // 오류
create(undefined); // 오류
```

---

**타입 단언 (Type assertions)**
