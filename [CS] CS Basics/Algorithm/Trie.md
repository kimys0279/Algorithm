# 트라이 (Trie)

우리가 여러 개의 문자열을 가지고 있을 때, **어떤 문자열이 그 문자열 중 하나인지 알아내는 방법**을 생각해보자.

단순하게 일일히 비교하는 방법이 있겠지만, 이러한 방법은 매우 비효율적이다. 최대 길이가 M인 문자열 N개의 집합에서 마찬가지로 최대 길이가 M인 문자열이 그 문자열의 집합에 포함되는지를 일일히 확인하면 최악의 경우 O(NM)의 비교 횟수가 필요하다.

이때, 문자열을 효율적으로 저장하고 탐색할 수 있는 자료구조가 <strong>트라이(Trie)</strong>다. Prefix tree, Digital search tree, Retrieval tree라고 부르기도 한다. 프레드킨이 Re<u>trie</u>val tree에서 "Trie"라는 이름을 붙였다.

트라이는 특정 문자열을 찾는 작업을 O(N)만에 해결할 수 있다. 그래서 주로 검색어 자동 완성, 사전에서 찾기, 문자열 검사 등에서 많이 사용된다. 그러나 각 노드에서 자식들에 대한 포인터들을 배열로 모두 저장하고 있기 때문에 저장 공간의 크기가 크다는 단점도 있다.

<br>

<br>

## 구조

기본적으로 K진 트리의 구조를 띠고 있다. 우리가 영어사전에서 "computer"라는 글자를 찾으려면 우선 제일 첫 글자인 `c`의 색인을 찾은 후, `u`, `m`, ... 순서대로 찾아갈 것이다. 이것을 논리적으로 컴퓨터에 적용한 구조가 바로 트라이 구조이다.

문자열의 목록이 `A`, `to`, `tea`, `ted`, `ten`, `i`, `in`, `inn`이라면 트라이는 다음과 같다.

<p><div align="center">


<img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/250px-Trie_example.svg.png">

</div></p>

루트 노드가 되는 가장 최상위 노드에는 어떠한 단어도 들어가지 않고, 루트 아래 노드부터 문자열의 접두사가 하나씩 나타나게 된다. 즉, `tea`는 `t` -> `te` -> `tea` 순으로 이루어지는데 이것은 모두 `tea`의 접두사이다. 즉, `tea`가 `te`를 포함한다는 사실도 트라이에서 알 수 있게 된다.

<br>

<br>

## 구현

구현은 크게 문자열을 트라이에 삽입하는 `Insert`와 문자열의 값을 return 하는 `Find`로 나눌 수 있다. 아래는 알파벳 대문자를 기준으로 트라이를 구현하는 방법이다.

<br>

### 🍀 Trie Struct

Trie 자료구조에 대한 전체적인 코드는 아래와 같다.

```cpp
struct Trie {
	bool finish; // 끝나는 지점을 표시해줌
	Trie* next[26]; // 26가지 알파벳에 대한 트라이
    
    // 생성자
	Trie() : finish(false) {
        memset(next, 0, sizeof(next));
    }
    
    // 소멸자
    ~Trie() {
        for (int i = 0; i < 26; i++)
            if (next[i])
                delete next[i];
    }
    
    // 트라이에 문자열 삽입
    void insert(const char* key) {
        if (*key == '\0')
            finish = true; // 문자열이 끝나는 지점일 경우 표시
        else {
            int curr = *key - 'A';
            if (next[curr] == NULL)
                next[curr] = new Trie(); // 탐색이 처음되는 지점일 경우 동적할당
            next[curr]->insert(key + 1); // 다음 문자 삽입
        }
    }
    
    // 트라이에서 문자열 찾기
    Trie* find(const char* key) {
        if (*key == '\0') return this; // 문자열이 끝나는 위치를 반환
        int curr = *key - 'A';
        if (next[curr] == NULL) return NULL; // 찾는 값이 존재하지 않음
        return next[curr]->find(key + 1); // 다음 문자를 탐색
    }
};
```

`Insert`와 `Find` 함수에 대해 좀 더 자세히 알아보자.

<br>

### 🍀 Insert

```cpp
void insert(const char* key) {
	if (*key == '\0') // 문자열 끝에 다다름
		finish = true;  
	else {
		int curr = *key - 'A';
		if (next[curr] == NULL) // 트리가 만들어져있지 않다면
			next[curr] = new Trie(); // 새로운 트리를 만든다.
        next[curr]->insert(key + 1);
    }
}
```

어떤 식으로 구현이 되는지 그림을 통해 알아보도록 하자.

1. 가장 초기 루트 노드에는 아무런 값도, 다른 노드도 존재하지 않는다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/q0ZGgXv/01.png"></div></p>

2. `ABC`부터 트라이에 삽입해보자. 아직 아무런 문자도 삽입하지 않았으므로 가장 앞의 문자인 `A`부터 시작한다.

3. 트라이는 현재 문자로 이루어진 노드가 존재한다면, 그 노드로 다음 문자열을 탐색한다.
   그러나 루트 노드에 아무런 노드가 생성되지 않았기 때문에 노드를 할당받은 후, `A`를 가리키는 노드를 생성해준다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/CMBnrL3/02.png"></div></p>

   `B`와 `C`도 마찬가지로 노드가 존재하지 않기 때문에 생성해준다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/JkK06r1/03.png"><img align="center" src="https://i.ibb.co/dm2647L/04.png"></div></p>

   

4. 그 다음 문자열을 탐색하려고 보니 문자열이 끝나서 이제 더 이상 존재하지 않는다. 이제 삽입이 끝났기 때문에 끝난 문자열이라는 것을 표시해주기 위해서 C옆에 ★을 붙여둔다. (실제 코드에서는 `finish`로 표시했다.)

   <p><div align="center"><img align="center" src="https://i.ibb.co/cth6F5t/05.png"></div></p>

5. 다음 `ABCD`를 삽입해보자. 이미 `ABC`를 삽입할 때 만들어 놓은 `A`, `B`, `C` 노드가 이미 존재한다. 이런 경우, 노드를 새로 생성하지 않고 해당 노드를 통해 다음 문자로 이동한다. 마지막 노드인 `D`는 존재하지 않기 때문에 `C`의 자식 노드로 `D`를 생성해주고, 마찬가지로 문자열이 끝났으므로 끝났다는 표시를 해준다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/jHk8ygY/06.png"></div></p>

6. 새로운 문자열인 `BCG`를 삽입해보자. 루트 노드에서 `B`로 가는 노드가 생성되어있지 않기 때문에 `B` 노드가 생성될 것이다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/JQ45ZzT/07.png"></div></p>

   그 다음 문자인 `C`로 넘어가보자. 그럼 의문이 들 수도 있다. 앞서 진행한 과정에서 `A` -> `B` -> `C`로 가는 경로가 존재하는데 똑같은 거 아닐까?

   그러나 우리가 지금 필요한 것은 루트에서 `A`, 그리고 `B`, `C` 순으로 가는 것이 아니라 루트에서 바로 `B`, 그리고 `C`로 이동하는 경로이다. 따라서, `B` 노드에도 `C` 노드가 생성된다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/1KCKVvL/08.png"></div></p>

7. 그 후, `C` 노드에서 `G` 노드로 연결된 노드가 없으므로, 노드를 생성해준 뒤 끝난 표시를 해준다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/wJ7qF5x/09.png"></div></p>

   

8. 이후, 순차적으로 `ZYX`, `BDE`를 넣어보면 아래처럼 트라이가 구성된다.

   <p><div align="center"><img align="center" src="https://i.ibb.co/dLGNmHQ/10.png"></div></p>

<br>

### 🍀 Find

```cpp
bool find(const char* key) {
    if (*key == '\0') // 문자열 끝에 다다름
        return false;
    if (finish) // 문자열이 끝남
        return true;
    int curr = *key - 'A';
    return next[curr]->find(key + 1);
}
```

위의 트리에서 `ABC`라는 문자가 잘 들어갔는지 확인해보자.

1. 첫번째 문자인 `A`가 루트 노드에서 갈 수 있는지 확인한다. `A` 문자로 가는 노드가 존재하기 때문에 다음으로 넘어간다.
2. `A` 노드에서 그 다음 문자인 `B`를 확인한다. `B` 노드가 존재하고, 마찬가지로 `B`에서 `C`까지도 갈 수 있기 때문에 넘어갈 수 있다.
3. 우리가 찾으려고 하는 문자열은 `ABC`이므로 `C`까지 확인하면 문자열이 끝난 상황이다. 문자열이 끝났다면, 현재 노드(마지막 노드)의 삽입할 때 문자열의 끝을 표시했던 것을 확인한다. `C`에 ★이 쳐져있기 때문에 `ABC` 문자열은 존재하는 것을 알 수 있다.

이번에는 `BTS`를 확인해보자.

1. 루트에서 첫번째 문자인 `B`로 가는 경로가 존재하기 때문에 다음으로 넘어간다.
2. 그러나 `B`에서 이동할 수 있는 노드 중에 `T`는 존재하지 않는다.
3. 해당 노드가 존재하지 않는다는 것으로 트라이에 삽입되지 않은 문자열이라는 사실을 바로 알 수 있다.

<br>

<br>

## 시간 복잡도와 공간 복잡도

앞서 말했듯이, 트라이는 효율적인 시간 복잡도를 가지는 대신, 메모리를 많이 차지하는 것이 치명적인 단점이다.

<br>

### 시간 복잡도

문자열의 최대 길이가 M일 때, `Find`와 `Insert` 모두 문자열의 길이(트리의 최대 높이) 내로 끝나기 때문에 <strong>O(M)</strong>의 시간 복잡도를 가지는 것을 알 수 있다.

<br>

### 공간 복잡도

위의 시간 복잡도 O(M)을 가지기 위해서는 다음 문자를 가리키는 노드가 필요하다. 예를 들어, 숫자에 대해 트라이를 만들어야 한다면 0\~9, 총 10개의 포인터 배열이 있어야하며, 알파벳 소문자에 대해 트라이를 만든다면 a\~z인 총 26개의 포인터 배열을 가지고 있어야 한다.

즉, 최종 메모리는 <strong>O(포인터의 크기 * 포인터 배열의 개수 * 트라이에 존재하는 총 노드의 개수)</strong>가 된다.

<br>

> [참고] Radix tree (Compact prefix tree)
>
> 트라이의 치명적인 단점인 공간에 대한 효율성을 최적화하기 위한 방법 중 하나이다. 아래 그림처럼 자식 노드가 하나밖에 없는 경우, 부모 노드에 모두 합치는 방식으로 필요한 메모리를 줄일 수 있다. 이 글에서는 따로 구현하는 방식은 설명하지 않는다.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Patricia_trie.svg/350px-Patricia_trie.svg.png)



## 추천 문제

[Gold 4] [전화번호 목록](https://www.acmicpc.net/problem/5052) / [생태학](https://www.acmicpc.net/problem/4358)

[Gold 2] [개미굴](https://www.acmicpc.net/problem/14725)

[Platinum 5] [Prefix와 Suffix](https://www.acmicpc.net/problem/13276)

[Platinum 3] [별다줄](https://www.acmicpc.net/problem/17365) / [휴대폰 자판](https://www.acmicpc.net/problem/5670) / [용량 부족](https://www.acmicpc.net/problem/5446)

[Platinum 2] [아름다운 이름](https://www.acmicpc.net/problem/3080) / [문자열 집합 판별](https://www.acmicpc.net/problem/9250)

<br>

<br>

## Reference

프로그래밍 대회에서 배우는 알고리즘 문제해결전략 2 (2018, 구종만 저) ~~a.k.a 종만북~~

[Wikipedia - Trie](https://en.wikipedia.org/wiki/Trie)

[Crocus - 트라이(Trie) 자료구조](https://www.crocus.co.kr/1053)

[얍문's Coding World - [ 자료구조 트라이(TRIE) ] 개념과 구현방법 (C++)](https://yabmoons.tistory.com/379)

[TWpower's Tech Blog - [Algorithm] 트라이(Trie) 개념과 기본 문제](https://twpower.github.io/187-trie-concept-and-basic-problem)
