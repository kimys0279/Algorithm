### 개요  
SQL 인젝션(SQL 삽입, SQL 주입으로도 불린다)은 코드 인젝션의 한 기법으로, 클라이언트의 입력값을 조작하여 서버의 데이터베이스를 공격할 수 있는 공격방식을 말한다.  
  
예를들어, 웹페이지 로그인 화면의 비밀번호 입력값에 SQL문의 일부를 입력하여, 쿼리 입력값 파라미터 매핑에 주입하는 경우이다.  
  
주로 사용자가 입력한 데이터가 유효성검사를 통과하여, 제대로 필터링하지 못했을 경우에 발생한다.  
  
공격 난이도가 낮지만 공격으로 인한 피해가 대체로 큰 편이다.  
  
이러한 injection 계열의 취약점들은 테스트를 통해 발견하기는 힘들지만, 스캐닝툴이나 코드 검증절차를 거치면 보통 쉽게 발견되기 때문에 탐지하기는 쉬운 편이다.  
   
OWASP(The Open Web Application Security Project)에서도 수년 동안 인젝션 기법이 보안 위협 1순위로 분류되는 만큼 보안에 각별한 주의가 필요하다.  
  
  
### 공격방법  
위에서 예를 든 비밀번호 입력값에  ' OR '1' = '1 를 입력하였다면,  
SELECT user FROM user_table WHERE id='admin' AND password=' ' OR '1' = '1 ';  
와 같은 쿼리가 실행될 수 있다.  
  
조건절 외에, JOIN 이나 UNION과 같은 구문을 통해서 실행할 수도 있다.  
  
  
### 방어방법
1. JDBC에는 PreparedStatement 클래스를 제공하므로, CreateStatement의 사용 구문을 대체하여 사용한다.    
(변수를 문자열로 바꾸는 것으로, 쿼리를 사전에 컴파일 한 뒤에 변수만 따로 집어넣어 실행한다.)  
  
2. throw Exception과 같은 Error Message 노출을 제거한다.  
  
  
### 참고자료  
1. [나무위키 SQL injection](https://namu.wiki/w/SQL%20injection)  
2. [위키백과 OWASP](https://ko.wikipedia.org/wiki/OWASP)  
3. [SQL Injection 이란? (SQL 삽입 공격)](https://noirstar.tistory.com/264)  
4. [prepareStatement 와 createStatement의 차이점](https://liketh.tistory.com/entry/prepareStatement-%EC%99%80-createStatement-%EC%B0%A8%EC%9D%B4%EC%A0%90)  