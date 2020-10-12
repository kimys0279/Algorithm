# Cookie와 Session


공통점: 사용자의 정보를 기억하는데 사용

차이점: 쿠키는 클라이언트에 저장 세션은 서버에 저장


HTTP는 기본적으로 비연결지향 프로토콜(Connectionless)이기 때문에 이전 상태를 저장하지않는다.(Stateless)

웹 페이지를 연속으로 방문하는 경우 사용자의 편의를 위해서 상태를 유지해야될때 쿠키와 세션을 사용한다.

쿠키는 클라이언트의 상태 정보를 로컬에 저장해서 이전 상태를 기억할 수 있게한다. 로컬에 저장되기때문에 다른 사용자에 의해 임의로 변경이 가능해서 보안성이 낮다. 아이디 저장, 쇼핑몰 장바구니 등 저장해두어도 크게 문제없는 정보를 저장하는데 사용한다.

세션은 사용자의 정보를 서버에 저장하고 쿠키에 세션아이디를 저장해서 정보를 주고받기때문에 쿠키보다 보안성이 높다.


## 🤔QnA

Q . 캐시와 쿠키,세션의 차이점

A . 캐싱 기본 개념 : 이미 가져온 데이터나 계산된 결과값의 복사본을 저장함으로써 처리 속도를 향상시키며, 이를 통해 향후 요청을 더 빠르게 처리할 수 있다.

웹 캐시는 클라이언트가 요청하는 html, image, js, css등 리소스를 내려받아 특정 위치에 저장하고 이후 동일한 URL의 리소스 요청은 다시 내려받지 않고 내부에 저장한 파일을 사용하여 더 빠르게 서비스하기 위한것이므로 사용자의 상태를 유지하기위해 사용하는 쿠키와 세션과는 다른개념이다.


Q . 쿠키와 세션의 저장형식 차이

A . 쿠키는 Key 와 Value로 구성된 String 형태
세션은 객체로 저장된다. 

request객체를 출력해보면 쿠키는 HTTP헤더안에 이렇게 저장돼있다.

cookie: connect.sid=s%3AMtVnpaHKRHMn58UnqqZezHPdnmL_zhbJ.N6bmCChSJatxTUvXS9
Rg7t%2BIPuvkU3PUga4KBdNyfcE'

세션은 세션미들웨어가 request객체안에 세션객체를 추가해준다. 출력해보면 이렇게 저장돼있다.

Session {
	cookie:
		{ path: '/',
			_expires: null,
			originalMaxAge: null,
			httpOnly: true } }

```
var express = require('express')
var parseurl = require('parseurl')
var session = require('express-session')

var app = express()

app.use(session({
    secret: 'asadlfkj!@#!@#dfgasdg',
    resave: false,
    saveUninitialized: true
}))

app.get('/', function (req, res, next) {
    console.log(req);
    res.send(`Cookie와 Session`);
})

app.listen(3000, function () {
    console.log('3000!');
});
```
