# 21강 COUNT 이외의 집계함수

### #1 SUM으로 합계구하기

집계함수의 종류중 SUM이 있습니다. SUM 집계함수를 사용해 집합의 합계를 구할 수 있습니다.

```sql
select sum(quantity) from sample51
```

SUM 집계함수에 지정되는 집합은 수치형 뿐입니다.

문자열형이나 날짜 시간형의 집합에서는 합계를 구 할 수 없습니다.

name열은 문자열형으므로 SUM(name)과 같이 지정할 수는 없습니다.

SUM집계함수도 COUNT와 마찬가지로 NULL값을 무시합니다. NULL값을 제거한 후 합계를 내게 됩니다.

### #2 AVG로 평균내기

합한 값을 개수로 나누면 평균값을 구할 수 있습니다. 집계함수가 반환한 값을 통해 평균값을 간단하게 구할 수 있습니다.

```sql
SUM(quantity) / COUNT(quantity) 
```

AVG 집계함수에 주어지는 집합은 SUM과 동일하게 수치형만 가능합니다.

- AVG로 평균구하기

```sql
select AVG(quantity),
SUM(quantity) / COUNT(quantity) 
from sample51
```

AVG 집계함수도 NULL값은 무시합니다. 즉, NULL값을 제거한 뒤에 평균값을 계산합니다. 만약 NULL을 0으로 간주해서 평균을 내보고싶다면 CASE를 사용해 NULL을 0으로 변환한 뒤에 AVG함수로 계산하면 됩니다.

- AVG로 평균값 계산(NULL을 0으로 변환)

```sql
select AVG(
CASE WHEN
quantity IS NULL 
THEN 0 
ELSE quantity
END)
AS avgnull0 
FROM sample51;
```

### #3 MIN MAX로 최솟값 최댓값 구하기

MIN집계함수, MAX 집계함수를 사용해 집합에서 최솟값과 최댓값을 구할 수 있습니다.

SUM 함수와 다르게 문자열형과 날짜시간형에도 사용할 수 있습니다.

NULL값을 무시하게 되는 특징이 있습니다.

- MIN MAX로 최솟값, 최댓값 구하기

```sql
select MIN(quantity),
MAX(quantity),
MIN(name),
MAX(name)
from sample1;

result: 1 10 A C
```

문자열형에서 MAX는 A~C중 C를 나타냅니다. 그리고 MIN은 A를 나타내게 됩니다.

