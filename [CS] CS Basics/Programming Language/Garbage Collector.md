# Garbage Collector

### Garbage Collector(GC)란 ?

- 메모리 관리 기법 중의 하나
- 프로그램이 동적으로 할당했던 메모리 영역 중에서 필요없게 된 영역을 해제하는 기능
    *필요없게 된 영역이란 어떤 변수도 가리키지 않게 된 영역
    즉, 주소를 잃어버려서 사용할 수 없는 메모리로
    프로그래밍 언어에서는 Danling Object, 자바에서는 Garbage라고 부른다.
- C, C++ 의 경우 수동 메모리 관리를 가정하고 설계되었기 때문에 객체를 관리하는 데 있어 메모리는 완전히 개발자의 몫이지만
Java는 GC를 제공하기 때문에 항상 background에서 데몬 쓰레드로 돌아가면서 메모리를 정리해준다.


### GC의 원리

- GC의 역할
    1. 메모리 할당
    2. 사용 중인 메모리 인식
    3. 사용하지 않는 메모리 인식

- GC를 해도 더이상 사용 가능한 메모리 영역이 없는데 계속 메모리를 할당하려고 하면 OutOfMemoryError가 발생하여 WAS가 다운될 수도 있다.
행(Hang) 즉, 서버가 요청을 처리 못하고 있는 상태가 된다.
- JVM의 메모리는 클래스 영역, 자바 스택, 힙, 네이티브 메소드 4개의 영역으로 나뉘는데, Garbage Collector에서는 힙 메모리를 다루게 된다.
즉, 자바 콜렉터가 인식하고 할당하는 자바 메모리 영역은 힙 영역이다.
    * JVM Heap
    - Young, Old, Perm 세 영역
    이 중 Perm 영역은 거의 사용되지 않는 영역으로, 클래스와 메소드 정보와 같이 자바 언어 레벨에서 사용되지 않는다.
    따라서 개발자가 고려해야 할 자바의 메모리 영역은 총 아래 4개의 영역으로 나뉜다고 볼 수 있다.
    Young (1. Eden, 2. Survivor1, 3. Survivor2), 4.Old
https://t1.daumcdn.net/cfile/tistory/267FB93758FF0CB017

### GC의 종류

    1. Minor GC : Young에서 발생하는 GC
    2. Major GC : Old, Perm 영역에서 발생하는 GC
이 두가지 GC가 어떻게 상호 작용하느냐에 따라 GC 방식에 차이가 나며, 성능에도 영향을 준다.
GC가 발생하거나 객체가 각 영역에서 다른 영역으로 이동할 때 애플리케이션의 병목이 발생하면서 성능에 영향을 주게 된다.
그래서 JVM에서는 Thread-Local Allocation Buffers(스레드 로컬 할당 버퍼)라는 것을 사용한다.
이를 통해 각 스레드별 메모리 버퍼를 사용하면 다른 스레드에 영향을 주지 않는 메모리 할당 작업이 가능하다.


### 메모리 관련 GC 튜닝을 위한 JVM 옵션

- Xms : JVM 시작 시 힙 영역의 크기
- Xmx : 최대 힙 영역 크기
- XX:NewRatio : New 영역과 Old 영역의 비율. (New 영역의 비율을 전달한다.)
- XX:NewSize : New 영역의 크기
- XX:SurvivorRatio : Eden 영역과 Survivor 영역의 비율 (Survivor 영역의 비율을 전달한다.)
https://waspro.tistory.com/340


### GC의 방식

- JDK 5.0 이상에서 지워하는 GC 방식에는 네가지가 있다.
WAS나 자바 애플리케이션 수행 시 옵션을 지정하여 선택할 수 있다.

    1. Serial Collector (시리얼 콜렉터)
    2. Parallel Collector (병렬 콜렉터)
    3. Parallel Compacting Collector (병렬 컴펙팅 콜렉터)
    4. Concurrent Mark-Sweep Collector (CMS 콜렉터)

1. Serial Collector
- Young 영역과 Old 영역이 시리얼하게(연속적으로) 처리되며 하나의 CPU를 사용한다.
- Sun에서는 이 처리를 수행할 때를 Stop-the-world라고 표현한다. 다시 말하면, 콜렉션이 수행될 때 애플리케이션 수행이 정지된다.

    1) 일단 살아있는 객체들은 Eden 영역에 있다.
    2) Eden 영역이 꽉차게 되면 To survivor 영역으로 살아있는 객체가 이동한다.
    이 때 Survivor 영역에 들어가기에 너무 큰 객체는 바로 Old 영역으로 이동한다.
    그리고 From Survivor 영역에 살아있는 객체는 To survivor 영역으로 이동한다.
    3) To Survivor 영역이 꽉 찼을 경우, Eden 영역이나 From Survivor 영역에 남아있는 객체들은 Old 영역으로 이동한다.
    이 이후) Old 영역이나 Perm 영역에 있는 객체들은 Mark-sweep-compact 콜렉션 알고리즘을 따른다.

        * Mark-sweep-compact 알고리즘
            1) Old 영역으로 이동된 객체들 중 살아있는 객체를 식별한다. (Mark)
            2) Old 영역의 객체들은 훑는 작업을 수행하여 쓰레기 객체를 식별한다. (Sweep)
            3) 필요없는 객체들을 지우고 살아있는 객체들을 한 곳으로 모은다. (Compact)

- 일반적으로 클라이언트 종류의 장비에서 많이 사용된다.
대기 시간이 많아도 크게 문제되지 않는 시스템에서 사용된다는 의미.

2. Parallel Collector
- 다른 CPU가 대기 상태로 남아 있는 것을 최소화하는 것이 목표다.
- 시리얼 콜렉터와 달리 Young영역에서의 콜렉션을 병렬로 처리한다.
- 많은 CPU를 사용하기 때문에 GC의 부하를 줄이고 애플리케이션의 처리량을 증가시킬 수 있다.
- Old 영역의 GC는 시리얼 콜렉터와 마찬가지로 Mark-sweep-compact 알고리즘을 사용한다.
https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWA820%2Fbtqw7xmxsJ1%2F80bzB068C10dKSLa3FuHNK%2Fimg.png

3. Parallel Compacting Collector
- Parallel Collector와 다른 점은 Old 영역 GC에서 새로운 알고리즘을 사용한다.
그러므로 Young 영역에 대한 GC는 병렬 콜렉터와 동일하지만, Old 영역의 GC는 다음 3단계를 거치게 된다.
    1) Mark 단계 : 매우 짧은 대기 시간으로 살아 있는 객체를 찾는 단계
    2) Sweep 단계 : 서버 수행과 동시에 살아 있는 객체에 표시를 해 놓는 단계
    3) Remark 단계 : Concurrent 표시 단계에서 표시하는 동안 변경된 객체에 대해서 다시 표시하는 단계
    4) Concurrent Sweep 단계 : 표시되어 있는 쓰레기를 정리하는 단계
- 병렬 콜렉터와 동일하게, 이 방식도 여러 CPU를 사용하는 서버에 적합하다.

4. Concurrent Mark-Sweep Collector
- low-latency-collector
- 힙 메모리 영역의 크기가 클 때 적합하다.
- Young 영역에 대한 GC는 병렬 콜렉터와 동일하다.
- Old 영역의 GC는 다음 4단계를 거친다.
    1) Mark 단계 : 매우 짧은 대기 시간으로 살아 있는 객체를 찾는 단계
    2) Sweep 단계 : 서버 수행과 동시에 살아 있는 객체에 표시를 해 놓는 단계
    3) Remark 단계 : Concurrent 표시 단계에서 표시하는 동안 변경된 객체에 대해서 다시 표시하는 단계
    4) Concurrent Sweep 단계 : 표시되어 있는 쓰레기를 정리하는 단계
- 2개 이상의 프로세서를 사용하는 서버에 적당하다. ex) 웹서버
https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbt2huS%2Fbtqw8BBPi26%2FZykotwD3D1WhFksmghb1Vk%2Fimg.png

네 종류 GC 방식에 대한 성능 및 기능 비교
https://t1.daumcdn.net/cfile/tistory/2129254758FF215238


### GC의 장점

- 유효하지 않은 포인터에 접근하지 않는다.
이미 해제된 메모리에 접근하는 버그를 말한다.
만약 이 포인터가 해제되고 새로운 값이 할당되었다면 잘못된 값을 읽어오게 된다.
- 이중 해제의 문제점이 없어진다.
이미 해제된 메모리를 또다시 해제하는 버그를 말한다.
일부 알고리즘에서는 해제된 메모리를 다시 해제하려고 시도하는 오류를 일으킬 수 있다.
- 메모리 누수가 없어진다.
더이상 필요하지 않은 메모리가 해제되지 않고 남아있는 버그를 말한다.
메모리 누수가 반복되면 메모리 고갈로 프로그램이 중단될 수 있다.


### GC의 단점

- 어떤 메모리를 해제할지 결정하는 데 비용이 든다.
객체가 필요없어지는 시점을 프로그래머가 미리 알고있는 경우에도 Garbage Collector가 메모리 해제 시점을 추적해야 하므로, 이 작업은 오버헤드가 된다.
- Garbage Collection이 일어나는 타이밍이나 점유 시간을 미리 예측하기 어렵다.
때문에 프로그램이 예측 불가능하게 일시적으로 정지할 수 있다. 실시간 시스템에 적합하지 않음.
- 할당된 메모리가 해제되는 시점을 알 수 없다.


### GC의 한계

- 어떤 방식의 Garbage Collection을 사용하든 실행 시간에 작업을 하는 이상 성능 하락을 피할 수는 없다.
- Garbage Collector가 존재하더라도 더 이상 접근이 불가능한 객체만 회수하기 때문에 메모리 누수는 발생할 수 있다.
