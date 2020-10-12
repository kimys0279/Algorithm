# Network Flow

# Network Flow란?

그래프 이론 중 하나

**Network Flow**는 그래프가 **가중치 그래프**이면서 **방향성 그래프** 일 때 그 그래프에 존재하는 각각의 간선(Edge)에  **데이터가 얼마나 많이 흐르고 있는가를 측정**하는 알고리즘

`가중치 그래프`: 노드와 노드 사이를 잇는 간선에 가중치(비용, 거리 등의 값)이 주어진 그래프

## Network Flow 그래프 기초 정의

즉, 데이터(값)가 흘러가는 최대 유량을 표현한 그래프입니다.

`유량`: Flow

`용량`: Capacity

유량을 표현 할 수 있기 때문에 각 가선이 용량과, 흐름을 갖게 되는데 그 표현은 다음과 같습니다.

기존 그래프에서 표현되는 가중값은 다음과 같습니다. (u → v 까지의 비용은 10입니다.)
![Untitled](https://user-images.githubusercontent.com/38197077/93088114-784c7e00-f6d4-11ea-821b-9860bbeab784.png)

하지만 그래프의 간선 가중치가 각 흐름과 용량을 따로 표현해야 할 때가 있는데,

이럴 때 필요한 것이 Network Flow 입니다.

(u → v까지의 용량(전송이 가능한 최대 유량)은 10이지만 흐름(최대 유량)은 4)

![Untitled 1](https://user-images.githubusercontent.com/38197077/93088088-71be0680-f6d4-11ea-8b66-052849f5bd4f.png)

![Untitled 2](https://user-images.githubusercontent.com/38197077/93088097-74b8f700-f6d4-11ea-9156-ea8ac8e4568c.png)

출발지점 (s) 에서 도착지점 (t) 까지 가는 경우는 각 네가지가 있습니다.

1. s → v1 → v3 → t
2. s → v1 → v4 → t
3. s → v2 → v4 → t
4. s → v2 → v3 → t

각 경우마다 t까지 흘려보낼 수 있는 데이터의 양은 다른데, 그 중 

3번의 경우가 최대 Flow가 6이 되므로 s → t의 flow 값은 6입니다.

Flow로 표현된 그래프

![Untitled 3](https://user-images.githubusercontent.com/38197077/93088099-75ea2400-f6d4-11ea-8d32-d83704c43611.png)

Network Flow에서는 Capacity와 Flow양이 다르기 때문에 최대 Flow양은 바로 앞에 있는 간선 혹은 바로 다음에 있는 간선의 용량에 따라서 다를 수 있습니다. (Flow/Capacity)

### 네트워크 플로우의 3가지 특성

1. 용량의 제한 `f(u, v) ≤ c(u, v)`
당연하게도 간선의 유량은 용량보다 작거나 같다.
2. 유량의 대칭 `f(u, v) = -f(u, v)`
이 특성은 최대 유량 문제를 해결 할 때 알고리즘에서 사용되는 특성인데,
A → B로 1의 유량이 흐른다면, 역으로 B → A 로는 -1 유량이 흐를 수 있다는 것을 의미
**즉, 이미 유량을 흘려 보냈던 행위를 취소할 수 있음을 의미**
3. 유량의 보존
source, sink를 제외한 모든 정점에서는 들어오는 유량과 나가는 유량이 같다.

# Maximum Flow Problem (최대 유량 문제)

주어진 가중치 그래프에서 가능한 최대 흐름을 찾는 문제

## 최적화문제

Single Source (하나의 시작점) - Single Sink (하나의 끝점) 가 주어졌을 때

`Source`: 시작하는 부분

`Sink`: 끝나는 부분

가능한 경로들이 무수히 있고

이중에서 흐름값이 최대가 되는 경로와 최대값을 찾는 문제

기본적으로 최대 유량 문제는 단순하게 가능한 모든 경우의 수를 탐색해서 찾을 수 있다.

그 방법 중 보편적으로 사용되는 방법인 

- **Edmonds-Karp 알고리즘 (BFS)**
- **Ford-Fulkerson 알고리즘 (DFS)
조건: 모든 가중치가 유리수여야만 합니다.
그렇지 않은 경우에는 Sink에 도달하지 못할 수 있습니다. (무리수 인 경우)**

1. S → T 로 가는 **증가 경로**(Augmenting path)를 아무거나 하나 찾는다. 이 때 증가경로는 단순 경로이고, 경로상의 모든 간선에 아직 여유 용량(residual)이 남아있다. `c(u, v) - f(u, v) > 0`
2. 증가 경로 중 **차단 간선**을 찾는다. 이 간선은 경로상에서 `c(u, v) - f(u, v) > 0` 값이 최소가 될 수 있는 간선이다. 이 값을 `F`라고 한다.
3. 경로상의 모든 간선에 `F`만큼의 유량을 추가한다. 
경로상의 모든 간선에 대해 `f(u, v) += F` , `f(u, v) -= f`를 해준다.

위 과정을 더이상 증가 경로가 없을 때까지 반복

### **Edmonds-Karp 알고리즘**

다음과 같은 가중 그래프가 주어졌고, Source에서 Sink까지 최대 흘려보낼 수 있는 유량을 구해야 합니다.

먼저 그래프에 존재하는 간선에 Flow를 모두 0으로 설정

![Untitled 4](https://user-images.githubusercontent.com/38197077/93088101-7682ba80-f6d4-11ea-92cf-6ed46ff62c73.png)

이후 정해진 용량안에서 가능한 용량의 양을 반복적으로 더해줍니다.

1 → 2  → 6 → 8

차단 간선 = 3 = (3 - 0)

![Untitled 5](https://user-images.githubusercontent.com/38197077/93088104-7682ba80-f6d4-11ea-8fe7-a8eb23bae8ae.png)

1 → 3 → 6 → 8

차단간선 = 2 = (2 - 0)

![Untitled 6](https://user-images.githubusercontent.com/38197077/93088105-771b5100-f6d4-11ea-9c5e-1dfede2caf58.png)

1 → 4 → 7 → 8

차단간선 = 4 = (4 -0)

![Untitled 7](https://user-images.githubusercontent.com/38197077/93088107-771b5100-f6d4-11ea-9d20-5230dde03db8.png)

1 → 4 → 7 → 6 → 2 → 5 → 8

6 → 2 의 음의 간선의  residual capacity(0 - (-3) = 3)가 3 이 되므로 증가경로가 존재

차단간선 = 1 = (1 -0)

2 → 6으로 흐르던 유량 3 중에서 1만큼을 2 → 5로 흘려보냄

![Untitled 8](https://user-images.githubusercontent.com/38197077/93088109-77b3e780-f6d4-11ea-84a1-c2690ee28806.png)

네트워크 플로우에서 최대 유량을 구할 때는 Source에서 Sink로 가는 경우의 수의 우선순위가 따로 없으므로 갈 수 있는 경로를 순서없이 구해도된다.

```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int INF = 1000000000;

int const N = 8;
int result;
int c[N + 1][N + 1]; //용량
int f[N + 1][N + 1]; //유량
int d[N + 1]; // 방문체크
vector<int> a[N + 1];

void maxFlow(int start, int end) {
    while(1) {
        // 방문 초기화
        fill(d, d + N + 1, -1);

        // 증가 경로를 찾기 위한 BFS
        queue<int> q;
        q.push(start);
        while(!q.empty()) {
            int x = q.front();
            q.pop();
            // 인접노드 방문
            for(int i = 0; i < a[x].size(); i++) {
                int y = a[x][i];

                // 방문하지 않은 노드 중 용량이 남은 경우
                if(c[x][y] - f[x][y] > 0 && d[y] == -1) {
                    q.push(y);
                    d[y] = x;

                    // 도착지에 도달한 경우
                    if(y == end) 
                        break;
                }

            }
        }

        // 모든 경로를 찾은 뒤 루프 탈출
        if(d[end] == -1)
            break;

        int flow = INF;
        // 거꾸로 최소 유량 탐색
        for(int i = end; i != start; i = d[i]) {
            flow = min(flow, c[d[i]][i] - f[d[i]][i]);
        }

        // 최소 유량만큼 추가
        for(int i = end; i != start; i = d[i]) {
            f[d[i]][i] += flow;
            // 역방향(음의 간선) 도 고려
            f[i][d[i]] -= flow;
        }

        result += flow;
    }
}

int main() {
    a[1].push_back(2);
    a[1].push_back(3);
    a[1].push_back(4);
    c[1][2] = 3;
    c[1][3] = 4;
    c[1][4] = 5;

    a[2].push_back(5);
    a[2].push_back(6);
    c[2][5] = 1;
    c[2][6] = 3;

    a[3].push_back(6);
    c[3][6] = 2;

    a[4].push_back(7);
    c[4][7] = 7;

    a[5].push_back(8);
    c[5][8] = 3;

    a[6].push_back(8);
    c[6][8] = 5;

    a[7].push_back(6);
    a[7].push_back(8);
    c[7][6] = 1;
    c[7][8] = 4;

    maxFlow(1, 8);

    cout << result << "\n";
		// output: 10
    
    return 0;
}
```

이 외에도 다양한 방법이 있다.

![Untitled 9](https://user-images.githubusercontent.com/38197077/93088111-77b3e780-f6d4-11ea-98b6-67926efd54a3.png)

# 참고

> - [https://www.youtube.com/watch?v=EpRU971qWX4&t=908s](https://www.youtube.com/watch?v=EpRU971qWX4&t=908s)
> - [https://blog.naver.com/ndb796/221237111220](https://blog.naver.com/ndb796/221237111220)
> - [https://m.blog.naver.com/PostView.nhn?blogId=jh20s&logNo=221298145631&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=jh20s&logNo=221298145631&proxyReferer=https:%2F%2Fwww.google.com%2F)
> - [http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220804885235](http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220804885235)
