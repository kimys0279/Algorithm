# SQL

SQL(Structured Query Language)은 관계형 데이터베이스에서 데이터 정의, 데이터 조작, 데이터 제어를 하기 위해 사용하는 언어이다. 

각 벤더의 관계형 데이터베이스(RDBMS)는 표준화된 SQL 이외에도 벤더 차별화 및 이용 편리성을 위해 추가 기능이나 내장 함수 등에서 독자적 개발을 계속 진행하고 있다. 상호 호환성이 뛰어난 표준 기능과, 벤더별 특징을 가지고 있는 독자적 기능 중 어떤 기능을 선택할 지는 사용자의 몫이지만 가능한 ANSI/ISO 표준을 기준으로 할 것을 권고한다.

SQL 문장은 단순 스크립트가 아니라 이름에도 포함되어 있듯이, 일반적인 개발 언어처럼 독립된 하나의 개발 언어이다. 

하지만 일반적인 프로그래밍 언어와는 달리 SQL은 관계형 데이터베이스에 대한 전담 접속(다른 언어는 관계형 데이터베이스에 접속할 수 없다) 용도로 사용되며 집합 논리에 입각한 것이므로, SQL도 데이터를 집합으로써 취급한다. 

이렇게 특정 데이터들의 집합에서 필요로 하는 데이터를 꺼내서 조회하고 새로운 데이터를 입력/수정/삭제하는 행위를 통해서 사용자는 데이터베이스와 대화하게 된다. 그리고 SQL은 이러한 대화를 가능하도록 매개 역할을 하는 것이다. 결과적으로 SQL 문장을 배우는 것이 곧 관계형 데이터베이스를 배우는 기본 단계라 할 수 있다.

<br/>

SQL 문장과 관련된 용어 중에서 먼저 테이블에 대한 내용은 건드리지 않고 단순히 조회를 하는 SELECT 문장이 있다. 그리고 테이블에 들어 있는 데이터에 변경을 가하는 UPDATE, DELETE, INSERT 문장은 테이블에 들어 있는 데이터들을 조작하는 종류의 SQL 문장들이다. 그 외, 테이블을 생성하고 수정하고 변경하고 삭제하는 테이블 관련 SQL 문장이 있고, 추가로 데이터에 대한 권한을 제어하는 SQL 문장도 있다.

| 명령어 종류         | 명령어                               | 설명                                                         |
| ------------------- | ------------------------------------ | ------------------------------------------------------------ |
| 데이터 정의어 (DDL) | CREATE<br/>ALTER<br/>DROP<BR/>RENAME | 테이블과 같은 데이터 구조를 정의하는데 사용되는 명령어들로 그러한 구조를 생성하거나 변경하거나 삭제하거나 이름을 바꾸는 데이터 구조와 관련된 명령어들이다. |
| 데이터 조작어 (DML) | SELECT                               | DB에 들어 있는 데이터를 조회하거나 검색하기 위한 명령어이다. |
|                     | INSERT<br/>UPDATE<br/>DELETE         | DB의 테이블에 들어 있는 데이터에 변형을 가하는 종류의 명령어이다. 예를 들어 데이터를 테이블에 새로운 행을 집어넣거나, 원하지 않는 데이터를 삭제하거나 수강하는 것들의 명령어이다. |
| 데이터 제어어 (DCL) | GRANT<br/>REVOKE                     | DB에 접근하고 객체들을 사용하도록 권한을 주고 회수하는 명령어이다. |

<출처 : DBGUIDE >

<br/>

이제부터 SQL를 직접 써보면서 알아볼 것이다. 

RDBMS은 mysql 5.7를 사용할 것이므로 sql 도 mysql 5.7에 맞게 작성하였다.

<br/>

### Mysql 기본 

mysql 를 설치했다면 다음과 같이 mysql를 접속할 수 있다.

```shell
shell> mysql -u user -p 
-- user에는 유저 이름
-- 이후 패스워드 입력
Enter password:
```

``` mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is x
Server version: 5.7.31-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

접속한다면 위와 같은 화면이 나온다.

<br/>

#### Query 입력

mysql > 옆에 쿼리를 입력하고 **세미콜론**을 입력하면 해당하는 결과를 확인할 수 있다.

```mysql
mysql> SELECT VERSION(), CURRENT_DATE;
+-------------------------+--------------+
| VERSION()               | CURRENT_DATE |
+-------------------------+--------------+
| 5.7.31-0ubuntu0.18.04.1 | 2020-08-17   |
+-------------------------+--------------+
1 row in set (0.00 sec)
```

<br/>

**여러 쿼리 입력**

단순히 세미콜론으로 구분할 수 있다.

```mysql
mysql> SELECT VERSION(); SELECT NOW();
+-------------------------+
| VERSION()               |
+-------------------------+
| 5.7.31-0ubuntu0.18.04.1 |
+-------------------------+
1 row in set (0.00 sec)

+---------------------+
| NOW()               |
+---------------------+
| 2020-08-17 18:06:44 |
+---------------------+
1 row in set (0.00 sec)
```

<br/>

| Prompt   | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| `mysql>` | 쿼리 입력 대기 중                                            |
| `->`     | 여러 줄의 쿼리 중 다음 줄입력 대기 중                        |
| `'>`     | 작은 따옴표(')의 완성을 입력 대기 중                         |
| `">`     | 큰 따옴표(")의 완성 입력 대기 중                             |
| ``>`     | Waiting for next line, waiting for completion of an identifier that began with a backtick (```) |
| `/*>`    | Waiting for next line, waiting for completion of a comment that began with `/*` |

**예시**

```mysql
mysql> SELECT USER()
    -> ;
mysql> SELECT * FROM my_table WHERE name = 'Smith AND age < 30;
    '>
    
```

<br/>

#### 데이터베이스 생성과 사용

mysql은 데이터베이스 생성하고 사용할 수 있다. 즉, 여러 데이터베이스를 사용할 수 있다.

**생성(Create)**

```mysql
mysql> CREATE DATABASE catch;
```

다음과 같이 'catch' 데이터베이스를 만들 수 있다. 

> 유닉스 시스템하에서는 SQL 키워드와는 다르게 데이터베이스 이름은 대소문자 구분을 한다. 
>
> catch 데이터베이스를 접근할 때, Catch, CATCH 등과 같은 경우는 불가하다는 것이다. 테이블의 경우도 동일하다 (다만 윈도우의 경우 적용되지 않는다.)

**사용(Select)**

데이터베이스 생성이 사용을 뜻하지는 않는다. 따라서 사용하기 위해서는 다음과 같이 쿼리를 입력한다.

```mysql
mysql> USE catch;
Database changed
```

<br/>

<br/>

### DDL

DDL은 다음 5 개의 명령어가 있다.

- CREATE
- ALTER
- DROP
- RENAME
- TRUNCATE

<br/>

| 명령어                     | 적용 가능 대상                                               |
| -------------------------- | ------------------------------------------------------------ |
| CREATE & ALTER & DROP 공통 | DATABASE<br/>EVENT<br/>FUNCTION<br/>LOGFILE GROUP<br/>PROCEDURE & FUNCTION<br/>SERVER<br/>TABLE<br/>TABLESPACE<br/>VIEW |
| CREATE & DROP              | **INDEX <br/>TRIGGER**                                       |
| ALTER                      | **INSTANCE**                                                 |
| RENAME, TRUNCATE           | TABLE                                                        |

<br/>

#### CREATE

가볍게 Database와 Table만 보자.

**Database**

```mysql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_option] ...

create_option: {
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
}
```

CREATE DATABASE 는 주어진 이름으로 데이터베이스를 생성한다. 생성문을 사용하기 위해서는 생성 권한이 필요아하다. 

> CREATE SCHEMA 는 CREATE DATABASE의 동의어이다.

만약 동일한 이름이 존재하고 IF NOT EXISTS을 명시하지 않았다면 에러가 발생한다.

<br/>

show 명령어를 통해 현재의 데이터베이스를 확인할 수 있다.

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> create database catch;	-- catch 라는 데이터베이스 생성
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| catch              |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
-- 만약 다시 만드려고 하면 에러 발생.
mysql> create database catch;
ERROR 1007 (HY000): Can't create database 'catch'; database exists
```

<br/>

**Table**

```mysql
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]

create_definition: {
    col_name column_definition
  | {INDEX | KEY}
  | {FULLTEXT | SPATIAL} [INDEX | KEY] 
  | [CONSTRAINT [symbol]] PRIMARY KEY
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
  | [CONSTRAINT [symbol]] FOREIGN KEY
  | CHECK (expr)
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT default_value]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [STORAGE {DISK | MEMORY}]
      [reference_definition]
  | data_type
      [COLLATE collation_name]
      [GENERATED ALWAYS] AS (expr)
      [VIRTUAL | STORED] [NOT NULL | NULL]
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [reference_definition]
}


table_option: {
    AUTO_INCREMENT [=] value
  | AVG_ROW_LENGTH [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | CONNECTION [=] 'connect_string'
  | {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTION [=] {'Y' | 'N'}
  | ENGINE [=] engine_name
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] value
  | MAX_ROWS [=] value
  | MIN_ROWS [=] value
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value
  | TABLESPACE tablespace_name [STORAGE {DISK | MEMORY}]
  | UNION [=] (tbl_name[,tbl_name]...)
}

partition_options:
    PARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list)
        | RANGE{(expr) | COLUMNS(column_list)}
        | LIST{(expr) | COLUMNS(column_list)} }
    [PARTITIONS num]
    [SUBPARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list) }
      [SUBPARTITIONS num]
    ]
    [(partition_definition [, partition_definition] ...)]

    SELECT ...   (Some valid select or union statement)
```

Table의 경우 생성하면서 다양한 옵션을 설정할 수 있다.

- 정의
  - 컬럼별 졍의
    - data type
  - Constraint
  - Key

- 테이블 옵션
  - 위의 SQL 참고
- 파티션 옵션
  - 파티셔닝 시 사용되는 옵션

<br/>

간단한 예제를 통해 테이블을 생성해보자.

**예제 1**

```mysql
mysql> CREATE TABLE dept (
    ->   dept_no INT(11) unsigned NOT NULL,
    ->   dept_name VARCHAR(32) NOT NULL,
    ->   PRIMARY KEY (dept_no)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> describe dept;  --  describe or desc
+-----------+------------------+------+-----+---------+-------+
| Field     | Type             | Null | Key | Default | Extra |
+-----------+------------------+------+-----+---------+-------+
| dept_no   | int(11) unsigned | NO   | PRI | NULL    |       |
| dept_name | varchar(32)      | NO   |     | NULL    |       |
+-----------+------------------+------+-----+---------+-------+
2 rows in set (0.09 sec)
```

dept라는 테이블은 dept_no, dept_name으로 구성되어 있으며 각각 int(11자리), 가변문자 32자리까지 가능하다.

또한, dept_no을 기본 키를 가진다는 테이블을 생성하였다.

<br/>

**예제 2**

예제 1보다 조금 더 복잡하게 만들어보자.

```mysql
mysql> create table student (
    -> id int(10) unsigned NOT NULL AUTO_INCREMENT,
    -> name varchar(20) NOT NULL,
    -> dept_no int(11) unsigned,
    -> grade int(4) unsigned NOT NULL default '1',
    -> PRIMARY KEY(id),
    -> FOREIGN KEY (dept_no) REFERENCES dept (dept_no)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> desc student;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name    | varchar(20)      | NO   |     | NULL    |                |
| dept_no | int(11) unsigned | YES  | MUL | NULL    |                |
| grade   | int(4) unsigned  | NO   |     | 1       |                |
+---------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

student라는 테이블을 생성하였다.

하나씩 설명해보자.

- id는 int 10자리, 양수만 가능하며 NULL이 허용되지 않는다. 또한 AUTO_INCREMENT를 통해 자동적으로 증가한다. 기본 키이다.
- dept_no는 dept 테이블의 dept_no을 외래키로 사용하여 설정한다.
- grade는 NULL이 허용되지 않으며 default값으로 1을 가진다.

<br/>

#### ALTER

ALTER는 적용 대상의 기존 조건을 수정, 추가, 제거할 수 있다. 

다음 형태로 사용된다.

```mysql
ALTER TABLE tbl_name
    [alter_option [, alter_option] ...]
    [partition_options]
    
alter_option: {
    table_options
  | ADD [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ADD [COLUMN] (col_name column_definition,...)
  | ADD {INDEX | KEY} [index_name]
        [index_type] (key_part,...) [index_option] ...
  | ADD {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name]
        (key_part,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]] PRIMARY KEY
        [index_type] (key_part,...)
        [index_option] ...
  | ADD [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
        [index_name] [index_type] (key_part,...)
        [index_option] ...
  | ADD [CONSTRAINT [symbol]] FOREIGN KEY
        [index_name] (col_name,...)
        reference_definition
  | ADD CHECK (expr)
  | ALGORITHM [=] {DEFAULT | INPLACE | COPY}
  | ALTER [COLUMN] col_name {SET DEFAULT literal | DROP DEFAULT}
  | CHANGE [COLUMN] old_col_name new_col_name column_definition
        [FIRST | AFTER col_name]
  | [DEFAULT] CHARACTER SET [=] charset_name [COLLATE [=] collation_name]
  | CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
  | {DISABLE | ENABLE} KEYS
  | {DISCARD | IMPORT} TABLESPACE
  | DROP [COLUMN] col_name
  | DROP {INDEX | KEY} index_name
  | DROP PRIMARY KEY
  | DROP FOREIGN KEY fk_symbol
  | FORCE
  | LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
  | MODIFY [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ORDER BY col_name [, col_name] ...
  | RENAME {INDEX | KEY} old_index_name TO new_index_name
  | RENAME [TO | AS] new_tbl_name
  | {WITHOUT | WITH} VALIDATION
}
-- partition option은 생략
```

- 추가
  - 컬럼
  - 인덱스
  - 기본 키
  - 외래 키
  - 조건 등등
- 수정
  - 컬럼 이름 등등
- 제거
  - 컬럼
  - 인덱스
  - 기본키/ 외래키

등등이 가능하다. 

<br/>

**예제 1**

현재 상태

```mysql
mysql> desc student;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name    | varchar(20)      | NO   |     | NULL    |                |
| dept_no | int(11) unsigned | YES  | MUL | NULL    |                |
| grade   | int(4) unsigned  | NO   |     | 1       |                |
+---------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

**칼럼 추가**

age라는 칼럼을 int(10)으로 추가하였다.

```mysql
mysql> alter table student add column age int(10) unsigned not null;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name    | varchar(20)      | NO   |     | NULL    |                |
| dept_no | int(11) unsigned | YES  | MUL | NULL    |                |
| grade   | int(4) unsigned  | NO   |     | 1       |                |
| age     | int(10) unsigned | NO   |     | NULL    |                |
+---------+------------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
```

**칼럼 변경**

age라는 칼럼을 age int(5) + NULL  허용으로 변경하였다.

```mysql

mysql> alter table student change column age age int(5) unsigned;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name    | varchar(20)      | NO   |     | NULL    |                |
| dept_no | int(11) unsigned | YES  | MUL | NULL    |                |
| grade   | int(4) unsigned  | NO   |     | 1       |                |
| age     | int(5) unsigned  | YES  |     | NULL    |                |
+---------+------------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
```

**칼럼 제거**

age라는 칼럼을 제거하였다.

```mysql
mysql> alter table student drop column age;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name    | varchar(20)      | NO   |     | NULL    |                |
| dept_no | int(11) unsigned | YES  | MUL | NULL    |                |
| grade   | int(4) unsigned  | NO   |     | 1       |                |
+---------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

<br/>

<br/>

#### DROP

DROP은 적용 대상을 제거한다.

다음 SQL문 형태로 사용한다.

```mysql
DROP [TEMPORARY] TABLE [IF EXISTS]
    tbl_name [, tbl_name] ...
    [RESTRICT | CASCADE]
```

- RESTRICT :해당 테이블과 의존성 관계가 있는 객체가 있으면 작업을 중지한다. 이 옵션이 기본값이다.

- CASCADE : 해당 테이블과 의존성 관계가 있는 모든 객체들도 함께 삭제한다.

<br/>

**예제**

dept라는 테이블이 student 테이블의 외래 키를 가지고 있으므로 dept 테이블을 삭제해보자.

```mysql
mysql> drop table dept;
ERROR 1217 (23000): Cannot delete or update a parent row: a foreign key constraint fails
mysql> drop table dept cascade;
ERROR 1217 (23000): Cannot delete or update a parent row: a foreign key constraint fails
```

??? 다 안된다. 

왜 안되는 지 이유를 찾아보니 

> The `RESTRICT` and `CASCADE` keywords do nothing. They are permitted to make porting easier from other database systems.

mysql 5.7 manual에 이렇게 적혀있다. RESTRICT / CASCADE 키워드는 아무것도 안한다. 그저 다른 DB시스템으로부터 이식하기 쉽도록 만든거다.

관계가 있는 테이블을 함부로 할 수 없도록 안전장치를 해 둔 것이다. 

따라서

```mysql
SET FOREIGN_KEY_CHECKS = 0;
drop table dept;
SET FOREIGN_KEY_CHECKS = 1;
```

와 같은 형태가 되어야 한다.

아래는 결과이다. 

```mysql
mysql> SET FOREIGN_KEY_CHECKS = 0;
ble deptQuery OK, 0 rows affected (0.00 sec)

mysql> drop table dept;
 FOREIGN_KEY_CHECKS = 1;Query OK, 0 rows affected (0.00 sec)

mysql> SET FOREIGN_KEY_CHECKS = 1;
Query OK, 0 rows affected (0.00 sec)

mysql> show tables;
+-----------------+
| Tables_in_catch |
+-----------------+
| student         |
+-----------------+
1 row in set (0.00 sec)
```

<br/>

#### RENAME

RENAME은 테이블만 적용 가능하다. 단어 뜻 그대로 이름을 다시 짓는 것이다.

다음과 같이 사용한다.

```mysql
RENAME TABLE
    tbl_name TO new_tbl_name
    [, tbl_name2 TO new_tbl_name2] ...
```

 <br/>

**사용 예시**

```mysql
RENAME TABLE old_table TO new_table;
ALTER TABLE old_table RENAME new_table;
```

위의 두 SQL문은 똑같은 효과를 발생한다.

다만 다른 점은 RENAME은 다음과 같이 여러 개의 테이블 명을 바꿀 수 있다. (ALTER는 불가)

```mysql
RENAME TABLE old_table1 TO new_table1,
             old_table2 TO new_table2,
             old_table3 TO new_table3;
```

**다른 DB로 이동**

다음과 같이 사용하여 다른 DB의 테이블로 테이블을 이동시킬 수 있다.

```mysql
RENAME TABLE current_db.tbl_name TO other_db.tbl_name;
```

<br/>

#### TRUNCATE

TRUNCATE 명령어는 테이블을 완전히 비운다. 이를 사용하기 위해서는 DROP권한이 있어야 한다.

다음과 같이 사용한다.

```mysql
TRUNCATE [TABLE] tbl_name
```

<br/>

> 미리 보는 DROP, TRUNCATE, DELETE의 차이점
>
> DROP, TRUNCATE, DELETE * FROM tbl 은 모두 삭제하는 명령어이다. 
>
> 그렇다면 차이점은 무엇일까?
>
> **DROP vs TRUNCATE**
>
> DROP은 테이블 객체 자체를 삭제시킨다. 따라서 테이블의 존재가 사라진다.
>
> TRUNCATE은 테이블의 모든 내용을 삭제시킨다. 
>
> ```mysql
> mysql> show tables;				-- 기존 테이블 현황
> +-----------------+
> | Tables_in_catch |
> +-----------------+
> | student         |
> +-----------------+
> 1 row in set (0.00 sec)
> 
> mysql> truncate table student;
> Query OK, 0 rows affected (0.01 sec)
> 
> mysql> show tables;				-- Truncate해도 table은 그대로 남아있다.
> +-----------------+
> | Tables_in_catch |
> +-----------------+
> | student         |
> +-----------------+
> 1 row in set (0.00 sec)
> 
> mysql> drop table student;		-- DROP
> Query OK, 0 rows affected (0.01 sec)
> 
> mysql> show tables;				-- DROP 하니 테이블이 없다
> Empty set (0.00 sec)
> ```
>
> <br/>
>
> **TRUNCATE vs DELETE**
>
> |                     | TRUNCATE             | DELETE            |
> | ------------------- | -------------------- | ----------------- |
> | 명령어              | DDL                  | DML               |
> | 속도                | 우세( DROP & CREATE) | 약세 (row by row) |
> | Rollback            | 불가 (b/c it's DDL)  | 가능              |
> | AUTO_INCREMENT 옵션 | 초기화               | 마지막 번호 유지  |
>
> 더 자세한 차이점은 [여기서 확인](https://dev.mysql.com/doc/refman/5.7/en/truncate-table.html)

<br/>

### DML





### REFERENCE

[DBGUIDE - SQL](http://www.dbguide.net/db.db?cmd=view&boardUid=148189&boardConfigUid=9&categoryUid=216&boardIdx=134&boardStep=1)

[MySQL 5.7 Manual](https://dev.mysql.com/doc/refman/5.7/en/)