# 5장 집계와 서브쿼리
## 22강 그룹화 -Group BY

```mysql
SELECT * FROM 테이블명 GROUP BY 열1, 열2, ...
```

예제

|no|name|quantity|
|-:|:-|-:|
|1|A|1|
|2|A|2|
|3|B|10|
|4|C|3|
|5|NULL|NULL|

 1. GROUP BY로 그룹화
   ```mysql
   SELECT name FROM sample51 GROUP BY name;
   ```
   
   - 지정된 열과 값이 같은 행들을 하나의 그룹으로 묶는다.
   - DISTINCT처럼 중복이 제거 되는 효과가 있다.
    
    > 집계함수랑 함께 사용하면 그 차이점이 더 크게 다가온다.
    
    
   ```mysql
       SELECT name, COUNT(name), SUM(quantity) 
       FROM sample51 GROUP BY name;
   ```
   |name|count(name)|sum(qunantitiy)|
|-:|:-|-:|
|NULL|0|NULL|
|A|2|3|
|B|1|10|
|C|1|3|

2. HAVING 구로 조건
  - 집계함수는 WHERE 구를 조건식에 사용할 수 없다.
   
   
    ```mysql
       SELECT name, COUNT(name)
       FROM sample51 WHERE COUNT(name) = 1 GROUP BY name;
   ```
   
   
  
   내부처리 순서
   WHERE 구-> GROUP BY 구 ->  HAVING 구 ->SELECT 구 -> ORDER BY 구
   
   
   
   > 집계함수를 사용할 경우 HAVING 구로 검색조건을 지정한다.
   
   
   ```
       SELECT name, COUNT(name)
       FROM sample51 GROUP BY name HAVING COUNT(name) = 1;
   ```
   
 - 별명(as) 사용시 주의할점(사용하지 말자)
    - SELECT 구보다 먼저 실행되기 때문에 별명 사용이 일반적으로 불가능하지만
    - MySQL과 같은 db에서는 실행이 가능하다.
    - 하지만 Oracle과 같은 db는 에러가 발생한다.
    - 결국, 사용하지 않는게 좋다.
     
3. 복수열의 그룹화
  - GRPOUP BY에 지정한 열 이외의 열은 집계함수를 사용하지 않는 채 SELECT 구에 기술해서는 안된다.
  
  즉, 위 예제로 예를들면
   no,quantity열을 SELECT구에 그대로 지정하면 에러가 발생할 수 도 있다.(db에 따라 에러가 발생하지 않을 수 도 있다.)
   사용할거면 GROUP BY에 지정하자.
     
4. 결과값 정렬
  - db내부 처리에서 같은 값을 그룹으로 지정하는 과정에서 순서가 바뀌는 부작용이 발생할 수 있다.
  - db마다 다르지만, 확실한것은 GROUP BY로만으로 정렬을 기대하기는 어렵다.
  - 결국, ORDER BY를 사용해서 정렬을 해야 원하는 결과를 얻을 수 있다.
     
