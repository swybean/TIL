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
`let isDone: boolean = false`

---

**Number (숫자)** : 부동 소수 값  
`let decimal: number = 6;`  
`let hex: nember = 0xF00d;`  
`let binary: number = 0b1010;`  
`let octal: number = 0o744;`

---

**String (문자열)** : 텍스트 데이터 타입  
`let color: string = "blue";`  
`color = 'red';`

템플릿 문자열을 사용하면 여러 줄에 걸쳐 문자열을 작성 가능 및 표현식을 포함 가능  
`` let fullName: string = `Bob Bobbington`;``

`let age: number = 37;`

`` let sentence: string = `Hello, my name is ${ fullName }. I'll be ${ age + 1 } years old next month.`; ``

-> 위는 아래 sentence 선언과 동일  
`let sentence: string = "Hello, my name is " + fullName + ".\n\n" + "I'll be " + (age + 1) + " years old next month.";`

---

**Array (배열)**

```typescript
배열 요소들을 나타내는 타입 뒤에 []를 쓰는 방법  let list: number[] = [1, 2, 3]

제네릭 배열 타입을 사용하는 방법
let list: Array<number> = [1, 2, 3]
```

---

**Tuple (튜플)**  
요소의 타입과 개수가 고정된 배열을 표현 가능  
단, 요소들의 타입이 모두 같을 필요는 없음.

```typescript
// 튜플 타입으로 선언
let x: [string, nunber];
```

---

```typescript

```
