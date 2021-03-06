# Optimizer



SQL 최적화 과정

1. SQL 파싱
   - 사용자로부터 SQL 전달
   - SQL 파서가 파싱 진행
2. SQL 최적화
   - 옵티마이저가 최적화 진행
   - 시스템 및 오브젝트 통계정보를 바탕으로 다양한 실행 경로 비교하여 선택
3.  Row-Source 생성
   - 옵티마이저가 선택한 실행경로를 실제 실행 가능한 코드 또는 프로시저 형태로 포맷팅

![sql가이드](http://www.dbguide.net/publishing/img/knowledge/SQL_239.jpg)

옵티마이저(Optimizer)는 사용자가 질의한 SQL문에 대해 최적의 실행 방법을 결정하는 역할을 수행한다. 

이러한 최적의 실행 방법을 실행계획(Execution Plan)이라고 한다. 

**다양한 실행 방법들 중에서 최적의 실행 방법을 결정하는 것이 바로 옵티마이저의 역할**이다. 

옵티마이저가 선택한 **실행 방법의 적절성 여부는 질의의 수행 속도에 가장 큰 영향** 미치게 된다. 최적의 실행 방법 결정이라는 것은 어떤 방법으로 처리하는 것이 최소 일량으로 동일한 일을 처리할 수 있을지 결정하는 것이다. 그러나 이러한 결정을 옵티마이저는 실제로 SQL문을 처리해보지 않은 상태에서 결정해야 하는 어려움이 있다. 

옵티마이저가 최적의 실행 방법을 결정하는 방식에 따라 [그림 Ⅱ-3-1]과 같이 규칙기반 옵티마이저(RBO, Rule Based Optimizer)와 비용기반 옵티마이저(CBO, Cost Based Optimizer)로 구분할 수 있다.

현재 대부분의 관계형 데이터베이스는 비용기반 옵티마이저만을 제공한다. 비록 규칙기반 옵티마이저를 제공하더라도 신규 기능들에 대해서는 더 이상 지원하지 않는다. 다만 하위 버전 호환성을 위해서만 규칙기반 옵티마이저가 남아 있을 뿐이다. 그렇지만 규칙기반 옵티마이저의 규칙은 보편 타당성에 근거한 것들이다. 이러한 규칙을 알고 있는 것은 옵티마이저의 최적화 작업을 이해하는데 도움이 된다.

<br/>

##### 가. 규칙기반 옵티마이저

**규칙기반 옵티마이저는 규칙(우선 순위)을 가지고 실행계획을 생성**한다. 

실행계획을 생성하는 규칙을 이해하면 누구나 실행계획을 비교적 쉽게 예측할 수 있다. 규칙기반 옵티마이저가 실행계획을 생성할 때 참조하는 정보에는 SQL문을 실행하기 위해서 이용 가능한 인덱스 유무와 (유일, 비유일, 단일, 복합 인덱스)종류, SQL문에서 사용하는 연산자(=, <, <>, LIKE, BETWEEN 등)의 종류 그리고 SQL문에서 참조하는 객체(힙 테이블, 클러스터 테이블 등)의 종류 등이 있다. 

이러한 정보에 따라 우선 순위(규칙)가 정해져 있고, 이 우선 순위를 기반으로 실행계획을 생성한다. 결과적으로 규칙기반 옵티마이저는 우선 순위가 높은 규칙이 적은 일량으로 해당 작업을 수행하는 방법이라고 판단하는 것이다. 



[그림 Ⅱ-3-2]는 Oracle의 규칙기반 옵티마이저의 15가지 규칙이다. 순위의 숫자가 낮을수록 높은 우선 순위이다.

![sql가이드](http://www.dbguide.net/publishing/img/knowledge/SQL_240.jpg)

> 규칙기반 옵티마이저의 우선 순위 규칙 중에서 주요한 규칙에 대해서만 간략히 설명한다.
>
> 규칙 1. Single row by rowid 
>
> - ROWID를 통해서 테이블에서 하나의 행을 액세스하는 방식이다. ROWID는 행이 포함된 데이터 파일, 블록 등의 정보를 가지고 있기 때문에 다른 정보를 참조하지 않고도 바로 원하는 행을 액세스할 수 있다. 하나의 행을 액세스하는 가장 빠른 방법이다. 
>
> 규칙 4. Single row by unique or primary key 
>
> - 유일 인덱스(Unique Index)를 통해서 하나의 행을 액세스하는 방식이다. 이 방식은 인덱스를 먼저 액세스하고 인덱스에 존재하는 ROWID를 추출하여 테이블의 행을 액세스한다.  
>
> 규칙 8. Composite index 
>
> - 복합 인덱스에 동등(‘=’ 연산자) 조건으로 검색하는 경우이다. 예를 들어, 만약 A+B 칼럼으로 복합 인덱스가 생성되어 있고, 조건절에서 WHERE A=10 AND B=1 형태로 검색하는 방식이다. 복합 인덱스 사이의 우선 순위 규칙은 다음과 같다. 인덱스 구성 칼럼의 개수가 더 많고 해당 인덱스의 모든 구성 칼럼에 대해 ‘=’로 값이 주어질 수록 우선순위가 더 높다. 
> - 예를 들어, A+B로 구성된 인덱스와 A+B+C로 구성된 인덱스가 각각 존재하고 조건절에서 A, B, C 칼럼 모두에 대해 ‘=’로 값이 주어진다면 A+B+C 인덱스가 우선 순위가 높다. 만약 조건절에서 A, B 칼럼에만 ‘=’로 값이 주어진다면 A+B는 인덱스의 모든 구성 칼럼에 대해 값이 주어지고 A+B+C 인덱스 입장에서는 인덱스의 일부 칼럼에 대해서만 값이 주어졌기 때문에 A+B 인덱스가 우선 순위가 높게 된다. 
>
> 규칙 9. Single column index
>
> - 단일 칼럼 인덱스에 ‘=’ 조건으로 검색하는 경우이다. 만약 A 칼럼에 단일 칼럼 인덱스가 생성되어 있고, 조건절에서 A=10 형태로 검색하는 방식이다.
>
> 규칙 10. Bounded range search on indexed columns 
>
> - 인덱스가 생성되어 있는 칼럼에 양쪽 범위를 한정하는 형태로 검색하는 방식이다. 이러한 연산자에는 BETWEEN, LIKE 등이 있다. 만약 A 칼럼에 인덱스가 생성되어 있고, A BETWEEN ‘10’ AND ‘20’ 또는 A LIKE '1%' 형태로 검색하는 방식이다.
>
> 규칙 11. Unbounded range search on indexed columns 
>
> - 인덱스가 생성되어 있는 칼럼에 한쪽 범위만 한정하는 형태로 검색하는 방식이다. 이러한 연산자에는 >, >=, <, <= 등이 있다. 만약 A 칼럼에 인덱스가 생성되어 있고, A > '10' 또는 A < '20' 형태로 검색하는 방식이다.
>
> 규칙 15. Full table scan 
>
> - 전체 테이블을 액세스하면서 조건절에 주어진 조건을 만족하는 행만을 결과로 추출한다.



규칙기반 옵티마이저는 **인덱스를 이용한 액세스 방식이 전체 테이블 액세스 방식보다 우선 순위가 높다**.

따라서 규칙기반 옵티마이저는 해당 SQL문에서 이용 가능한 인덱스가 존재한다면 전체 테이블 액세스 방식보다는 항상 인덱스를 사용하는 실행계획을 생성한다. 

> 참고
>
> 규칙기반 옵티마이저가 조인 순서를 결정할 때는 조인 칼럼 인덱스의 존재 유무가 중요한 판단의 기준이다. 조인 칼럼에 대한 인덱스가 양쪽 테이블에 모두 존재한다면 앞에서 설명한 규칙에 따라 우선 순위가 높은 테이블을 선행 테이블(Driving Table)로 선택한다. 한쪽 조인 칼럼에만 인덱스가 존재하는 경우에는 인덱스가 없는 테이블을 선행 테이블로 선택해서 조인을 수행한다. 조인 칼럼에 모두 인덱스가 존재하지 않으면 FROM 절의 뒤에 나열된 테이블을 선행 테이블로 선택한다. 만약 조인 테이블의 우선 순위가 동일하다면 FROM 절에 나열된 테이블의 역순으로 선행 테이블을 선택한다. 규칙기반 옵티마이저의 조인 기법의 선택은 다음과 같다. 양쪽 조인 칼럼에 모두 인덱스가 없는 경우에는 Sort Merge Join을 사용하고 둘 중하나라도 조인 칼럼에 인덱스가 존재한다면 일반적으로 NL Join을 사용한다.

다음 SQL문을 이용해서 규칙기반 옵티마이저의 최적화 과정을 알아보자.

```sql
SELECT ENAME
FROM EMP 
WHERE JOB = 'SALESMAN' AND SAL BETWEEN 3000 AND 6000 
INDEX 
--------------------------------- 
EMP_JOB : JOB 
EMP_SAL : SAL 
PK_EMP : EMPNO (UNIQUE)
```



조건절에서 JOB 칼럼의 조건은 ‘=’, SAL 칼럼의 조건은 ‘BETWEEN’으로 값이 주어졌고 각각의 칼럼에 단일 칼럼 인덱스가 존재한다. 우선 순위 규칙에 따라 JOB 조건은 규칙 9의 단일 칼럼 인덱스를 만족하고 SAL 조건은 규칙 10의 인덱스상의 양쪽 한정 검색을 만족한다. 

따라서 우선 순위가 높은 EMP_JOB 인덱스를 이용해서 조건을 만족하는 행에 대해 EMP 테이블을 액세스하는 방식을 선택할 것이다. 다음은 규칙기반 옵티마이저가 생성한 실행계획이다.

```sql
Execution Plan 
------------------------------------------------------------ 
SELECT STATEMENT Optimizer=CHOOSE 
	TABLE ACCESS (BY INDEX ROWID) OF 'EMP' 
		INDEX (RANGE SCAN) OF 'EMP_JOB' (NON-UNIQUE)
```



단점

- 통계정보를 활용하지 않고 단순한 규칙에만 의존하기 때문에 대량 데이터를 처리하는 데 부적합

<br/>

##### 나. 비용기반 옵티마이저

규칙기반 옵티마이저는 조건절에서 ‘=’ 연산자와 'BETWEEN' 연산자가 사용되면 규칙에 따라 ‘=’ 칼럼의 인덱스를 사용하는 것이 보다 적은 일량 즉, 보다 적은 처리 범위로 작업을 할 것이라고 판단한다. 

그러나 실제로는 ‘BETWEEN’ 칼럼을 사용한 인덱스가 보다 일량이 적을 수 있다. 단순한 몇 개의 규칙만으로 현실의 모든 사항을 정확히 예측할 수는 없다. 

비용기반 옵티마이저는 이러한 규칙기반 옵티마이저의 단점을 극복하기 위해서 출현하였다. 비용기반 옵티마이저는 SQL문을 처리하는데 필요한 비용이 가장 적은 실행계획을 선택하는 방식이다. 여기서 **비용이란 SQL문을 처리하기 위해 예상되는 소요시간 또는 자원 사용량**을 의미한다. 

비용기반 옵티마이저는 비용을 예측하기 위해서 규칙기반 옵티마이저가 사용하지 않는 테이블, 인덱스, 칼럼 등의 다양한 객체 통계정보와 시스템 통계정보 등을 이용한다. 통계정보가 없는 경우 비용기반 옵티마이저는 정확한 비용 예측이 불가능해져서 비효율적인 실행계획을 생성할 수 있다. 그렇기 때문에 정확한 통계정보를 유지하는 것은 비용기반 최적화에서 중요한 요소이다.

![sql가이드](http://www.dbguide.net/publishing/img/knowledge/SQL_241.jpg)

[그림 Ⅱ-3-3]과 같이 비용기반 옵티마이저는 질의 변환기, 대안 계획 생성기, 비용 예측기 등의 모듈로 구성되어 있다. 

- 질의 변환기
  - 사용자가 작성한 SQL문을 처리하기에 보다 용이한 형태로 변환하는 모듈이다. 

- 대안 계획 생성기
  - 동일한 결과를 생성하는 다양한 대안 계획을 생성하는 모듈이다. 대안 계획은 연산의 적용 순서 변경, 연산 방법 변경, 조인 순서 변경 등을 통해서 생성된다. 동일한 결과를 생성하는 가능한 모든 대안 계획을 생성해야 보다 나은 최적화를 수행할 수 있다.
  - 그러나 대안 계획의 생성이 너무 많아지면 최적화를 수행하는 시간이 그만큼 오래 걸릴 수 있다. 그래서 대부분의 상용 옵티마이저들은 대안 계획의 수를 제약하는 다양한 방법을 사용한다. 이러한 현실적인 제약으로 인해 생성된 대안 계획들 중에서 최적의 대안 계획이 포함되지 않을 수도 있다. 

- 비용 예측기
  - 대안 계획 생성기에 의해서 생성된 대안 계획의 비용을 예측하는 모듈이다. 대안 계획의 정확한 비용을 예측하기 위해서 연산의 중간 집합의 크기 및 결과 집합의 크기, 분포도 등의 예측이 정확해야 한다. 보다 나은 예측을 위해 옵티마이저는 정확한 통계정보를 필요로 한다. 또한 대안 계획을 구성하는 각 연산에 대한 비용 계산식이 정확해야 한다. 

앞에서 규칙기반 옵티마이저는 항상 인덱스를 사용할 수 있다면 전체 테이블 스캔 보다는 인덱스를 사용하는 실행계획을 생성한다고 했다. 

그렇지만 비용기반 옵티마이저는 인덱스를 사용하는 비용이 전체 테이블 스캔 비용보다 크다고 판단되면 전체 테이블 스캔을 수행하는 방법으로 실행계획을 생성할 수도 있다.

비용기반 옵티마이저는 통계정보, DBMS 버전, DBMS 설정 정보 등의 차이로 인해 동일 SQL문도 서로 다른 실행계획이 생성될 수 있다. 또한 비용기반 옵티마이저의 다양한 한계들로 인해 실행계획의 예측 및 제어가 어렵다는 단점이 있다.



### REFERENCE

[DB GUIDE - Optimizer](http://www.dbguide.net/db.db?cmd=view&boardUid=148208&boardConfigUid=9&categoryUid=216&boardIdx=136&boardStep=1)