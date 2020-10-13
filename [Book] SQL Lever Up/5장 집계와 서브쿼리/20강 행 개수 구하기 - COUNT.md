# 20강 행 개수 구하기 - COUNT

### #1 COUNT로 행 개수 구하기

COUNT함수는 인수로 주어진 집합의 `개수` 를 구해 반환합니다.

```sql
select count(*) from sample51;

result: 5
```

`*은`모든 열을 나타낼때사용하는 메타문자, COUNT집계함수에서는 '모든 열 = 테이블 전체' 라는 의미로 사용됩니다. 즉, COUNT는 인수로 지정된 집합(테이블 전체)의 개수 반환합니다. 행의 개수를 구하는것과 동일합니다.

- where 구 지정하기

```sql
select count(*) from sample51 where name = 'A'

result: 2
```

이름이 A인 행의 개수를 구합니다.

- where 구 계산 방법

1. where로 행 검색
2. COUNT로 행의 개수 집계

### #2 집계함수와 NULL값

집계함수는 집합안에 NULL값이 있을 경우 이를 `제외`하고 처리합니다.

- 5개의 테이블에서 no컬럼은 NULL이 없고, name컬럼에는 NULL이 1개 존재한다고 가정합니다.

```sql
select count(no), count(name) from sample51;

result: 5 4
```

단, `COUNT(*)` 경우에는 모든열의 행의 수를 카운트하기 때문에 5 라는 결과를 얻게 됩니다.

### #3 DISTINCT로 중복 제거

집합안에 중복된 값이 있는지 여부를 확인하여 중복을 제거할 경우 사용합니다.

```sql
select distinct name from sample51;
```

DISTINCT는 예약어로 열명이 아닙니다. SELECT 구에서 DISTINCT를 지정하면 중복된 데이터를 제외한 결과를 클라이언트로 반환합니다.

- ALL 키워드

```sql
select all name from sample51;
```

중복 유무와 관계없이 문자 그대로 모든 행을 반환합니다. 즉, SELECT 구에 지정하는 ALL 또는 DISTINCT는 중복된 값을 제거할 것인지 설정하는 스위치와 같은 역할을 합니다.

ALL과 DISTICT 중 어느것도 지정하지 않은 경우에는 중복된 값은 제거되지 않습니다. 즉, 생략할 경우 ALL로 간주됩니다.

### #4 집계함수에서 DISTINCT

- name열에서 NULL값을 제외하고, 중복하지 않는 데이터의 개수를 구하는 경우

```sql
select count(ALL name),
count(DISTINCT name)
from sample51;

result: 4 3
```

집계함수의 인수로 DISTINCT를 지정하여 수식자로 지정후 COUNT의 값을 반환시키게 합니다.

ALL을 생략해도 결국 같은결과를 얻게됩니다.

ALL, DISTINCT는 인수가 아니므로 `,`를 붙이지 않습니다.