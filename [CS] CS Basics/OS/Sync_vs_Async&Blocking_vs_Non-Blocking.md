# Synchronous vs Asynchronous & Blocking vs Non-Blocking



### Synchronous vs Asynchronous

Synchronous에서 'syn'은 together, 'chrono'는 time을 뜻한다. 



동기 / 비동기의 개념은 여러가지다. 

> **Synchronous/Asynchronous는 처리되는 방식의 차이다.**

**Synchronous (동기)**

- 호출하는 함수가 호출되는 함수의 작업 완료 후 리턴을 기다리거나, 또는 호출되는 함수로부터 바로 리턴 받더라도 작업 완료 여부를 호출하는 함수 스스로 계속 확인하며 신경쓰면 Synchronous다.
- 메소드 리턴시간과 결과를 전달받는 시간이 일치하면 Synchronous다.
- 순차적으로 진행하는 것도 동기다. 예를 들어 A 작업이 끝나야만 B가 시작할 수 있는 것도 동기이다. 

**Asynchronous (비동기)**

- 호출되는 함수에게 callback을 전달해서, 호출되는 함수의 작업이 완료되면 호출되는 함수가 전달받은 callback을 실행하고, 호출하는 함수는 작업 완료 여부를 신경쓰지 않으면 Asynchronous다.

<br/>

### Blocking & Non-Blocking

흔히 Synchronous  = Blocking이고 Asynchronous = Non-Blocking이라고 생각하지만 동기,비동기와는 관점이 다르다.

내가 직접 제어할 수 없는 대상을 상대하는 방법을 뜻한다. 

그래서 대상이 제한적이다. EX. I/O, 멀티쓰레드 동기화(다른 스레드의 결과 확인)

> **Blocking/NonBlocking은 호출되는 함수가 바로 리턴하느냐 마느냐가 관심사**다.

호출된 함수가 바로 리턴해서 호출한 함수에게 제어권을 넘겨주고, 호출한 함수가 다른 일을 할 수 있는 기회를 줄 수 있으면 NonBlocking이다.

그렇지 않고 호출된 함수가 자신의 작업을 모두 마칠 때까지 호출한 함수에게 제어권을 넘겨주지 않고 대기하게 만든다면 Blocking이다.

<br/>

그렇다면 이제 경우를 생각해보자.

### CASE 1 

![Imgur](http://i.imgur.com/iSafBIF.png)

위와 같은 경우는 흔히 알고 있는 개념이다. 

1. blocking되는 함수를 불렀고 Synchronous하므로 결과를 리턴할 때까지 대기한다. ex. file.read(), write()
2. Asynchronous하고 Non-Blocking한 함수를 불렀으므로 callback를 기다리며 다른 일을 수행한다. ex. nodejs

<br/>

### CASE 2. Sync + Non-Blocking

![Imgur](http://i.imgur.com/a8xZ9No.png)



자 생각해보자. Synchronous하다면 결과를 반환할 때까지 기다려야 하는 거 아닌가?

꼭 그렇지 않다. Non-Blocking 함수가 바로 제어권을 넘겨주므로 그동안 다른 일을 하지만, 계속 반환하는 지 체크하는 것이다. 

이러한 과정을 Polling이라고 하며 busy-wait이라고도 한다. 

<br/>

### CASE 3. Async + Blocking

![Imgur](http://i.imgur.com/zKF0CgK.png)

마지막은 Blocking 함수를 불렀기에 제어권이 함수에 유지되어 있고 Callback과 결과값이 같이 넘어오기에 

그동안 프로세스는 다른 일을 하지 못한다. 

<br/>

### 마무리

![img](http://wiki.sys4u.co.kr/download/attachments/7767390/Screenshot_31.png?version=1&modificationDate=1516115655000&api=v2)

추가로 I/O에서 비교해보자.



![img](https://t1.daumcdn.net/cfile/tistory/24073F3B5715D92735)

- 읽으려고 하지만 data가 없어서 data가 들어올 때까지 기다린다. 
- 처리가 끝나면 결과 값이 반환된다.



Blocking 형태의 프로그래밍을 하면 서버 입장에서는 여러 클라이언트 처리가 어렵다. 그래서 클라이언트 접속 별로 쓰레드를 생성하여 따로 I/O를 호출하는 것도 방법이지만, 이는 context switching 비용이 커서 성능이 하락한다. 

따라서 이를 해결하기 위해 Non-Blocking I/O 모델을 사용한다.

<br/>

![img](https://t1.daumcdn.net/cfile/tistory/2610A2385715D99C2B)

- System call를 호출하여 read를 하려 하지만 아직 데이터가 없기 때문에 EWOULDBLOCK을 return한다.
- application은 계속 데이터가 들어왔는지 확인한다. 
- 만약 데이터가 들어왔고 처리가 완료되면 결과 값을 반환한다.

<br/>

![img](https://t1.daumcdn.net/cfile/tistory/275A07445715DA8C01)

- Async I/O에서는 system call을 호출했지만, 바로 return한다.
- 데이터가 생기면 callback를 호출한다.



<br/><br/>

### REFERENCE

[Homoefficio.github.io](https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/)

[토비님 - 스프링캠프2017 : Async & Spring](https://www.youtube.com/watch?v=HKlUvCv9hvA&t=717s)

[SYS4U OPEN WIKI](http://wiki.sys4u.co.kr/pages/viewpage.action?pageId=7767390)

[개발자를 꿈꾸는 프로그래머](https://jwprogramming.tistory.com/33)