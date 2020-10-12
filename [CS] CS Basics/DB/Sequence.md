### Sequence  
  
### 개요  
순차적 증가하는 순번을 반환하는 데이터베이스 객체.  
유일한 값을 생성해주는 객체로, 보통 Primary Key 값을 생성하기 위해 사용한다.  
테이블과 독립적으로 저장되고 생성되어 여러 테이블에서 쓸 수 있다.(핵심)  

  
  
### 문법  
increment by n: 시작값부터 증가값을 n으로 지정한다. 음수면 감소하며, 디폴트는 1이다.  
minvalue n: 최솟값을 n으로 지정한다.  
maxvalue n: 최댓값을 n으로 지정한다.  
nominvalue, nomaxvalue: 무한대값 지정.  
start with n: 시작값을 n으로 지정하여 순차적으로 증가한다.  
  
시퀀스명.nextval: 현재 시퀀스 값의 다음 값을 반환한다.  
시퀀스명.currval: 현재 시퀀스 값을 반환한다.  
  
cycle:  최대값을 넘으면 다시 처음부터 순환하도록 지정한다.  
nocycle: 최대값 생성시 시퀀스생성을 중지한다.  
cache n: 메모리에 캐시하는 갯수 지정. 기본값은 20이다.  
  
  
  
### 사용 예
-생성(CREATE), 수정(ALTER), 삭제(DROP) 의 각각의 예문은 다음과 같다.  
CREATE SEQUENCE test_seq  
start with 1  
increment by 1;  
  
ALTER SEQUENCE test_seq;  
  
DROP SEQUENCE test_seq;  
  
  
-현재 시퀀스 값 확인  
SELECT test_seq.currval FROM dual;  
  
  
  
### Quiz  
DELETE FROM board;  
DELETE FROM board2;  
DROP SEQUENCE test_seq;  
  
CREATE SEQUENCE test_seq  
start with 1  
increment by 1  
maxvalue 100;  
  
INSERT INTO board  
(idx, title)  
VALUES  
(test_seq.nextval, 'title1');  
  
INSERT INTO board2  
(idx, title)  
VALUES  
(test_seq.nextval, 'title2');  
  
SELECT * FROM board;  
SELECT * FROM board2;  
  
  
  
### 참고  
1.[SEQUENCE(시퀀스)란 무엇인가?](https://pongshowng.tistory.com/10)  
2.[오라클 시퀀스(Sequence) 사용법 총정리(생성, 조회, 수정, 삭제)등](https://coding-factory.tistory.com/420)  
3.[Oracle Sequence 만들기](https://offbyone.tistory.com/239)  