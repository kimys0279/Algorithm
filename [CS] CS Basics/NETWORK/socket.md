# WebSocket과 Socket.IO

![WebsocketSo1](https://d2.naver.com/content/images/2015/06/helloworld-1336-1-1.png)

기존의 HTTP 프로토콜은 서버와 클라이언트 사이의 연결이 유지되지 않는다. (connectionless) 따라서 상호작용(실시간 통신)하는 웹 서비스를 위해서는 숨겨진 프레임(Hidden Frame)을 이용한 방법이나 Long Polling, Stream 등 다양한 방법을 사용하며 복잡하고 어려운 코드로 구현했다. 그러나 이러한 방식은 브라우저가 HTTP 요청를 보내고 웹 서버가 이 요청에 대한 HTTP 응답를 보내는 단방향 메세지 교환 '규칙'을 변경하지 않고 구현한 방식이다.

> [참고] Long Polling은 수민 님이 발표하신 [여기](LongPolling.md)를 참고

<br><br>

## WebSocket

보다 쉽게 상호작용하는 웹 페이지를 만들려면 브라우저와 웹 서버 사이에 더 자유로운 양방향 메시지 송수신(bi-directional full-duplex communication)이 필요하다. 그래서 HTML5 표준 기술로 WebSocket API가 등장했다. WebSocket은 소켓을 이용하여 서버와 클라이언트 사이에서 자유롭게 데이터를 주고 받는 양방향 통신을 가능하게 한다. 즉 기존의 요청-응답 관계 방식보다 더 쉽게 데이터를 교환할 수 있다.

WebSocket을 사용하기 위해서는 아래처럼 Upgrade 헤더를 사용하여 웹 서버에 요청한다.

- Client Request

```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com
```

- Server Response

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
Sec-WebSocket-Protocol: chat
```

브라우저는 "Upgrade: websocket" 헤더 등과 함께 랜덤하게 생성한 키를 서버에 보낸다. 웹 서버는 이 키를 바탕으로 토큰을 생성한 후 브라우저에 돌려준다. 이런 과정으로 WebSocket 핸드쉐이킹이 이루어진다.

HTML5 웹소켓은 매우 유용한 기술이지만, 브라우저별로 지원하는 웹소켓 버전이 다르며 오래된 브라우저의 경우 아예 지원하지 않는다. 따라서 자바스크립트를 이용하여 브라우저에 상관없이 실시간 웹을 구현할 수 있는 Socket.IO를 좀 더 많이 사용하고 있다.

<br>

### WebSocket 예제

```js
if ('WebSocket' in window) {  
    var oSocket = new WebSocket(“ws://localhost:80”);

    // 메세지를 받았을 때
    oSocket.onmessage = function (e) { 
        console.log(e.data); 
    };

    // 소켓에 연결할 때
    oSocket.onopen = function (e) {
        console.log(“open”);
    };

    // 소켓 연결을 종료할 때
    oSocket.onclose = function (e) {
        console.log(“close”);
    };

    // 서버에 메세지를 보내고 싶을 때
    oSocket.send(“message”);
    oSocket.close();
}
```

WebSocket 프로토콜을 나타내는 ws://는 URI 스키마(Scheme)를 사용한다. 암호화 소켓은 https:// 처럼 wss://를 사용한다.

<br><br>

## Socket.io

웹소켓은 HTML5의 기술이기 때문에 오래된 버전의 웹 브라우저는 웹소켓을 지원하지 않는다. 특히 자동 업데이트가 되지 않는 익스플로러 구 버전 사용자들은 웹소켓으로 작성된 웹페이지를 볼 수 없다. 이를 해결하기 위해 나온 여러 기술 중 하나가 Socket.IO이다.

> **Socket.IO** is a library that enables real-time, bidirectional and event-based communication between the browser and the server.
>
> ![Diagram for bidirectional communication](https://socket.io/images/bidirectional-communication.png)

Socket.IO는 node.js 기반으로 만들어진 기술로, 거의 모든 웹 브라우저와 모바일 장치를 지원하는 실시간 웹 애플리케이션 지원 라이브러리이다. 100% 자바스크립트로 구현되어 있으며, WebSocket, FlashSocket, AJAX Long Polling, AJAX Multi part Streaming, IFrame, JSONP Polling 등 현존하는 대부분의 실시간 웹 기술들을 추상화해 놓았다. 다시 말해, Socket.IO는 자바스크립트를 이용하여 브라우저 종류에 상관없이 실시간 웹을 구현할 수 있도록 한 기술이다.

Socket.IO는 웹 브라우저와 웹 서버의 종류와 버전을 파악하여 가장 적합한 기술을 선택하여 사용한다. 만약 브라우저에 FlashSocket이라는 기술을 지원하는 플러그인이 설치되어 있으면 그것을 사용하고 플러그인이 없으면 AJAX Long Polling 방식을 사용하도록 하는 식이다.

![img](https://grm-project-template-bucket.s3.ap-northeast-2.amazonaws.com/lesson/les_FqloD_1533200905301/a662c719d95712ae8dd36fbda227932c187db78218c9df0e55e015f24128f688.png)

Socket.IO를 사용하려면 다음과 같이 NPM(Node Package Management)을 이용하여 Socket.IO를 웹 서버에 설치한다.

```bash
$ npm install socket.io
```

기본 예시는 아래와 같다.

- Server - index.js

```js
const content = require('fs').readFileSync(__dirname + '/index.html', 'utf8');

const httpServer = require('http').createServer((req, res) => {
  // serve the index.html file
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Content-Length', Buffer.byteLength(content));
  res.end(content);
});

const io = require('socket.io')(httpServer);

io.on('connect', socket => {
  console.log('connect');
});

httpServer.listen(3000, () => {
  console.log('go to http://localhost:3000');
});
```

- Client - index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Minimal working example</title>
</head>
<body>
    <ul id="events"></ul>

    <script src="/socket.io/socket.io.js"></script>
    <script>
        const $events = document.getElementById('events');

        const newItem = (content) => {
          const item = document.createElement('li');
          item.innerText = content;
          return item;
        };

        const socket = io();

        socket.on('connect', () => {
          $events.appendChild(newItem('connect'));
        });
    </script>
</body>
</html>
```

아래 명령어를 이용하여 server를 실행한다.

```bash
$ node index.js
```

![Minimal working example - connect event on both sides](https://socket.io/images/minimal-example-connect.gif)

<br>

### Socket.IO 예제

- 서버에서 클라이언트로 이벤트 보내기

```js
// index.js
// 서버에서 매 1초마다 'hello'라는 이벤트 이름으로 클라이언트에 보낸다.
io.on('connect', socket => {
  let counter = 0;
  setInterval(() => {
    socket.emit('hello', ++counter);
  }, 1000);
});
```

```js
// <script> in index.html
const socket = io();

socket.on('connect', () => {
  $events.appendChild(newItem('connect'));
});

socket.on('hello', (counter) => {
  $events.appendChild(newItem(`hello - ${counter}`));
});
```

![Minimal working example - server to client communication](https://socket.io/images/minimal-example-server-to-client.gif)

- 클라이언트에서 서버로 이벤트 보내기

```js
// index.js
io.on('connect', socket => {
  socket.on('hey', data => {
    console.log('hey', data);
  });
});
```

```js
// <script> in index.html
const socket = io();

socket.on('connect', () => {
  $events.appendChild(newItem('connect'));
});

// 클라이언트에서 매 1초마다 아래 메세지를 'hey' 라는 이벤트 이름으로 서버에 보낸다.
let counter = 0;
setInterval(() => {
  ++counter;
  socket.emit('hey', { counter }); // the object will be serialized for you
}, 1000);
```

![Minimal working example - client to server communication](https://socket.io/images/minimal-example-client-to-server.gif)

<br><br>

## Reference

[Naver D2 - WebSocket과 Socket.io](https://d2.naver.com/helloworld/1336)

[구름 EDU - Web Socket이란?](https://edu.goorm.io/learn/lecture/557/%ED%95%9C-%EB%88%88%EC%97%90-%EB%81%9D%EB%82%B4%EB%8A%94-node-js/lesson/174379/web-socket%EC%9D%B4%EB%9E%80)

https://html.spec.whatwg.org/multipage/web-sockets.html

https://socket.io/

[Wikipedia - WebSocket](https://en.wikipedia.org/wiki/WebSocket)

