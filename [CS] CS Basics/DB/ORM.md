# ORM (Object Relational Mapping)

<p><div align="center"><img src="https://media.vlpt.us/post-images/alskt0419/668a9bb0-23a4-11ea-b8e9-c92e4da32c9c/ORM.png"></div></p>

객체지향적 구조? 모든 데이터는 객체이며, 각 객체는 독립된 데이터와 독립된 함수를 지님

SQL 구조? 데이터는 테이블 단위로 관리되며 객체들을 조회하기 위한 명령어를 사용

ORM은 각 테이블 또는 구분하고자 하는 데이터 단위로 객체를 구현하고, 데이터 간의 관계를 형성

<p><div align="center"><img src="https://t1.daumcdn.net/cfile/tistory/9971C03F5BA051390B"></div></p>

객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 Framework

객체지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 테이블을 사용하기 때문에 객체 모델과 관계형 모델간에 불일치가 존재 → ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결

즉, 객체를 통해 간접적으로 데이터베이스 데이터를 다룸

이러한 중간 계층을 Persistence Layer라 하며, ORM Framework들은 기존의 Entity Bean(*[여기](https://kimseunghyun76.tistory.com/327) 참고)이 수행하던 Persistence Bridge의 역할을 ORM 패러다임의 Entity 방식으로 가능하게 함

<br><br>

## 사용 예제

- Java

  ```java
  public class Person{
      private String name;
      private String height;
      private String weight;
      private String ssn;
      //implement getter & setter methods
  }
  ```

- iBatis

  ```xml
  <select id="getPerson" resultClass="net.agilejava.person.domain.Person">
      SELECT name, height, weight, ssn FROM USER WHERE name = #name#;
  </select>
  ```

  해당 쿼리의 결과를 받을 객체를 지정해줄 수 있다. 즉, getPerson이라고 정의된 쿼리 결과는 `net.agilejava.person.domain`의 `Person` 객체에 자동으로 매핑되는 것이다.

- Hibernate

  ```xml
  <hibernate-mapping>
      <class name="net.agilejava.person.domain.Person" table="person">
          <id name="name" column="name"/>
          <property name="height" column="height"/>
          <property name="weight" column="weight"/>
          <property name="ssn" column="ssn"/>
      <class>
  </hibernate-mapping>
  ```

위 두개의 Framework의 예시를 보면 알 수 있듯이, setter 메소드가 있으면 객체에 결과를 set하는 작업을 따로 해주지 않아도 자동으로 해당 값이 할당된다. 물론 여기에 1:m 이나 m:1등의 관계들이 형성되면 추가적인 작업이 필요하긴 하지만, 일단 눈에 보이는 간단한 부분은 처리가 되는 것을 볼 수 있다. 물론 반대의 경우에도 객체를 던져주면 ORM Framework에서 알아서 get을 수행해 해당하는 column에 넣어주게 된다.

<br><br>

## 객체-관계 간의 불일치

<p><div align="center"><img src="https://gmlwjd9405.github.io/images/database/orm-impedance-mismatch.png"></div></p>

### 세분성(Granularity)

경우에 따라서 데이터베이스에 있는 테이블 수보다 더 많은 클래스를 가진 모델이 생길 수 있다.

예를 들어, 어떤 사용자의 세부 사항에 대해 데이터를 저장한다고 해보자. 객체지향 프로그래밍에서는 코드 재사용과 유지보수를 위해 `Person`과 `Address`라는 두 개의 클래스로 나눠서 관리할 수 있다. 그러나, 데이터베이스에는 `person`이라는 하나의 테이블에 사용자의 세부사항을 모두 저장할 수 있다. 이 상황에서 Object는 2개, Table는 1개가 되어 개수가 달라지는 것이다.

### 상속성(Inheritance)

RDBMS는 객체지향 프로그래밍 언어의 특징인 상속 개념이 없다.

### 일치(Identity)

RDBMS는 'sameness'라는 하나의 개념을 정확히 정의하는데, 바로 기본키(Primary Key)를 이용하여 동일성을 정의한다. 그러나 자바는 객체 식별(`a == b`)과 객체 동일성(`a.equals(b)`)을 모두 정의한다.

즉, RDBMS에서는 PK가 같으면 서로 동일한 record로 정의하지만, Java에서는 주소값이 같거나 내용이 같은 경우를 구분해서 정의한다.

### 연관성(Associations)

객체지향 언어는 객체 참조(Reference)를 사용하는 연관성을 나타내는 반면, RDBMS는 연관성을 ‘외래키(Foreign Key)’로 나타낸다.

예를 들어, 자바에서의 객체 참조는 아래처럼 방향성이 있기 때문에,

```java
  public class Employee { 
      private int id; 
      private String first_name; 
      …
      private Department department; // Employee -> Department
      …
  }
```

양방향 관계가 필요한 경우 연관을 두 번 정의해야 한다. 즉, 서로 Reference를 가지고 있어야 한다. 그러나, RDBMS에서는 FK와 Join으로 자연스럽게 방향성이 없는 연결이 이루어진다.

<p><div align="center"><img src="https://gmlwjd9405.github.io/images/database/db-join-example.png"></div></p>

### 탐색(Navigation)

자바와 RDBMS에서 객체를 접근하는 방법이 근본적으로 다르다.

자바는 그래프 형태로 하나의 연결에서 다른 연결로 이동하며 탐색한다. 예를 들어, `user.getBillingDetails().getAccountNumber()`의 형식이다.  그러나 RDBMS에서는 일반적으로 쿼리 수를 최소화하고 `JOIN`을 통해 여러 엔티티를 로드하고 원하는 대상 엔티티를 선택(select)하는 방식으로 탐색한다.

<br><br>

## 장단점

### Pros

- 객체지향적인 코드로 인해 더 직관적이고 로직에 집중할 수 있도록 도와준다.
  - SQL문이 아닌 클래스의 메서드를 통해 데이터베이스를 조작할 수 있으므로 개발자가 객체 모델만 이용해서 프로그래밍을 하는 데 집중할 수 있다.
  - 선언문, 할당, 종료 같은 부수적인 코드가 없거나 줄어든다.
  - 객체마다 코드를 별도로 작성하기 때문에 코드의 가독성이 높아진다.
  - SQL의 절차적이고 순차적인 접근이 아닌 객체지향적인 접근으로 인해 생산성을 높여준다.
- 재사용 및 유지보수의 편리성이 증가한다.
  - ORM은 독립적으로 작성되어있고, 해당 객체들을 재활용할 수 있다.
  - 매핑 정보가 명확하여, ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- DBMS에 대한 종속성이 줄어든다.
  - 대부분 ORM 솔루션은 DB에 종속적이지 않기 때문에 구현 방법뿐만 아니라 많은 솔루션에서 자료형 타입까지 유효하다. (*종속성? 프로그램 구조가 데이터 구조에 영향을 받는다.)
  - 프로그래머는 Object에 집중함으로 극단적으로 DBMS를 교체하는 거대한 작업에도 비교적 적은 리스크와 시간이 소요된다.
  - 또한 자바에서 가공할 경우 `equals`, `hashCode`의 오버라이드 같은 자바의 기능을 이용할 수 있고, 간결하고 빠른 가공이 가능하다.

### Cons

- 완벽한 ORM 으로만 서비스를 구현하기가 어렵다.
  - 사용하기는 편하지만 설계는 매우 신중하게 해야한다.
  - 프로젝트의 복잡성이 커질경우 난이도 또한 올라갈 수 있다.
  - 잘못 구현된 경우에 속도 저하 및 심각할 경우 일관성이 무너지는 문제점이 생길 수 있다.
  - 일부 자주 사용되는 대형 쿼리는 속도를 위해 SP를 쓰는등 별도의 튜닝이 필요한 경우가 있다.
  - DBMS의 고유 기능을 이용하기 어렵다.  (하지만 이건 단점으로만 볼 수 없다 : 특정 DBMS의 고유기능을 이용하면 이식성이 저하된다.)
- 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다.
  - 이미 프로시저가 많은 시스템에선 다시 객체로 바꿔야하며, 그 과정에서 생산성 저하나 리스크가 많이 발생할 수 있다.

<br><br>

## Frameworks

### JPA/[Hibernate](https://hibernate.org/)

JPA(Java Persistence API)는 자바의 ORM 기술 표준으로 인터페이스의 모음이다. 이러한 JPA 표준 명세를 구현한 구현체가 바로 Hibernate이다.

### [Sequelize](https://sequelize.org/)

Sequelize는 Postgres, MySQL, MariaDB, SQLite 등을 지원하는 `Promise`에 기반한 비동기로 동작하는 Node.js ORM이다. Promise의 장점은 아래와 같다.

1) 복잡한 비동기 코드를 깔끔하고 쉽게 만들 수 있도록 한다.
2) Chaining을 통해 값을 전달하거나 연속된 일련의 작업을 처리 할 수 있다.
3) Error handling에 대한 처리를 깔끔하게 할 수 있다.

### [Django ORM](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

python기반 프레임워크인 Django에서 자체적으로 지원하는 ORM이다.

### Prisma

Prisma의 특징은 GraphQL스키마를 기반으로 DB를 자동생성 해준다는 것이다. (*GraphQL? facebook에서 만든 Graph Query Language로 애플리케이션 Query 언어로써 기존의 REST API의 한계점을 극복하고자 나온 통신 규약으로 REST API를 대체할 수 있다.) GraphQL의 장점은 아래와 같다.

1) 요청메세지가 값이 없는 JSON과 비슷하며 받는 데이터는 JSON형태 이다.
2) 단일요청으로 원하는 데이터를 한번에 가져올 수 있다.
3) type system을 지원한다.
4) GraphiQL 등의 강력한 도구를 사용 할 수 있다.
5) 확장성이 좋다.

<br><br>

## Reference

https://jins-dev.tistory.com/entry/ORMObject-Relational-Mapping%EC%9D%B4%EB%9E%80-ORM-%ED%8C%A8%EB%9F%AC%EB%8B%A4%EC%9E%84%EC%9D%98-%EA%B0%9C%EB%85%90

http://www.incodom.kr/ORM

https://geonlee.tistory.com/207

https://velog.io/@alskt0419/ORM%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C...-iek4f0o3fg
