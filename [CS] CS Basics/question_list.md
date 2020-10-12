## OS

- [x] Process와 Thread의 차이점 

- [x] Multi-Thread에 대해 설명하시오.
  - 장점과 단점
  - 멀티 프로세스 대신 멀티 스레드를 사용하는 이유
  - CPU 코어와 스레드 생성 갯수의 관계
    - 스레드를 많이 생성할 경우 성능 하락이 있는지
  - 스레드에서 stack부분만 공유하는 이유
  
- [x] Thread-safe

- [ ] User Thread와 Kernel Thread의 차이점

- [x] Deadlock에 대해 설명하시오.
  - 교착상태(데드락, Deadlock)의 개념과 조건
  - 데드락을 방어, 회피하는 방법.
  - 은행가 알고리즘, 식사하는 철학자 문제에 대해서 설명해보세요.

- [ ] 동기화 기법의 종류와 동기화 기법을 설명해보세요.
  - 커널영역 동기화와 유저영역 동기화에 대해서 설명하고, 대표적인 기법을 설명하시오.
  - 세마포어와 뮤텍스의 차이에 대해서 설명하시오.

- [ ] Memory Hierarchy에 대해 설명하시오.

- [ ] 메모리 할당 알고리즘에 대해 설명하시오.

- [ ] 페이지 교체 알고리즘에 대해 설명하시오.

- [ ] 메모리 관리 전략에 대해 설명하시오.
  - 메모리 관리 배경
  -	단편화(Fragmentation)
  -	Paging과 Segmentation의 개념 및 차이점

- [ ] CISC, RISC의 차이점

- [ ] Context Switching에 대해 설명하시오.

- [x] CPU Scheduling에 대해 설명하시오
  -  CPU 스케줄러
  -  FCFS
  -  SJF
  -  SRT
  -  Priority scheduling
  -  RR

- [ ] 동기(sync)와 비동기(Async)의 차이점

- [ ] Virtual Memory에 대해 설명하시오.
  - 배경
  - 가상 메모리가 하는 일
  -  Demand Paging (요구 페이징)
  - 페이지 교체 알고리즘

- [x] Cache Memory에 대해 설명하시오.
  -  Locality
  -  Caching line

- [ ] 스케줄러의 종류
  - 장기 스케줄러
  - 단기 스케줄러
  - 중기 스케줄러

<br>

## NETWORK

- [ ] Frame, Packet, Segment, Datagram

- [x] OSI 7 Layer
  - OSI 7 계층 존재 이유
  
- [ ] 웹 브라우저에서 서버로 요청하면 일어나는 일련의 과정에 대해 설명하시오.

- [x] CORS 이슈

- [x] HTTP란?

- [ ] HTTP Method의 종류
   - GET, POST 방식의 차이점
   
- [x] HTTP와 HTTPS의 차이점

- [x] HTTP 1.0과 2.0의 차이점

- [x] HTTP 요청/응답 헤더

- [x] TCP-3-hands-shaking
  - TCP의 3-way-handshake와 4-way-handshake
  - 3-way-handshake와 4-way-handshake가 다른 이유
  
- [x] TCP와 UDP
  - TCP와 UDP의 차이점
  - TCP의 흐름제어와 혼잡제어
  - TCP연결이 신뢰성인 이유
  
- [ ] TCP/IP 4 Layer

- [ ] DNS의 Round Robin 방식

- [ ] Routing Table

- [x] REST API
  - REST와 RESTful의 개념
  
- [ ] UTF-8

- [ ] URL Encode

- [x] Cookie와 Session

- [x] 소켓(Socket)
  -  Socket.io와 WebSocket의 차이

<br>

## DB

- [x] 데이터베이스
  - 데이터베이스를 사용하는 이유
  - 데이터베이스 성능
  - 데이터베이스의 종류 
  
- [x] RDBMS

- [x] NoSQL
  - 정의
  - CAP 이론
    - 일관성
    - 가용성
    - 네트워크 분할 허용성
  - 저장방식에 따른 분류
    -  Key-Value Model
    -  Document Model
    -  Column Model
  
- [ ] RDBMS와 NoSQL 차이

- [x] DB 기초
  
  - PK / FK / ER모델
  
- [ ] VIEW 뷰

- [ ] UML이란

- [x] 이상현상

- [ ] DB / 개체/ 참조 무결성

- [ ] 트리거

- [ ] SQL

  - DDL 
  - DML
  - DCL
  - 서브쿼리 subquery (Inner Query)
  - GROUBY
  - WHERE / HAVING BY 차이점
  - 테이블 DROP / Truncate, Delete 차이
  - 비교조건식 / 논리조건식
  - ISNULL 조건식 / LIKE 조건식

- [ ] Join
  
  - INNER JOIN 
  - LEFT/RIGHT OUTER JOIN
  - FULL OUTER JOIN
  - CROSS JOIN
  - SELF JOIN 셀프조인
  
- [x] 정규화
  
  - 정규화 탄생 배경
  - 개념
  - 종류
  - 장단점
  - 역정규화
  
- [x] Transaction
  - 개념
  - 트랜잭션과 Lock
  - 트랜잭션의 특성
  - 트랜잭션의 상태
  - 트랜잭션을 사용할 때 주의할 점
  - 트랜잭션 격리 수준(Transaction Isolation Level)
  
- [ ] Index
  -  Index 란 무엇인가
  -  Index 의 자료구조
  -  Primary index vs Secondary index
  -  Composite index
  -  Index 의 성능과 고려해야할 사항
  
- [ ] 시퀀스

- [ ] 옵티마이저(Optimizer)란

- [ ] Replication / 파티셔닝(Partitioning) / 샤딩(Sharding)

- [ ] 객체 관계 매핑(Object-relational mapping, ORM)이란

- [ ] SQL injection

- [ ] N+1 문제

<br>

## DATA STRUCTURE / ALGORITHM

- [ ] Big-O 표기법
  
- [ ] Stack & Queue
  - 개념
  - 차이점

- [ ] ArrayList & LinkedList

- [ ] Sort
  - Selection Sort
  - Bubble Sort
  - Insertion Sort
  - Quick Sort
  - Merge Sort
  - Heap Sort
  - Topological Sort

- [ ] Tree
  -  Binary Tree
    - preorder / inorder / postorder  traversal
  -  Full Binary Tree
  -  Complete Binary Tree
  -  BST (Binary Search Tree)
  	- 평균 검색 시간 worst time & worst case
  - 그래프(Graph)와 트리(Tree)의 차이점
  
- [ ] DFS / BFS

- [ ] Back-tracking

- [ ] 우선순위 큐 (Heap)

- [ ] Hash Table
  -  Hash Function
  -  Resolve Collision
  -  Open Addressing
  -  Separate Chaining
  -  Resize

- [x] 이분 탐색

- [ ] 그리디

- [ ] 동적 계획법 (Dynamic Programming)

- [ ] Fibonacci 방식의 Recursion, Dynamic Programming, 반복 세 가지 방식에 대한 차이

- [x] Union-find (DisJoint Set)

- [ ] 최소 신장 트리 (MST)
  - Kruskal algorithm
  - Prim algorithm
  
- 최단 경로 알고리즘
  - [ ] Djikstra algorithm
  - [x] Bellman-Ford algorithm
  - [ ] Floyd-Warshall algorithm

- [x] 트라이 (Trie)

- [ ] Red-Black Tree

- [ ] B+ Tree & B- Tree

- [x] Segment Tree
  
- [x] KMP
  
<br>

## Security

- [x] 대칭키와 비대칭키
  -  대표 암호화 알고리즘
  -  차이점

- [x] SSL/TLS

- [ ] MAC

<br>

## Programming Language

- [x] 객체 지향 프로그래밍이란 무엇인가?
  - 개념
  - 특징
  - 원칙
  - 절차지향 프로그래밍과의 차이점
  
- [x] 중복함수(Overloading)와 재정의(Overriding)의 차이점

- [x] 스마트 포인터란?

- [x] 가상 함수에 대해서 설명하시오.
  - 순수 가상함수와 가상함수의 차이점에 대해서 설명하시오.
  
- [x] malloc와 new의 차이에 대해서 설명하시오.

- [ ] C와 C++의 차이점에 대해서 설명해보시오.

- [ ] Call by value와 Call by reference에 대해서 설명해보시오.

- [x] 깊은복사와 얕은 복사에 대해서 설명해보세요.

- [x] Reference와 Pointer에 대해서 설명해보세요.

- [x] Garbage Collector

<br>

## etc

- [ ] 컴퓨터 아키텍쳐
  -  32비트, 64비트 차이

- [ ] TDD 란 무엇이며 어떠한 장점이 있는가?

- [x] 함수형 프로그래밍이란?

- [ ] Git 과 GitHub 에 대해서

- [ ] 디자인 패턴의 개념과 종류
  - Singleton 패턴
  - Strategy 패턴
  - Template Method 패턴
  - Factory Method 패턴
  - MVC1 패턴과 MVC2 패턴

