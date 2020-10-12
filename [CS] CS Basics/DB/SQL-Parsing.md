# SQL Parsing



이전 Optimizer에서 다뤘던 SQL 파싱에 대해 조금 더 알아보자.

<br/>

기본적인 SQL 최적화 과정은 다음과 같다.

1. SQL 파싱
   - 사용자로부터 SQL 전달
   - SQL 파서가 파싱 진행
2. SQL 최적화
   - 옵티마이저가 최적화 진행
   - 시스템 및 오브젝트 통계정보를 바탕으로 다양한 실행 경로 비교하여 선택
3. Row-Source 생성
   - 옵티마이저가 선택한 실행경로를 실제 실행 가능한 코드 또는 프로시저 형태로 포맷팅

<br/>

### Soft Parsing vs Hard Parsing

SQL 파싱에는 Soft Parsing, Hard Parsing 두 가지 방식이 있다. 

차이점을 알아보자.

<br/>

#### SQL Cache

DB에는 SGA(System Global Area)라는 서버 프로세스와 백그라운드 프로세스가 공통으로 액세스하는 데이터와 제어 구조를 캐싱하는 메모리 공간이 존재한다.

SGA 구성 요소인 라이브러리 캐시(Library Cache)는 SQL 파싱, 최적화, 로우 소스 생성 과정을 거쳐 생성한 내부 프로시저를 반복 재사용할 수 있도록 캐싱해두는 메모리 공간이다. (SGA는 Oracle 기준)

> 참고
>
> Mysql의 경우 아래 그림과 같이 Query Cache를 사용한다.

DBMS가 SQL를 파싱한 후 해당 SQL이 라이브러리 캐시에 존재한다면 곧 바로 실행 단계로 넘어간다. 그렇지 않다면 최적화 단계를 거친다.

SQL을 캐시에서 찾아 곧바로 실행 단계로 넘어가는 것은 Soft Parsing이다.

캐시에서 찾는 것을 실패해 최적화 및 Row source 생성 단계까지 모두 거치는 것을 Hard Parsing이라 한다.

![oracle architecture](https://docs.oracle.com/en/database/oracle/oracle-database/20/cncpt/img/cncpt325.gif)

[Oracle Architecture]

![mysql](https://dev.mysql.com/doc/refman/8.0/en/images/mysql-architecture.png)

[MYSQL Architecture]

<br/>

<br/>

### Why Hard?

SQL 최적화는 옵티마이저가 최적의 경로를 찾는 과정이다. 

만약 3개의 테이블을 조인한다고 해보자. 

조인 순서를 고려하면 최대 6(3!)가지가 나온다. 여기에 조인 방식, 테이블 스캔 방식 등등 고려하면 경우의 수는 증가한다. 

하나의 쿼리를 수행하는데 후보군이 될만한 많은 실행경로를 도출하고, 딕셔너리와 통계정보를 읽어 효율성을 판단하는 과정은 쉽지 않다. 

Hard Parsing은 DB에서 CPU를 많이 소비하는 몇 안되는 작업 중 하나다.

따라서 Hard Parsing을 거쳐 생성된 내부 프로시저를 일회용으로 사용하고 만다면 비효율적인 것이다. 그렇기에 라이브러리 캐시가 필요하다.

<br/>

### Bind Parameter

사용자 정의 함수/프로시저, 트리거 등은 생성시 이름을 갖는다. 따라서 컴파일하게 되면 딕셔너리에 영구 보관된다. 

실행하면 라이브러리 캐시에 적재되어 재사용이 가능하다.

그러나 SQL은 따로 이름이 없고 텍스트 자체가 이름 역할을 한다. 

라이브러리 캐시는 캐시다. 즉, 모든 SQL를 저장할 수 없다. 

<br/>

다음 SQL문을 확인해보자.

```sql
SELECT * FROM EMP WHERE EMPNO = 1;
SELECT * FROM emp WHERE empno = 1;
select * from EMP where EMPNO = 1;
select * from emp where empno = 1;
select * from emp where empno = 1 ;
select * from emp where empno = 1; -- empno가 1인 경우 찾기.
```

실행 시 나오는 결과는 모두 같다. 

그런데 위에서도 말했듯이 SQL문은 그 자체가 이름 역할을  하기에 실행하면 각각 Hard Parsing을 하고 캐시에 공간을 사용한다.

<br/>

예시를 생각해보자.

```java
String sql = "SELECT * FROM CUSTOMER WHERE ID ='" + login_id +"'";
```

위와 같은 sql문을 쇼핑몰 로그인 모듈에서 사용했다고 생각해보자. 

만약 100만명이 동시접속하려고 한다면 어떤 일이 발생할까?

100만개의 SQL이 하드파싱되면서 CPU 사용률이 급격히 올라가 부하가 생길 것이다.

그렇다면 어떻게 해결할 까?

```sql
create procedure LOGIN(id in varchar2){}
```

위와 같은 프로시저를 생성하고 parameter로 id를 넘겨주게 하면 된다. 

```java
String sql = "SELECT * FROM CUSTOMER WHERE ID = ?";
PreparedStatement st = con.prepareStatement(SQL);
st.setString(1,login_id);
```

위와 같이 수정한다면 하드 파싱은 한 번만 일어날 것이고 라이브러리 캐시에서도 SQL 하나만 발견 될 것이다. 



<br/>

### REFERENCE

[친절한 SQL 튜닝]

[Mysql 8.0 Manual](https://dev.mysql.com/doc/refman/8.0/en/pluggable-storage-overview.html)