# [OS] CPU Scheduling

- CPU를 사용하려고 하는 프로세스들 사이의 우선순위를 관리하는 작업 - **자원을 어떤 프로세스에 얼마나 할당하는지** 정책을 만드는 것
- 프로세스들에게 자원을 최대한 공평하게 배분하며 처리율과 CPU 이용률을 증가시키고, 오버헤드, 응답시간(Response time / Turnaround time), 대기시간을 최소화하기 위한 기법
- **선점형 스케줄링(Preemptive Scheduling)** 과 **비선점형 스케줄링(Non-preemptive / Cooperative Scheduling)** 이 있음
- 메모리에 여러 개의 프로세스를 올려놓고(다중 프로그래밍), CPU의 가동시간을 적절히 나누어(시분할) 각각의 프로세스에게 분배하여 실행
  ![img](https://media.vlpt.us/post-images/pa324/e9880700-15a3-11ea-a2b9-311a942f152c/image.png)

<br>

> [참고] 스케줄러의 종류와 특징
>
> | 종류                                      | 특징                                                         |
> | ----------------------------------------- | ------------------------------------------------------------ |
> | 장기 스케줄러<br />(Long-term Scheduler)  | 어떤 프로세스가 시스템의 자원을 차지할 것인가를 결정해 준비(Ready) 상태 큐로 보내는 작업<br />수행 빈도가 적고 느림 |
> | 중기 스케줄러<br />(Mid-term Scheduler)   | 어떤 프로세스들이 CPU를 할당 받을 것인지 결정하는 작업<br />CPU를 할당받으려는 프로세스가 많을 경우, 프로세스를 일시 대기(Waiting)시킨 후 활성화해서 부하를 조절<br />메모리 부족 시 swap out, 메모리가 남으면 swap in 결정 |
> | 단기 스케줄러<br />(Short-term Scheduler) | 프로세스가 실행되기 위해 CPU를 할당받는 시기와 특정 프로세스를 지정하는 작업<br />자주 수행되고 빠름 |

<br>

### CPU 스케줄링이 발생하는 상황

1. 실행 상태에 있던 프로세스가 I/O 요청 등에 의해 Block 상태가 되는 경우
2. 실행 상태에 있던 프로세스가 타이머 인터럽트 발생에 의해 준비 상태로 되는 경우
3. I/O 요청으로 Block 상태에 있던 프로세스의 I/O 작업이 완료되어 인터럽트가 발생하고, 그 결과 이 프로세스의 상태가 준비 상태로 바뀌는 경우
4. CPU에서 실행 상태에 있는 프로세스가 종료되는 경우

<br>

> [참고] 프로세스의 생명주기
>
> ![img](https://t1.daumcdn.net/cfile/tistory/27033450580366160E)
>
> - 생성 (Create) : 프로세스 생성
> - 실행 (Running) : 프로세스가 프로세서를 차지하여 명령어들을 실행
> - 준비 (Ready) : 프로세스가 프로세서를 사용하고 있지는 않지만 언제든지 사용할 수 있는 상태로, CPU가 할당되기를 기다리는 중
> - 대기 (Waiting) : 프로세스가 입출력 완료, 시그널 수신 등 어떤 사건을 기다리고 있는 상태
> - 종료 (Terminated) : 프로세스 종료


<br>
<br>


## 선점형 스케줄링

- 하나의 프로세스가 CPU를 차지하고 있을 때, **우선순위가 높은 다른 프로세스가 현재 프로세스를 중단시키고** CPU를 점유하는 스케줄링 방식
- 비교적 응답이 빠르다는 장점이 있지만, 처리 시간을 예측하기 힘들고 높은 우선순위 프로세스들이 계속 들어오는 경우 오버헤드를 초래
- 실시간 응답환경, Deadline 응답환경 등 우선순위가 높은 프로세스를 빠르게 처리해야 할 경우 등에 유용

<br>

### 라운드 로빈 (Round Robin / RR)

![img](https://media.vlpt.us/post-images/pa324/aa46f8b0-15a0-11ea-8ab8-dbe6ee364b43/image.png)
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbwsAyu%2FbtqtYKVKWZO%2Fzr8z1dwh0dcHjioiwhUMIK%2Fimg.png)

![img](https://t1.daumcdn.net/cfile/tistory/99BB8E405CC6C6302D)

- 프로세스마다 같은 크기의 CPU 시간을 할당 (시간 할당량 / Time Slice / Quantum) - 보통 10 ~ 100ms 정도
- 프로세스가 할당된 시간 내에 처리 완료를 못하면 준비 큐 리스트의 가장 뒤로 보내지고, CPU는 대기 중인 다음 프로세스로 넘어감
- 균등한 CPU 점유 시간을 보장하며, 시분할 시스템을 사용

<br>

> [참고] 시분할 시스템
>
> CPU 스케줄링과 다중 프로그래밍을 이용해서 각 사용자들에게 컴퓨터 자원을 시간적으로 분할하여 사용할 수 있게 해주는 대화식 시스템

<br>

### SRT (Shortest Remaining Time First)

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FceeNYb%2FbtqtYLAlP1i%2FJ1q8Bp7y8qorIE4d7yttQk%2Fimg.png)

![img](https://t1.daumcdn.net/cfile/tistory/99EB0D405CC6C6312A)

- 가장 짧은 시간이 소요되는 프로세스를 먼저 수행
- 남은 시간이 더 짧다고 판단되는 프로세스가 준비 큐에 생기면 언제라도 프로세스가 선점됨

<br>

### 다단계 큐 (Multi Level Queue)

![img](https://media.vlpt.us/post-images/pa324/fc18cb30-15a2-11ea-934d-7b176b41c2f3/image.png)

- 작업들을 여러 종류 그룹으로 분할, 여러 개의 큐를 이용하여 상위 단계 작업이 선점
- 각 큐는 자신만의 독자적인 스케줄링을 가짐

<br>

### 다단계 피드백 큐 (Multi Level Feedback Queue)

![img](https://media.vlpt.us/post-images/pa324/07383c80-15a3-11ea-a2b9-311a942f152c/image.png)

- 입출력 위주와 CPU 위주인 프로세스의 특성에 따라 큐마다 서로 다른 CPU 시간 할당량을 부여
- FCFS(FIFO)와 라운드 로빈 기법을 혼합
- 새로운 프로세스는 높은 우선순위을 가지지만 프로세스의 실행 시간이 길어질수록 점점 낮은 우선순위 큐로 이동하며, (이 때, 우선 순위가 낮을 수록 시간 할당량을 크게 줌으로써 보완 가능) 마지막 단계에서 FCFS 방식을 적용 
- 유연성이 뛰어나며, turnaround 시간과 response time에 최적화



> [추가] 우선 순위가 높은 프로세스를 먼저 처리해야 하는데 계속 밀리면 어떡하나?
>
> 우선, 다단계 큐 알고리즘은 프로세스의 중요도에 따라 큐로 나누고 각 큐에서 다른 알고리즘을 적용해 효율을 높일 수 있는 장점이 있으나, 한 번 해당 큐에 들어가면 프로세스는 다른 큐로 이동하거나 변경되는 것이 거의 불가능하다는 단점이 있다. 즉, 스케줄링 오버헤드가 낮은 대신에 유연하지 못하다.
>
> 이것을 보완하기 위해 나온 것이 다단계 피드백 큐이다. 다단계 피드백 큐는 **CPU burst(프로세스 실행시간)와 중요도의 상관 관계**, 즉, 보통 사용자와 interactive하지 않는 background 프로세스일수록 CPU Burst가 매우 크다는 특징을 이용한 것이다. 우선 순위가 높은 큐일수록 time quantum이 작은데, 그 time quantum을 다 채웠다는 것은 CPU Burst가 큰 프로세스, 즉 우선순위가 낮은 프로세스일 가능성이 높다. time quantum을 채울수록 프로세스는 아래로 이동하게 되고, 이런 프로세스들은 대부분 사용자와 대화형으로 동작하는 것이 아니기 때문에 context switching을 하지 않고 그냥 쭉 수행시켜주는 것이 유리하므로 마지막 단계에서는 FCFS를 사용한다.
>
> 예를 들어, 우리가 크기가 매우 큰 프로그램을 다운로드 받는다고 가정하자. 그럼 대부분은 이 작업을 신경쓰지 않고 인터넷 서핑 등을 할 것이다. 이 상황에서 바로바로 처리해야 하는 일은 인터넷 서핑에서 발생하는 마우스 클릭이나 입출력 등이지, 다운로드가 아니다. 이렇게 다운로드처럼 CPU를 계속 써야하는, CPU Burst가 큰 작업을 우선순위가 낮다고 판별하고, 사용자와 대화형으로 동작하는 CPU Burst가 짧은 작업을 우선순위가 높다고 판별하는 것이 다단계 피드백 큐이다.
>
> 다단계 피드백 큐의 문제점으로는 다른 스케줄링 방식에서도 흔히 발생하는 기아 현상 (starvation)이 있다. 사용자와 interactive한, 즉, 우선 순위가 높은 프로세스가 계속 해서 들어오면 첫번째 큐의 프로세스만 계속해서 수행하고 낮은 우선순위 큐에 있는 프로세스는 순서가 밀리기 때문이다. 이 경우, 낮은 우선순위 큐에서 너무 오래 대기하는 프로세스에게 자원을 할당하는  Aging 방식을 도입해서 해결할 수 있다.

<br>
<br>


## 비선점형 스케줄링

- 한 프로세스가 CPU를 할당받으면 작업 종료 후 **CPU 반환 시까지 다른 프로세스는 PCU 점유가 불가능**한 스케줄링 방식
- 모든 프로세스에 대한 요구를 공정하게 처리할 수 있지만, 짧은 작업을 수행하는 프로세스가 긴 작업 종료 시까지 대기해야할 수도 있다. (콘베이 현상)
- 처리시간 편차가 적은 특정 프로세스 환경에 용이

<br>

### 우선순위 (Priority)

![img](https://media.vlpt.us/post-images/pa324/e820d2b0-159f-11ea-934d-7b176b41c2f3/image.png)

- 각 프로세스 별로 우선순위가 주어지고, 우선순위에 따라 CPU를 할당함
- 우선 순위가 같을 경우 FCFS
- 설정, 자원 상황 등에 따른 우선순위를 선정해 주요/긴급 프로세스에 대한 우선처리가 가능

<br>

### 기한부 (Deadline)

- 작업들이 명시된 기간이나 기한 내에 완료되도록 계획



> [추가] 설명 추가
>
> 각 프로세스마다 끝내야 하는 기간과 그에 따른 이익이 명시돼있고, 이익을 최대로 할 수 있는 알고리즘을 사용해서 구현한다. 방식이 꽤 구체적이라 [여기](http://blog.naver.com/babobigi/2204977801340)를 참고하면 쉽게 이해될 것 같다.

<br>

### FCFS (First Come First Served) / FIFO (First In First Out)

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Thread_pool.svg/400px-Thread_pool.svg.png)
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdufF6d%2FbtqtWhgy7Zl%2FBMv2BKEl9fSAF3GxFKIwjk%2Fimg.png)

![img](https://t1.daumcdn.net/cfile/tistory/99FBAB405CC6C63029)

- 프로세스가 대기 큐에 도착한 순서에 따라 CPU를 할당

<br>

### SJF (Shortest Job First)

![img](https://media.vlpt.us/post-images/pa324/7d6a5c80-159e-11ea-934d-7b176b41c2f3/image.png)
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbzYkhC%2FbtqtY8oiA3Q%2F4kZqk2gBuwj0klLXZzVUN0%2Fimg.png)

![img](https://t1.daumcdn.net/cfile/tistory/999F5B405CC6C63014)

- 프로세스가 도착하는 시점에 따라 그 당시 가장 작은 서비스 시간을 갖는 프로세스가 종료 시까지 자원 선점
- 준비 큐 작업 중 가장 짧은 작업부터 수행하므로 평균 대기시간이 최소
- CPU 요구시간이 긴 작업과 짧은 작업 간의 불평등이 심하여, CPU 요구시간이 긴 프로세스는 기아 현상 발생

<br>

> [참고] 기아 현상 (Starvation)
>
> 시스템 부하가 많아서 낮은 등급에 있는 준비 큐의 프로세스가 무한정 기다리는 현상
> 이를 해결하기 위해 오랫동안 기다린 프로세스의 우선순위를 높여주는 에이징(Aging) 기법을 사용

<br>

### HRN (Highest Response Ratio Next)

- 대기 중인 프로세스 중 현재 Response Ratio가 가장 높은 것을 선택 (Response Ratio = (대기시간 + 서비스시간) / 서비스시간)
- SJF와 Aging 기법을 합쳐 SJF의 약점인 기아 현상을 보완한 기법으로 긴 작업과 짧은 작업 간의 불평등을 완화



> [추가] HRN Gantt Chart
>
> ![운영체제 HRN 스케줄링: 비선점 응답률 계산 관련해서 | KLDP](https://kldp.org/files/aaa_6.jpg)
>
> - 위의 예시에서, P1과 P2과 들어오는 시점에는 대기하고 있는 프로세스가 없으므로 바로 실행한다.
> - P2가 끝나는 9ms에서는 P2가 수행하는 기간 동안 P3, P4, P5 세가지 프로세스가 모두 대기하게 되는데, 이때 Response Ratio를 계산해보면 P3은 (5 + 4) / 4 = 2.25, P4는 (3 + 5) / 5 = 1.6, P5는 (1 + 2) / 2 = 1.5 이므로 P3이 먼저 실행된다.
> - P3이 끝나는 13ms에서는 P4와 P5가 대기하는데, Reponse Ratio가 P4는 2.4, P5는 3.5로 더 큰 P5가 먼저 실행되고, 마지막으로 P4가 실행되는 것이다.

<br>
<br>


## References

[Wikepedia - Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))

[[IT 기술면접 준비자료] CPU 스케줄링 기법 (선점 스케줄링, 비선점 스케줄링)](https://preamtree.tistory.com/19)

[CPU 스케줄링](https://bnzn2426.tistory.com/65)

[운영체제 - CPU 스케줄링](https://velog.io/@pa324/운영체제-CPU-스케줄링)

[multilevel feedback queue 특징, 문제점](https://jhnyang.tistory.com/156)
