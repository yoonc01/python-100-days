# Day 2
팁 계산기

# Demo 사이트
https://appbrewery.github.io/python-day2-demo/

# Description
전체 금액과 몇 퍼센트로 tip을 줄 것인지, 그리고 몇 명이서 나누어서 내는지에 따라 각 인원이 내야 하는 금액 계산
(조건문을 아직 배우지 않았으므로 입력은 정상 값들만 들어온다고 가정하고 작성)

# 배운 내용 정리
## data type
- type 함수를 사용하여 데이터 타입을 확인할 수 있다.
### int
- 정수가 몇 자리 숫자인지 구하는 방법은 len() 함수를 이용해서 구할 수 없다.
- 큰 정수를 표현할 때 1,234,567은 , 대신 _를 사용하여 1_234_567라고 나타낼 수 있다.
- int 함수를 이용하여 정수형으로 바꿀 수 있다. 하지만 모든 것을 변환할 수 있는 것은 아니다.

### str
- 문자열은 문자들이 연결된 것이다. 그렇기에 인덱싱을 이용하여 각 문자를 추출할 수 있다. 
- 인덱싱은 0부터 시작한다. 하지만 음수로 지정할 수 있으며 `-1`(마지막 문자)은 마지막 문자를 의미한다.

### float
- 실수를 이야기한다.

### bool
- 참, 거짓 다시 말해 `True`와 `False`를 의미한다.

## Math
- `+` 더하기
- `-` 빼기
- `*` 곱하기
- `/` 나누기(부동 소수점(`float`))으로 나옴
- `//` 몫 구하기(정수(`int`))로 나옴
- `%` 나머지 구하기(실수로도 나누어서 나머지 구할 수 있음)
- `**` 거듭제곱(`a**b`는 a를 b번 곱한다는 의미)

### 우선 순위
#### 1. ()
#### 2. **
#### 3. * or / or // or %
#### 4. + or -

### 근사하기
- int 함수를 이용하면 소수점 이하를 버림할 수 있음
- round 함수를 이용하면 반올림 가능함(두 번째 인자를 전달하여 소수 몇번째 자리까지 반올림할 것인지 설정 가능)

### f-string
- f"This is {variable}"의 꼴로 variable 값을 문자열에 넣을 수 있다.