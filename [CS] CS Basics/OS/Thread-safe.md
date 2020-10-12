# Thread-safe

> A data type or static method is *threadsafe* if it behaves correctly when used from multiple threads, regardless of how those threads are executed, and without demanding additional coordination from the calling code.

멀티 스레드 프로그래밍에서 일반적으로 어떤 함수나 변수, 혹은 객체가 여러 스레드로부터 동시에 접근이 이루어져도 프로그램의 실행에 문제가 없음을 뜻한다.

즉, 하나의 함수가 한 스레드로부터 호출되어 실행 중일 때, 다른 스레드가 그 함수를 호출하여 동시에 함께 실행되더라도 각 스레드에서의 함수의 수행 결과가 올바르게 나오는 것으로 정의한다.

Thread-safe하지 않은 코드는 아래와 같다.

```cpp
int num;
boolean is_even;

int inc(int n) {
    num += n;
    if (num % 2) is_even = false;
    else is_even = true;
    return num;
}
```

위 코드는 싱글 스레드 환경에서는 문제가 없지만, 멀티 스레드 환경에서는 전역 변수인 num과 is_even을 공유하기 때문에 문제를 발생시킬 소지가 있다. 이를 thread-safe하게 만들기 위해서는 critical section이라는 개념을 도입해 연산들을 serialize 해줘야 한다. 아래는 Mutex를 이용한 방법이다.

```cpp
int num;
boolean is_even;
pthread_mutex_t mutex_lock = PTHREAD_MUTEX_INITIALIZER;

int inc(int n) {
    pthread_mutex_lock(&mutex_lock);
    /* Critical Section Start */
    
    num += n;
    if (num % 2) is_even = false;
    else is_even = true;
    return num;
    
    /* Critical Section End */
	pthread_mutex_unlock(&mutex_lock);
}
```

보통 thread-safe를 달성하기 위해서

1. **Mutual Exclusion** : 공유 자원을 꼭 사용해야 하는 경우 자원의 접근을 세마포어 등의 lock으로 통제한다. 통상적으로 사용되는 방법이다.
2. **Thread Local Storage** : 각각의 스레드에서만 접근 가능한 저장소들을 사용함으로써 동시 접근을 막는다.
3. **Re-entrancy** : 어떤 함수가 한 스레드에 의해 호출되어 실행 중일 때, 다른 스레드가 그 함수를 호출하더라도 그 결과가 각각에게 바르게 주어져야 한다.
4. **Atomic Operation** : 공유 자원에 접근할 때 원자적으로 정의된 접근 방법을 사용한다.
5. **Immutable Object** 등의 방법이 제안된다.

어떤 프로그램이 thread-safe인지 아닌지 알아내는 것은 간단하지 않다. 아래는 [이 내용](http://web.mit.edu/6.005/www/fa15/classes/20-thread-safety/)을 정리한 것이다.

<br>

### 1. Confinement

데이터를 단일 스레드에서만 접근할 수 있도록 하여 변경 가능한 데이터에 대한 경쟁을 피한다. 공유 변경 가능 데이터는 경쟁 조건의 근본 원인이기 때문에 변경 가능 데이터를 *공유하지 않음*으로써 해결 가능하다.

지역 변수는 항상 Confinement하다. 각 스레드에는 자체 스택이 있고, 지역 변수는 스택에 저장되기 때문이다. 함수가 여러 번 호출되더라도 각 호출에는 고유한 변수를 가지고 있게 된다.

아래 코드를 생각해보면, computeFact 함수가 각각의 스레드에서 호출되지만 서로 영향을 미치지 않는 것을 알 수 있다.

```java
public class Factorial {

    /**
     * Computes n! and prints it on standard output.
     * @param n must be >= 0
     */
    private static void computeFact(final int n) {
        BigInteger result = new BigInteger("1");
        for (int i = 1; i <= n; ++i) {
            System.out.println("working on fact " + n);
            result = result.multiply(new BigInteger(String.valueOf(i)));
        }
        System.out.println("fact(" + n + ") = " + result);
    }

    public static void main(String[] args) {
        new Thread(new Runnable() { // create a thread using an
            public void run() {     // anonymous Runnable
                computeFact(99);
            }
        }).start();
        computeFact(100);
    }
}
```

![img](http://web.mit.edu/6.005/www/fa15/classes/20-thread-safety/figures/confinement-3.png)

<br>

지역 변수와 달리 전역 변수는 스레드 제한이 되지 않는다. 전역 변수는 하나의 스레드 만이 변수를 사용할 것이라고 명시해준다. 

```java
// This class has a race condition in it.
public class PinballSimulator {

    private static PinballSimulator simulator = null;
    // invariant: there should never be more than one PinballSimulator
    //            object created

    private PinballSimulator() {
        System.out.println("created a PinballSimulator object");
    }

    // factory method that returns the sole PinballSimulator object,
    // creating it if it doesn't exist
    public static PinballSimulator getInstance() {
        if (simulator == null) {
            simulator = new PinballSimulator();
        }
        return simulator;
    }
}
```

위 코드에서, `PinballSimulator` 클래스는 `getInstance()` 메소드에 경쟁이 있다. 두 개의 스레드가 동시에 해당 메소드를 호출하면 원하지 않는 `PinballSimulator`가 두 개 생길 수 있다. `static`을 통해 `PinballSimulator`가 하나만 존재할 수 있도록 만들고, `getInstance()`에서 `simualtor`가 존재하지 않을 때만 새로운 `PinballSimulator`를 만든다.

<br>

### 2. Immutable

공유되는 데이터라도 항상 똑같은 값이 나올 수 있도록 변경 불가능한 데이터 유형(C++의 `const`, JAVA의 `private final`)이나 참조 등을 사용한다. 데이터를 바꿀 수 있는 setter 함수도 없어야 한다.

<br>

### 3. Using Thread-safe Data Types

Java 라이브러리에는 몇몇 Thread-safe인 데이터 유형이 있다. 공유 가능하고 변경 가능한 데이터를 이런 Thread-safe한 데이터 유형에 저장해서 사용한다.

대표적으로, Java에서 `StringBuffer`와 `StringBuilder`를 생각해보자.

> *[StringBuffer is]* A **thread-safe**, mutable sequence of characters. A string buffer is like a String, but can be modified. At any point in time it contains some particular sequence of characters, but the length and content of the sequence can be changed through certain method calls.
>
> String buffers are **safe for use by multiple threads.** The methods are **synchronized** where necessary so that all the operations on any particular instance behave as if they occur in some serial order that is consistent with the order of the method calls made by each of the individual threads involved.

> *[StringBuilder is]* A mutable sequence of characters. This class provides an API compatible with StringBuffer, but **with no guarantee of synchronization**. This class is designed for use as a drop-in replacement for StringBuffer in places where the string buffer was being **used by a single thread** (as is generally the case). Where possible, it is recommended that this class be used in preference to StringBuffer as it will be faster under most implementations.

간단히 요약하자면, `StringBuffer`는 멀티 스레드 환경에서 사용하기 좋으며, 동기화가 되기 때문에 thread-safe하다. 그러나 `StringBuilder`는 싱글 스레드 환경에서 사용될 수 있으며 동기화가 이루어지지 않는다. 여기서 Thread-safe Data Type은 `StringBuffer`라고 할 수 있겠다.

`Vector`와 `Hashtable`을 제외한 Java Collection Interface 대부분은 싱글 스레드 환경에서 사용할 수 있도록 설계되어있어  `List`, `Set`, `Map`, `ArrayList`, `HashSet`, `HashMap` 등은 thread-safe하지 않다. 

멀티 스레딩 환경을 위해 자바에서는 `Collections.synchronizedXXX()` 메소드를 제공한다.

```java
List<String> list = Collections.synchronizedList(new ArrayList<String>());
private static Map<Integer,Boolean> cache = Collections.synchronizedMap(new HashMap<>());
```

위와 같이 선언하면 동기화되어 thread-safe한 리스트를 만들 수 있다. 그러나 동기화된 컬렉션은 스레드가 작업할 때 lock이 걸리기 때문에 스레드가 병렬적으로 요소들을 처리할 수 없다. 이 부분을 개선하기 위해서 java.util.concurrent 패키지에서 부분 잠금을 사용하는 ConcurrentXXX가 제공된다.

```java
Map<K,V> map = new ConcurrentHashMap<K,V>();
Queue<E> queue = new ConcurrentQueue<E>();
```

<br><br>

## Reference

[위키백과 - 스레드 안전](https://ko.wikipedia.org/wiki/스레드_안전)

[MIT - Reading 20: Thread Safety](http://web.mit.edu/6.005/www/fa15/classes/20-thread-safety/)
