# DNS

```
$ dig google.com 
$ nslookup google.com 
$ nslookup redhat.com 8.8.8.8 # redhat.com 을 8.8.8.8 DNS서버에 질의 한다.
```

아래 웹사이트 형식의 googleapp에서 지원하는 dig\
서비스도 있다.
https://toolbox.googleapps.com/apps/dig/

## DNS 과정 (Linux 기준)


[www.google.com](http://www.google.com) 으로 DNS 질의를 한다고 가정한다.

1. Client local pc에 `/etc/hosts` 에 해당 DNS의 IP 정보가 등록되어 있는지 확인한다.
2. local pc에 DNS가 cache 되어있는지 확인한다.
(linux는 OS 레이어에서 따로 로컬에서 dns cache를 하지 않는 것 같다.)
(systemd를 사용하는 linux에서는 OS 수준의 DNS 캐싱이 거의 없고, nscd, dnsmasq 라는 프로세스가 돌고 있으면, 캐시할 수도 있는 것 같다. nscd는 `/var/cache/nscd/hosts` 에 캐시되고, dnsmasq는 하드웨어 메모리에 DNS를 캐시한다고 한다.)
- 캐시를 한다. strace, ptrace 둘 중 하나로 ping 해보면 어떤 걸 참조하는지 볼 수 있다. 그래서 사실은 /etc/hosts를 보기 전에 이 정보를 먼저 본다. (strace로 프로세스가 어떤걸 참조하는지 순서를 볼 수 있다)
3. `/etc/resolv.conf` 에 등록되어있는 네임서버(local DNS, ISPDNS) 에 DNS를 질의한다. ( 저는 8.8.8.8 Google NS를 사용한다고 가정하겠습니다.)
4. local DNS에 질의받은 DNS가 캐시되어 있는지 확인한다.
5. ROOT 네임서버에 [www.google.com](http://www.google.com)에 대한 IP정보를 가지고 있는지 확인한다. 없으면 역트리 구조로 되어있는 www.google.com dns 중 com에 해당하는 NS 정보를 가져오고 com NS 에게 www.google.com에 대한 정보가 있는지 확인한다.
- 실제로는 ROOT NS로 바로 질의하는게 아니라, gTLD(com) 로 질의를 먼저 함 
- ROOT NS는 [a.root-servers.net](http://a.root-servers.net) 이라는 DNS를 가지고 있고, a~? 까지 전세계에 총 13개의 NS를 가지고 있다.
6. com NS 또한 [www.google.com](http://www.google.com) IP정보가 있는지 확인하고, 역으로 google.com  서브도메인에 대한 google.com NS에게 IP정보를 묻는다.
7. [google.com](http://google.com) NS가 마침내 [www.google.com](http://www.google.com)의 IP(A record) 정보를 가지고 있는게 확인이 되면 최초 요청했던 NS(8.8.8.8) 에게 www.google.com의 IP 주소를 응답하고 캐시한다.  




![NS 트리구조](https://3.bp.blogspot.com/_w9eymytxILM/TOPE_AZVDGI/AAAAAAAAABw/KmoHeeX4N2w/s400/dns-hierarchy.gif)


![DNS 질의 과정 이미지화](https://user-images.githubusercontent.com/38197077/92390929-c43c7780-f156-11ea-9345-cbd7a6152a11.png)

DNS서버가 어떻게 구성되어 있는지?

- DNS 관련 지식
    - NS는 역할이 두개로 나뉜다. ( 캐시 NS, 정식 NS ) ISPDNS는 캐시용 NS이다.
    - 기본 DNS와 보조 DNS 둘 다에게 무조건 요청하고 먼저 응답해주는 DNS에게 질의하는 것이다.
    - DNS 질의는 애플리케이션 레이어(L7)에 있는 DNS 프로토콜을 사용한다. 
    DNS 프로토콜의 PORT 번호는 53번이다. ( TCP, UDP 둘다 사용하는데 대부분 UDP 프로토콜을 사용, 질의하는 Byte가 크면 TCP를 쓰게 된다. 그래서 방화벽 설정은 TCP, UDP 둘 다 열어줘야함 )
    - NS(Name Server)는 호스트들의 IP 정보를 가지고 있는 `Zone` File을 가지고 있다.
    Zone File은 다음과 같은 데이터를 담고 있다.
    Zone file 종류가 두개 있다. ( 역질의용 Zonefile, 두개 다 구성해줘야 한다, 역질의용 Zonefile이 있으면 예를 들어 IP로 질의 해도 DNS로 접속된다. )
    linux에서는 다음과 같은 위치에 존파일을 설정한다. `/var/named/userdomainname.com.zone`
    (위치는 정해지지 않았고 설정하기 나름이다. 존파일의 설정은 공백과 탭이 엄격하다.)
        - 도메인의 책임자가 누구인지 기록 (DNS에서는 SOA record이다.)
        보통 이메일을 넣게 되고, [admin.google.com](http://admin.google.com) 이 SOA라면 admin@google.com 으로 해석하면 된다.
        - 호스트 정보 
        레코드와 호스트 정보(host_name, record type, TTL, data 등)를 가지고 있다.
        예를 들면 www(host name), 192.168.0.2(data), A(record type) 라고 한다면 www.{domain} 의 A레코드는 192.168.0.2 이다.

        [Zone file 유형과 역할](https://www.notion.so/ae3f3272a0154c3a8ad100b3f3ccd24b)

## TLD는 어떻게 관리될까? 궁금해서 찾아본 것들

TLDs(Top level domain)

gTLD, ccTLD(국가 코드가 포함된), newTLD 같은 것들이 있다.

ICANN이란 무엇이며 gTLD와는 어떤 관계가 있나요?

ICANN(**Internet Corporation for Assigned Names and Numbers**)은 새로운 gTLD를 승인하고 등록 프로세스를 감독 및 관리하는 비영리 조직입니다. 언제든지 다른 모든 사람들처럼 기다렸다가 gTLD를 확보할 수도 있지만, 커다란 이점이 있는 몇 가지 대안을 활용할 수도 있습니다.

즉 TLD는 ICANN이란 조직에서 관리한다!

![DNS%20802ba6977d0648119003e64d21250dfc/Untitled%201.png](DNS%20802ba6977d0648119003e64d21250dfc/Untitled%201.png)

domain tree




# Q&A
- 여러 개의 서버가 한 도메인에 해당?되었을 때 어떻게 분배하나요.\
: 다수개의 A레코드를 등록해놓을 시 라운드로빈으로 DNS질의가로드밸런싱 됩니다. 한 예로 google.com의 A레코드를 살펴보겠습니다.
다음은 google.com의 A레코드에 대한 질의결과입니다. 보시는 것과 같이 다수개의 A레코드가 등록되어 있는 것을 보실 수 있습니다.
```
id 5563
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
google.com. IN A
;ANSWER
google.com. 299 IN A 64.233.185.100
google.com. 299 IN A 64.233.185.113
google.com. 299 IN A 64.233.185.138
google.com. 299 IN A 64.233.185.139
google.com. 299 IN A 64.233.185.102
google.com. 299 IN A 64.233.185.101
;AUTHORITY
;ADDITIONAL
```

- 호스트가 www가 아니더라도 DNS 질의는 같나요?\
:호스트가 다르더라도 결국엔 google.com(second level domain)의 하위도메인이므로 질의되는 흐름은 같습니다.


# 참고

> DNS 처리 과정
[https://umount.net/how_dns_working_1/](https://umount.net/how_dns_working_1/)
Linux에서 local에 cache된 DNS를 보는 방법
[https://unix.stackexchange.com/questions/28553/how-to-read-the-local-dns-cache-contents](https://unix.stackexchange.com/questions/28553/how-to-read-the-local-dns-cache-contents)
DNS Server Zone file 구성
[https://yoonperl.tistory.com/26](https://yoonperl.tistory.com/26)
DNS 서버 구축하기 [http://blog.naver.com/PostView.nhn?blogId=okaysungnam&logNo=221272065928&categoryNo=55&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search](http://blog.naver.com/PostView.nhn?blogId=okaysungnam&logNo=221272065928&categoryNo=55&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search)
