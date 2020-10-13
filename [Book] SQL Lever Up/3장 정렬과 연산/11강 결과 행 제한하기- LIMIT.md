# 11강 결과 행 제한하기 - LIMIT	

> SELECT 명령에서는 결과값으로 변환되는 행을 제한할 수 있습니다.	
```	
SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명 LIMIT 행수 [OFFSET 시작행]	
```	

## 1.행수 제한	

    - LIMIT 구는 표준 SQL이 아니다.	

    - MySQL, PostgreSQL등에서 사용되는 문법이다.	

> SELECT * FROM sample33;	

| no |	
|------:|	
| 1 | 	
| 2 | 	
| 3 |	
| 4 | 	
| 5 | 	
| 6 |	
| 7 |	

> SELECT * FROM sample33 LIMIT 3;	
| no |	
|------:|	
| 1 | 	
| 2 | 	
| 3 |	

   - 정령한 후 제한하기	

     - WHERE no <= 3 vs LIMIT 3의 차이점	

       - LIMIT는 반환할 행수를 제한하는 기능으로, WHERE 구로 검색한 뒤,	

       - ORDER BY로 정렬한 뒤	

       - 최종적으로 처리 된다.	

       > SELECT * FROM sample33 ORDER BY no DESC LIMIT 3;	
| no |	
|------:|	
| 7 | 	
| 6 | 	
| 5 |	

    - 다른 데이터베이스에서는 어떻게 사용할까?	
       1. SQL Server : TOP사용	
         - LIMIT과 유사	

       2. ORACLE : ROWNUM 사용	
         - SELECT * FROM sample33 WHERE ROWNUM <= 3;	

         - ROWNUM은 클라이언트에게 결과가 반환될 때 각 행에 할당되는 행 번호	

         - ROWNUM으로 행을 제한할 경우	

            - WHERE 구로 지정하므로 정렬하기전에 처리된다.	
                -> LIMIT로 행을 제한한 경우와 결과값이 다르다.	

                > 이 문제에 대해서는 5장의 **FROM구에서 서브쿼리 사용하기**에서 다시 언급!.	
              	
 ## 2. 오프셋 지정	
     - 웹 시스템에서는 클라이언트의 브라우저를 통해 페이지 단위로 화면에 표시할 내용 처리.	
     - 대량의 데이터를 하나의 페이지에 표시하는 것은 기능적으로도 속도 측면에서 효율적이지 못한다.	
     - 일반적으로 페이지 나누기(pagination)기능을 사용한다.	

      ex) 게시판 하단 부분	

     - 위치 지정은 0부터 시작	
     - '시작할 행 -1'로 기억	

     > SELECT * FROM sample33 LIMIT 3 OFSET 3;	
     	
| no |	
|------:|	
| 4 | 	
| 5 | 	
| 6 |	

  - 4행 부터 3건의 데이터 표시!
