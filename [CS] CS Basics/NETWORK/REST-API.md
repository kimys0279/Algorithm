## REST API

[0. API란?](#API란?)  
[1. REST API란?](#REST-API란?)  
[2. REST 개념](#REST-개념)  
[3. REST는 왜 필요할까](#REST는-왜-필요할까)  
[4. REST 구성](#REST-구성)  
[5. REST  조건](#REST-조건)  
[6. REST API 설계](#REST-API-설계)  
[7. REST 장단점](#REST-장단점)  
[8. REST API를 만족시켜보자](#REST-API를-만족시켜보자)  
[REFERENCE](#REFERENCE)  

<br/>


### API란?

API(Application Programming Interface)란 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다. 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스를 제공한다. ( 출처 : 위키백과)

예를 들면 구글 지도 API가 있다. 

한 상황을 가정해보자. 많은 사람들이 구글 지도를 쓰고 싶어한다. 그런데 사람들마다 제각각 다르게 자원을 요청하면 구글에선 어떻게 할까? 

요청을 일일이 보고 처리해야 한다. 매우 비효율적이다. 

그래서 사용하고 싶은 사람들한테 말한다. \'쓰고 싶으면 우리가 정한 형식대로 자원을 요청해라\' 이렇게 구글은 지도 API를 정해놓은 것이다. 

이렇게 정해놓으면 많은 사람들은 형식에 따라 자원을 요청할 테고 서버는 형식에 맞게 처리해주면 된다. 이것이 API이다.  

<br/>

### REST API란?

REST API는 REST라는 스타일을 따르는 API를 뜻한다.

그렇다면 이제 REST에 대해 알아보자.

<br/>

### REST 개념

REST(Representational State Transfer) 란

- 2000년도에 로이 필딩 (Roy Fielding)의 박사학위 논문에서 최초로 소개
-  로이 필딩은 HTTP의 주요 저자 중 한 사람으로 그 당시 웹(HTTP) 설계의 우수성에 비해 제대로 사용되어지지 못하는 모습에 안타까워하며 웹의 장점을 최대한 활용할 수 있는 아키텍처로써 REST를 발표
- 1996년부터 1999년까지 HTTP 1.0의 기존 디자인에 기반을 둔 HTTP 1.1와 병행하여 REST 구조의 스타일을 개발하였다.
-   HTTP 통신에서 자원에 대한 CRUD 요청을 Resource와 Method로 표현하여 특정한 형태로 전달하는 방식

대충 정리해보자면 HTTP을 더 잘 활용하기 위하여 나타난 새로운 스타일이다. HTTP 통신에서 사용되는 스타일이다. 

사실 개념만 들었을 때는 무슨 뜻인지 모르겠다. 더 살펴보자.

<br/>

### REST는 왜 필요할까

로이필딩은 어떠한 이유로 REST를 만들었을까? 

REST는 웹과 같은 분산 하이퍼미디어 시스템을 위한 아키텍쳐 스타일이다.

**1. 독립적 진화를 위해서**

서버와 클라이언트 각각 독립적으로 진화한다. 

예를 들어보자. 흔히 말하는 어플을 본다면 가끔씩 업데이트하라고 요청이 온다. 

그런데 업데이트를 하지 않으면 어떤 일이 발생하는가? 똑같다. 업데이트를 하지 않든 말든 어플을 사용할 순 있다. 

서버에서는 업데이트로 진화(?)했지만, 클라이언트는 그렇지 못한 것이다.

이처럼 서버의 기능이 변경되어도 클라이언트 업데이트를 할 필요가 없다.

 **다만 uniform interface을 지킨다는 조건이 붙는다.** 이전과 같은 interface로 온다면 클라이언트는 얼마든지 이해할 수 있다. 

따라서 REST를 사용한다면 독립적 진화가 가능하다.

**2. 분산 시스템을 위해서**

거대한 애플리케이션을 모듈별로 분리하기 쉬워졌다.  REST API(혹은 RESTful API)를 사용한다면 모듈, 애플리케이션 간의 통신이 가능하기 때문이다.

<br/>

### REST 구성

- **자원(Resource)** 
  - URI(Uniform Resource Identifier) : 자원의 식별자
- **행위(Verb)** 
  - HTTP METHOD (ex. GET, POST, PUT, DELETE )
- **표현(Representations)**
  - 주고받는 데이터의 형태 (ex. json, xml, text)



> URI 과 URL의 차이점은?
>
> URI(Uniform Resource Identifier)은 인터넷에 있는 자원을 나타내는 유일한 주소이다. 하위 개념으로 URL, URN이 있다.
>
> URL(Uniform Resource Locator)은 네트워크 상의 자원의 위치를 의미한다.  URL은 웹 사이트 주소뿐만 아니라 컴퓨터 네트워크상의 자원을 모두 나타낼 수 있다



> HTTP 메서드와 멱등성(Idempotent)
>
> | 메서드 | 의미   | 멱등성 |
> | ------ | ------ | ------ |
> | POST   | Create | No     |
> | GET    | Select | YES    |
> | PUT    | Update | Yes    |
> | DELETE | Delete | Yes    |
>
> 멱등성(Idempotent)란 여러 번 수행해도 결과가 같은 경우를 의미한다. 
>
> POST 연산은 리소스를 추가하기에 Idempotent하지 않지만 나머지는 반복 수행해도 Idempotent하다. (GET의 경우, 조회수 연산 기능이라면 멱등성 X)
>
> Idempotent가 중요한 이유는 REST는 개별 API를 Stateless하게 수행하게 되므로 API 호출하였다가 실패할 경우, 트랜잭션 복구를 위해서 다시 실행할 경우가 있다.
>
> Idempotent하지 않다면 기존 상태를 저장했다가 원상 복귀를 해야하고, Idempotent하다면 반복적으로 메서드를 수행해주면 된다.

<br/>

### REST  조건

로이 필딩이 제안한 REST는 6가지의 아키텍처 스타일을 지켜야 한다. 

이 사람이 꽤나 엄격한 게 optional한 Code-on-demand를 제외한 다른 조건이 하나라도 지켜지지 않다면 REST API이 아니라고 주장한다.(원작자(?)가 그렇다는데 그렇다고 해야지...)

요즘 REST API라고 불리는 건 대부분 로이필딩에 의하면 REST API이 아니라는 것이다.

그럼 어떤 조건이 있는지 살펴보자.



#### 1. Uniform Interface (유니폼 인터페이스)

Uniform Interface란, Resource(URI)에 대한 요청을 통일되고 한정적으로 수행하는 아키텍처 스타일을 의미한다. 

Rest API는 HTTP를 사용하는 모든 플랫폼에서 요청가능하다. Loosely Coupling(느슨한 결함) 형태를 갖게 되었다.

Uniform Interface에는 4가지의 조건이 있다.

**1) Resource identification in request**

- 자원을 요청할 때 URI를 사용해야 한다

**2) Resource manipulation through representations**

- 자원 추가/삭제/수정 등의 행위를 메시지에 표현을 담아서 전달해야 한다.

**3) Self descriptive message**

- API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조로 되어 있어야 한다.

이응준님이 DEVIEW 2017에서 발표하신 '그런 REST API로 괜찮은가'에서 나온 사례다.

**HTML**

```http
GET /todos HTTP/1.1
Host: example.org

HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<a href="https://todos/1">회사 가기</a>
<a href="https://todos/2">집에 가기</a>
</body>
</html>
```

클라이언트는 GET요청을 했고 서버는 200 OK라는 응답을 하며 Content를 보내준다. 그러면서 content - type이 text/html 타입이라고 알려준다.

HTML에 대한 명세는 IANA(각종 type에 대한 명세를 저장해놓은 사이트라고 보면 된다.)에 있으므로 그에 따라서 HTML 태그를 해석한다. 

그러면 HTML 파일에 대한 표현을 클라이언트가 모두 이해할 수 있다.



그렇다면 요즘 많이 쓰는 JSON파일을 보자.

**JSON**

```http
GET /todos HTTP/1.1
Host: example.org

HTTP/1.1 200 OK
Content-Type: application/json

[ 
  {"id": 1, "title": "회사 가기"},
  {"id": 2, "title": "집에 가기"}
]
```

위와 거의 동일하다. 다른 점은 Content-type이 application/json이다. 똑같이 IANA에 가서 json에 대한 명세를 찾을 것이다.

그런데 id, title는 서버에서 정한 변수일 것이다. 변수에 대한 것은 당연히 IANA에 존재하는 JSON 명세에는 없을 것이다. 

그렇다면 클라이언트는 content에 대한 해석을 할 수 없다. 그러므로 이는 self-descriptive라는 조건을 만족하지 못하는 것이다.

그렇다면 어떻게 해야 만족할 수 있을까?는 [아래](#REST-API를-만족시켜보자)를 확인.



self -descriptive를 만족시킨다면 서버나 클라이언트가 변경되더라도 오고가는 메세지는 언제나 self-descriptive하므로 언제나 해석이 가능하다

= 독립적 진화가 가능



**4) HATEOAS(Hypermedia as the engine of application state)**
애플리케이션의 상태는 hyperlink를 통해 전이되어야 한다.

이응준님이 DEVIEW 2017에서 발표하신 '그런 REST API로 괜찮은가'에서 나온 사례다.

```http
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<head></head>
<body><a href="/test">test</a></body>
</html>
```

body를 보면 test라는 링크가 걸려있다. 링크로 다른 상태로 이동할 수 있다.

```http
HTTP/1.1 200 OK
Content-Type: application/json
Link: </articles/1>; rel="previous",
      </articles/3>; rel="next;
      
{
    "title": "The second article",
    "contents": "blah blah..."
}
```

이 역시 Link라는 헤더로 다른 리소스를 가리키고 있다. 즉 하이퍼링크로 타고 상태 전이 가능.

이러한 조건을 지켜야 HATEOAS를 지킨다고 말할 수 있다.



어디서 어디로 전이가 가능한지 미리 결정되지 않는다. 어떤 상태로 전이가 완료되고 나서야 그 다음 전이될 수 있는 상태가 결정된다.

= 링크는 동적으로 변경될 수 있다.

= 독립적 진화가 가능



#### 2. Stateless (무상태성)

작업을 위한 상태정보를 따로 저장하고 관리하지 않는다. 

서버는 각각의 요청을 완전히 다른 것으로 인식하고 처리를 한다. 이전 요청이 다음 요청 처리에 연관이 되면 안된다. 

덕분에 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않음으로써 구현이 단순해진다.



#### 3. Cacheable (캐시 가능)

REST는 HTTP라는 웹 표준을 사용하므로, 웹에서 사용하는 인프라를 활용할 수 있다. 

따라서 HTTP가 가진 캐시 기능을 사용할 수 있다.



#### 4. Client - Server 구조

UI문제와 데이터 저장소의 문제를 분리하면서 UI가 다양한 플랫폼에서 활용될 수 있다.  

서버는 요청에 대한 응답만 해주면 되고,   

클라이언트는 사용자 인증, 컨텍스트 등을 관리하는 구조로 역할이 구분되기 때문에  

서로간의 의존성이 줄어든다.  



#### 5. Layered System 계층형 구조

클라이언트는 서버에 직접 연결되었는지, 중간 서버를 통해 연결되었는지를 알 수 없다. 

그러므로 REST 서버는 다중 계층으로 구성될 수 있다. 

다중 계층이 되면서 로드 밸런싱 기능, 암호화 계층을 추가할 수 있으며 Proxy, 게이트웨이와 같은 네트워크 기반의 중간 매체를 사용할 수 있다.

이는 시스템 규모 확장성을 향상시킬 수 있다.



#### 6. Code on Demand(optional)

클라이언트는 리소스에 대한 표현을 응답으로 받고 처리해야 하는데, 어떻게 처리해야 하는지에 대한 Code를 서버가 제공하는 것을 의미한다. Html에서의 javascript가 가장 대표적인 예이다.

이것은 사전 구현에 필요한 기능의 수를 줄임으로써 클라이언트를 단순화한다.  



<br/>


### REST API 설계

#### 설계 원칙

**1. URI는 정보의 자원을 표현해야 한다. (리소스명은 동사보다는 명사를 사용)**

```http
    GET /users/delete/1	(x)
```

URI는 자원을 표현하는데 중점을 두어야 한다.  

delete와 같은 행위에 대한 표현이 들어가서는 안된다.



**2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE 등)로 표현**

위의 잘못 된 URI를 HTTP Method를 통해 수정해 보자.

```http
    DELETE /users/1
```

URI에서는 행위를 없애고 HTTP Method를 이용하였다.

회원정보를 가져올 때는 GET, 회원 추가 시의 행위를 표현하고자 할 때는 POST METHOD를 사용하여 표현한다.

**회원정보를 가져오는 URI**

```http
    GET /users/show/1     (x)
    GET /users/1          (o)
```

**회원을 추가할 때**

```http
    GET /users/insert/2 (x)  - GET 메서드는 리소스 생성에 맞지 않습니다.
    POST /users/2       (o)
```

**[참고]HTTP METHOD의 알맞은 역할**

| Method | Action  | 역할                     |
| :----- | :------ | :----------------------- |
| GET    | read    | 해당 리소스를 조회       |
| POST   | create  | 리소스를 생성            |
| PUT    | replace | **리소스의 전체를 교체** |
| PATCH  | modify  | **리소스의 일부를 수정** |
| DELETE | delete  | 모든/특정 리소스를 삭제  |



#### URI 설계 주의점

**1) 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용**

```
   http://github.com/catch4/cs
```

Github 사이트에 들어가서 catch4라는 그룹에서 cs라는 repo를 요청하는 것이다.



**2) URI 마지막 문자로 슬래시(/)를 포함하지 않는다.**

URI의 모든 글자는 리소스의 유일한 식별자이므로 URI가 달라지면 지칭하는 리소스도 달라진다. 

혼동을 주지 않도록 URI 경로의 마지막에는 슬래시(/)를 사용하지 않는다.

```
    http://github.com/catch4/cs/	(x)
    http://github.com/catch4/cs		(o)
```



**3) 하이픈(-)은 URI 가독성을 높이는데 사용**

URI를 쉽게 읽고 해석하기 위해, 불가피하게 긴 URI경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.



**4) 언더바(_)는 URI에 사용하지 않는다.**

언더바는 잘 보이지 않거나 가려진다. 따라서 하이픈으로 대체한다.



**5) URI 경로에는 소문자를 사용한다.**

URI는 대문소문자에 따라 다른 리소스로 인식한다. 

RFC 3986(URI 문법 형식)은 URI 스키마와 호스트를 제외하고는 대소문자를 구별하도록 규정하기 때문이다



**6) 파일 확장자는 사용하지 않는다.**

파일 확장자는 사용하지 않는다. 

보기 안 좋고, 없애면 URI의 길이도 줄어든다. 넣을 장점이 없다는 것이다.

```
http://api.example.com/device-management/managed-devices.xml	(x)
http://api.example.com/device-management/managed-devices		(o)
```

그렇지만, API의 파일 확장자를 강조하고 싶다면, Content-type 헤더를 통해 media type를 알려주어 파일에 어떻게 접근해야 하는지를 알려주면 된다.





#### 자원 표현 방식

좀 더 명확하게 하기 위해, resource 타입을 네 가지 카테고리(document, collection, store, controller)로 나눈다. 그리고 항상 자원을 4가지 중 하나 타입으로 넣도록 해야 한다. 

**1. DOCUMENT**

document 자원은 객체 인스턴스 또는 데이터베이스 레코드와 유사한 개념이다. REST에서는 document를 collection 자원 내의 하나의 자원이라고 표현한다.

document의 상태 표현은 보통 value와 다른 자원에 연결되어 있는 link를 포함한다.

단수형 이름을 사용한다. 아래에서는 device-management, user-management가 doucment이다.

```
http://api.example.com/device-management/managed-devices/{device-id}
http://api.example.com/user-management/users/{id}
http://api.example.com/user-management/users/admin
```

**2. COLLECTION**

collection은 document의 집합이다. collection은 서버가 관리하는 resource 저장소이다.

Client은 새로운 자원을 컬렉션에 추가하길 제안할 수 있다. 그러나 새로운 resource을 생성할지 말지는 collection에 달려있다. 

collection resource는 무엇을 포함할지를 선택하며 포함되어 있는 리소스의 URI를 결정한다. 

복수형 이름을 사용한다.  users , accounts 등이 collection이다.

```
http://api.example.com/device-management/managed-devices
http://api.example.com/user-management/users
http://api.example.com/user-management/users/{id}/accounts
```

**3. STORE**

store는 client가 관리하는 resource 저장소이다. store은 api client가 resource을 넣었다 뺐다 할 수 있다. 그럼에도 새로운 URI을 생성하지 않는다. 처음에 store에 resource가 들어갔을 때 URI가 생성된다.

복수형 이름을 사용한다. playlists가 해당한다. playlist는 여러 음악을 넣었다 뺐다 할 수 있다. 

```
http://api.example.com/song-management/users/{id}/playlists
```

**4. CONTROLLER**

controller는 절차적인 개념이다. 뭔소린가 싶겠지만, 

controller resource는 매개변수와 반환값이 있는 실행 함수와 같다. 입력값과 출력값이 있는 것이다.

동사로 표현한다. 

```
http://api.example.com/cart-management/users/{id}/cart/checkout
http://api.example.com/song-management/users/{id}/playlist/play
```

<br/>

### REST 장단점

**장점**

1. 쉬운 사용
   - 메세지가 정확하여 이해하기 쉽고, 만들기도 쉽다.
2. 서버와 클라이언트의 분리
   - 서버와 클라이언트를 분리하면서 서버의 부하를 줄일 수 있다.
3. 기존 웹 인프라를 사용가능하다. HTTP를 그대로 사용하기 때문이다.



**단점**

1.   HTTP Method의 제한
     - 보통 5가지의 방법만을 사용하기에 이를 벗어난 부분은 사용하기 어렵다. ex. 메일 보내기
2.   표준의 부재
     - 공식 API가이드가 없다.  => 관리가 힘들다



<br/>

### REST API를 만족시켜보자

이응준님의 DEVIEW 2017 ['그런 REST API로 괜찮은가'](https://tv.naver.com/v/2292653/list/168686)을 참고했다. (꼭 보는 것을 추천!)

대부분의 REST API는 두 가지를 만족시키지 못한다. 따라서 두 가지를 만족시켜보자.

**Self-descriptive 만족시키기**

방법 1. Media type 정의하기

```http
GET /todos HTTP/1.1
Host: example.org

HTTP/1.1 200 OK
Content-Type: application/vnd.todos+json

[ 
  {"id": 1, "title": "회사 가기"},
  {"id": 2, "title": "집에 가기"}
]
```

Media type을 위와 같이 정의한다. 미디어 타입 문서를 작성하여 id, title에 대한 의미를 정의한다.

그리고 IANA에 미디어 타입을 등록한다. 그렇다면 명세를 찾아가서 해석 가능하다.

BUT, 매번 미디어 타입 정의해야 한다.



방법 2. Profile

```http
GET /todos HTTP/1.1
Host: example.org

HTTP/1.1 200 OK
Content-Type: application/json
Link: <https://example.org/docs/todos>; rel="profile"

[ 
  {"id": 1, "title": "회사 가기"},
  {"id": 2, "title": "집에 가기"}
]
```

id, title의 의미를 정의한 명세를 작성한다.

Link 헤더에 profile relation으로 해당 명세를 링크한다.

이제 메시지를 보는 사람은 명세를 찾아갈 수 있으므로 이 문서의 의미를 온전히 해석할 수 있다.

BUT, 클라이언트가 Link헤더(RFC 5988)와 profile(RFC 6906)을 이해해야 한다.



**HATEOAS 만족시키기**

방법 1. data로

```http
GET /todos HTTP/1.1
Host: example.org

HTTP/1.1 200 OK
Content-Type: application/json
Link: <https://example.org/docs/todos>; rel="profile"

[ 
  {
    "link": "https://example.org/todos/1",
    "title": "회사 가기"
  },
  {
    "link": "https://example.org/todos/2",
    "title": "집에 가기"
  }
]
```

data에 다양한 방법으로 하이퍼링크를 표현한다.

BUT, 링크를 표현하는 방법을 직접 정의해야 한다.



방법 2. HTTP 헤더로

```http
POST /todos HTTP/1.1
Content-Type: application/json

{
    "title": "점심 약속"
}

HTTP/1.1 204 No Content
Location: /todos/1
Link: </todos/>; rel="collection"
```

Link, Location 등의 헤더로 링크를 표현한다.

BUT, 정의된 relation만 활용한다면 표현에 한계가 있다.

<br/>

### REFERENCE

[초보개발자님의 REST API ?](https://medium.com/@dydrlaks/rest-api-3e424716bab)  
[위키백과- REST](https://ko.wikipedia.org/wiki/REST)  
[위키백과-URI,URL](https://ko.wikipedia.org/wiki/통합_자원_식별자)  
[그런 REST API로 괜찮은가 - PPT 슬라이드](http://slides.com/eungjun/rest#/)  
[그런 REST API로 괜찮은가 - DEVIEW 영상](https://tv.naver.com/v/2292653/list/168686)  

[조대협 - 대용량 아키텍처와 성능 튜닝](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9788965400950&orderClick=LAG&Kc=)

