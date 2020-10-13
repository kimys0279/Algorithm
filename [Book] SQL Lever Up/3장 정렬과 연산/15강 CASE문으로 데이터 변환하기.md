# 1. CASE문

> 임의의 조건에 따라서 독자적으로 변환 처리를 지정해서 데이터를 변환하고 싶을 때 CASE문을 사용할 수 있다. 
```mysql
CASE WHEN 조건식1 THEN 식1   
  [WHEN 조건식2 THEN 식2...]   
  [ELSE 식3]   
END  
```

예를 들어, **NULL값을 0으로 간주해서 계산하고 싶을 때는 어떻게 해야 할까?**   
NULL값으로 연산한 결과는 모두 NULL이 되는데?   
이 경우에 **CASE문**을 이용해서 처리할 수 있다.   

RDBMS에서는 사용자가 함수를 작성할 수 있다.
간단한 처리의 경우에는 사용자 정의 함수를 작성하지 않고 CASE문으로 처리할 수 있다.

``WHEN절``: 참과 거짓을 반환하는 조건식을 적어준다.
해당 조건을 만족해서 참이 되는 경우, THEN절에 있는 식이 처리된다.
이때 WHEN과 THEN을 한데 조합해 지정할 수 있다.
WHEN절의 조건식을 차례로 평가해 나가게 되는데,
가장 먼저 조건을 만족한 WHEN절과 대응하는 THEN절 식의 결과를 CASE문의 결과값으로 반환한다.

만약, 그 어떤 조건식도 만족하지 못할 경우에는 ELSE절의 식이 CASE문의 결과값으로 반환된다.
``ELSE절``은 생략 가능하고 생략했을 경우에는 기본값으로 **ELSE NULL**로 처리된다.

### 1) CASE문을 이용하여 NULL값을 0으로 변환하기   

```mysql 
SELECT column, CASE WHEN column IS NULL THEN 0 ELSE column END "column(null=0)" 
FROM table;   
```

column값이 NULL일 때 WHEN column IS NULL은 참이 되므로
CASE문은 THEN절의 ‘0’을 반환한다.
NULL이 아닌 경우에는 ELSE절의 ‘column’, 즉 column의 값을 반환한다.

### 2) COALESCE
**NULL값을 변환하는 경우에는 COALESCE 함수를 사용하는 편이 더 쉬울 수 있다**.
위의 CASE문을 이용해 NULL값을 0으로 변환하는 예제를 COALESCE 함수를 이용하면
아래와 같이 바꿀 수 있다.   

SELECT column, COALESCE(column, 0) FROM table;      

COALESCE 함수는 여러 개의 인수를 지정할 수 있다.
주어진 인수 가운데 NULL이 아닌 값에 대해서는 가장 먼저 지정된 인수의 값을 반환한다.
앞의 예문은 column이 NULL이 아니면 column값을 그대로 출력하고,
그렇지 않으면(column이 NULL이면) 0을 출력한다.

# 2. 또 하나의 CASE문   

숫자로 이루어진 코드를 알아보기 더 쉽게 문자열로 변환하고 싶은 경우
CASE문을 많이 사용한다.
수치 데이터를 문자화하는 것을 디코드라고 부르고,
반대로 문자를 수치화하는 것을 인코드라고 부른다.

단순 CASE문으로 예를 들자면,
성별 코드를 변환해보면,

## 1)단순 CASE로 성별 코드를 남자, 여자로 변환하기   
my sql> SELECT column명 AS "코드",   
CASE column명   
  WHEN 1 THEN '남자'   
  WHEN 2 THEN '여자'   
  ELSE '미지정'   
END AS "성별" FROM table명;   

단순 CASE문에서 CASE 뒤에는 대상을 적고 WHEN 뒤에는 값을 적는다.

# 3. CASE를 사용할 경우 주의사항

## 1) ELSE 생략
CASE문에서 ELSE는 생략할 경우, ELSE NULL이 되는 것에 주의하자.
대응되는 WHEN이 하나도 없는 경우 ELSE절이 사용된다.
이때, ELSE를 생략한 경우 NULL이 반환되게 된다.
따라서 ELSE를 생략하지 지정하는 편이 낫다.

CASE문의 ELSE는 생략하지 않는 편이 낫다!

## 2) WHEN에 NULL 지정하기
여기에서 데이터가 NULL인 경우를 고려해서 WHEN NULL THEN ‘데이터 없음’과 같이 지정해도
문법적으로는 문제가 없지만 정상적으로 처리되지 않는다.
예를 들어, CASE문에서 WHEN절에 NULL을 지정해보자.

### 단순 CASE문에서 WHEN절에 NULL 지정하기   

```mysql
CASE a   
  WHEN 1 THEN '남자'   
  WHEN 2 THEN '여자'   
  WHEN NULL THEN '데이터 없음'   
  ELSE '미지정'   
END   
```

이 예제에서 조건식이 처리되는 순서는 아래와 같다.

a = 1   
a = 2   
a = NULL   

그런데 문제는 비교 연산자 =로는 NULL값과 같은지 아니지를 비교할 수 없다는 것이다.
따라서 a열의 값이 NULL이라고 해도 a = NULL은 참이 되지 않는다.
즉, ‘데이터 없음’ 대신 ELSE절에 있는 ‘미지정’이라는 결과값이 나온다.
이때 NULL값인지 아닌지를 판정하기 위해서는 IS NULL을 사용한다.
다만, 단순 CASE문은 특성상 =연산자로 비교하는 만큼, NULL값인지를 판정하기 위해서는
검색 CASE문을 사용해야 한다.   

### 검색 CASE문으로 NULL 지정하기   

```mysql
CASE   
  WHEN a = 1 THEN '남자'   
  WHEN a = 2 THEN '여자'   
  WHEN a IS NULL THEN '데이터 없음'   
  ELSE '미지정'   
END
```

단순 CASE문으로는 NULL값을 비교할 수 없다!

3) DECODE NVL   

Oracle에는 디코드를 수행하는 DECODE함수가 내장되어 있어서
CASE문과 같은 용도로 사용할 수 있다.
단, DECODE 함수는 Oracle에서만 지원하는 함수인 만큼 다른 데이터베이스 제품에서는 사용할 수 없다.
NULL값을 변환하는 함수도 있는데, Oracle에서는 NVL 함수, SQL Server에서는 ISNULL 함수가 이에 해당한다.
다만, 이 함수들은 특정 데이터베이스에 국한된 함수이기 때문에
NULL값을 변환할 때는 표준 SQL로 지정되어 있는 COALESCE함수를 사용한다.
