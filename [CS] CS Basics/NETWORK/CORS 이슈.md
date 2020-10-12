# CORS 이슈

<br>

CORS란?

Cross Origin Resource Sharing의 약자로 도메인 또는 포트가 다른 서버의 자원을 요청하는 매커니즘을 말한다.

<br>
<br>

CORS가 나오게 된 배경

<br>

동일 출처 정책(same-origin policy)

예전에는 같은 도메인에서 모든 요청과 응답이 이뤄지는것이 당연했기 때문에 다른 서버로 요청을 보내는것을 보안상의 이유로 요청을 주고받을수 없게 했다.

웹이 단순 문서제공이 아니라 웹애플리케이션을 만들기 시작하면서 다른 서버로 요청을 주고받아야하는 경우가 많아졌기때문에 CORS가 나오게 되었다.  

<br>
<br>

CORS 이슈

동일 출처가 아닌경우 기본정책에 따라 다른서버에 요청한 데이터를 브라우저에서 차단하기 때문에 정상적으로 데이터를 받을 수 없게 되는것이다.

프로토콜, 서브도메인, 도메인, 포트 중 하나만 달라도 동일출처가 아니다.


![Untitled](https://user-images.githubusercontent.com/37561621/85845391-23891d80-b7df-11ea-8b43-a67772d83a04.png)


<br>

해결방법

서버에서 응답헤더에 해당하는 프론트의 요청을 허용한다는 내용 넣기

```jsx
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors()); // CORS 미들웨어 추가
```

위에 처럼 미들웨어를 적용하면 모든 요청에 대해 허가를 하게 된다.
모든요청에 대해 허가하게되면 보안에 취약하기때문에 cors 미들웨어에는 여러가지 설정할 수 있다.
( [https://www.npmjs.com/package/cors](https://www.npmjs.com/package/cors) )

```jsx
const corsOptions = {
    origin: 'http://localhost:3000', // 허락하고자 하는 요청 주소
    credentials: true, // true로 하면 설정한 내용을 response 헤더에 추가
};

app.use(cors(corsOptions)); // config 추가
```

<br>

+추가

<br>

클라이언트에서 해결하는방법

<br>



1. 웹브라우저 실행 시 외부요청을 허용하는 옵션사용

크롬에서는 --disable-web-security

<br>


2. 외부요청을 가능하게 해주는 플러그인 설치

서버에서 받은 요청의 응답에 특정헤더를 추가하면 요청이 가능하기때문에

요청을 가로채서 응답에 헤더를 추가해주는 플러그인을 설치한다


<br>


이 두가지 방법은 일반사용자가 사용해야되는 웹페이지라면 적용할수없다.

<br>


3. JSONP

웹 브라우저가 css나 js같은 리소스파일은 동일출처정책에 영향받지않고 로딩이 가능하다.

이런 점을 이용해서 외부 서버에서 읽어온 js파일을 json으로 바꿔주는 편법

리소스파일을 GET메서드로 읽어오기때문에 GET방식의 API만 요청 가능하다

<br>


클라이언트에서 해결하는 방법은 공식적인 방법이 아니라서 서버에서 처리해서 응답을 보내는게 좋다


<br>


참고

https://brunch.co.kr/@adrenalinee31/1
