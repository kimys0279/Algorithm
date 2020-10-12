# Segment Tree

배열 A[1], ..., A[N]이 있을 때, 아래 문제를 생각해보자.

> [문제 1] 순서쌍 (i, j)에 대하여 A[i], ... ,A[j] 중 최솟값을 찾는 경우를 생각해보자. A[i]부터 A[j]까지 순회하면서 찾는 것이 가장 단순한 방법일 것이다. 이 경우 시간 복잡도는 O(N)이 된다. 그러나 이러한 연산이 Q개 주어지고 N과 Q의 범위가 1부터 10만이라면, 시간 복잡도가 O(NQ)이므로 오랜 시간이 걸릴 것이다.

>  [문제 2] 구간 [l, r] (l ≤ r)이 주어진다. (1) <u>A[l] + A[l+1] + ... + A[r-1] + A[r]을 구해서 출력</u>한 뒤, (2) <u>i번째 수를 v로 바꾼다</u>. 이 과정을 M번 반복한다. (1)번 과정은 O(N), (2)번 과정은 O(1)이므로 M번 수행하는 경우 시간 복잡도는 마찬가지로 O(MN + M) = O(MN)가 된다.

[문제 1]은 RMQ(Range Minimum Query), [문제 2]는 구간 합을 구하는 문제로, 세그먼트 트리를 이용해 시간적 효율성을 높일 수 있는 대표적인 문제이다. 세그먼트 트리는 저장된 자료를 적절히 전처리해 이러한 쿼리를 빠르게 대답할 수 있도록 한다. 아래에서 확인할 수 있겠지만 쿼리를 Q번 반복한다고 했을 때, 세그먼트 트리를 이용하면 위의 문제를 O(QlgN)만에 수행할 수 있다.

세그먼트 트리에서 노드들은 다음과 같은 의미를 가진다.

- 리프 노드 : 배열의 그 수 자체
- 리프 노드를 제외한 다른 노드 : 왼쪽 자식과 오른쪽 자식의 최솟값 또는 합을 저장

즉, N = 10인 경우 세그먼트 트리는 다음과 같이 나타낼 수 있다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg1.png)

리프 노드의 경우 배열 값과 똑같고, 범위가 적힌 노드의 경우, 예를 들어 5~7이라면 5, 6, 7번째의 최솟값 또는 합을 저장하고 있다는 뜻이다.

<br><br>

## 🍀 트리 만들기

세그먼트 트리는 Full binary tree에 가깝기 때문에 배열에 모든 값이 대부분 가득 차게 된다. 따라서 포인터 동적할당을 통한 트리가 아닌 배열로 트리를 만들 것이다. 배열을 이용하게 되면 어떤 노드의 인덱스가 x일 때, 왼쪽 자식의 인덱스는 2\*x, 오른쪽 자식의 인덱스는 2\*x+1이 된다. 이를 이용하기 위해 트리 배열의 인덱스 번호는 1부터 시작한다. 트리의 각 노드의 번호를 나타내면 다음과 같다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg2.png)

<br>

### 트리 배열의 크기

배열의 원소의 개수를 N이라고 했을 때,  N이 2의 제곱꼴인 경우에는 Full Binary Tree가 되므로 필요한 노드의 개수는 2\*N - 1개이다. N이 2의 제곱꼴이 아닌 경우에는 세그먼트 트리의 높이 H = ⌈lgN⌉이 되고, 필요한 배열의 크기는 2^(H+1) - 1이다.이게 귀찮다면 메모리는 좀 낭비하게 되겠지만 그냥 N에 4를 곱하는 것도 한 방법이다. 4*N은 모든 경우에 우리가 필요로 하는 배열의 크기보다 크기 때문이다.

```c++
int h = (int)ceil(log2(n));
int tree_size = (1 << (h + 1));
```

<br>

### 초기화 : init

아래와 같은 과정을 거쳐서 Segment Tree를 만들 수 있다.

```cpp
// arr: 초기 배열
// tree: 세그먼트 트리
// node: 세그먼트 트리 노드 번호
// node가 담당하는 합의 범위가 start ~ end

long long init(vector<long long> &arr, vector<long long> &tree, int node, int start, int end) {
    if (start == end)	// 노드가 리프 노드인 경우
        return tree[node] = arr[start];	// 배열의 그 원소를 가져야 함
    
    int mid = (start + end) / 2;
    
    // 구간 합을 구하는 경우
    return tree[node] = init(arr, tree, node * 2, start, mid) + init(arr, tree, node * 2 + 1, mid + 1, end);
    
    // 구간의 최솟값을 구하는 경우도 비슷하게 해줄 수 있다.
    // return tree[node] = min(init(arr, tree, node * 2, start, mid), init(arr, tree, node * 2 + 1, mid + 1, end));
}
```

```cpp
init(arr, tree, 1, 0, N - 1);
```

그림으로 나타내면 다음과 같은 과정이 이루어진다.

![img](https://t1.daumcdn.net/cfile/tistory/2502C34458BF17AE2D)

<br>

### 시간 복잡도

초기화 과정에서 걸리는 시간을 생각해보면, 각 노드마다 걸리는 시간은 O(1)이니 초기화 과정에는 노드의 수와 같은 시간이 걸린다. 따라서 초기화 과정의 시간 복잡도는 O(N)이 된다.

<br><br>

## 🍀 합 찾기 : sum

구간 left, right가 주어졌을 때, 합을 찾으려면 루트부터 트리를 순회하면서 각 노드가 담당하는 구간과 left, right 사이의 관계를 살펴봐야 한다.

예를 들어, 0~9까지 합을 구하는 경우는 루트 노드 하나만으로 합을 알 수 있다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg3.png)

2~4까지 합을 구하는 경우는 다음과 같고,

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg4.png)

5~8까지 합을 구하는 경우는 다음과 같다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg5.png)

3~9까지 합을 구하는 경우는 다음과 같을 것이다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg6.png)

노드가 담당하고 있는 구간이 `[start, end]`이고, 합을 구해야하는 구간이 `[left, right]`라면 다음과 같이 4가지 경우로 나눠서 생각할 수 있다.

1. `[left,right]`와 `[start,end]`가 겹치지 않는 경우 : 교집합이 공집합인 경우
2. `[left,right]`가 `[start,end]`를 완전히 포함하는 경우 : 교집합이 `[start, end]`인 경우
3. `[start,end]`가 `[left,right]`를 완전히 포함하는 경우 : 교집합이 `[left, right]`인 경우
4. `[left,right]`와 `[start,end]`가 겹쳐져 있는 경우 (1, 2, 3 제외한 나머지 경우)

```cpp
long long sum(vector<long long> &tree, int node, int start, int end, int left, int right) {
    // case 1: [start, end] 앞 뒤에 [left, right]가 있는 경우,
    // 겹치지 않기 때문에 탐색을 더 이상 할 필요가 없다.
    if (left > end || right < start) return INT_MAX;
    
    // case 2: [start, end]가 [left, right]에 포함
    if (left <= start && end <= right) return tree[node];
    
    // case 3, 4: 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색 시작
    int mid = (start + end) / 2;
    return sum(tree, node*2, start, mid, left, right) + sum(tree, node*2+1, mid+1, end, left, right);
}
```

아래 트리에서 8~11의 구간합을 구하고 싶다고 가정하자.

![img](https://t1.daumcdn.net/cfile/tistory/2219B13558BF246E06)

먼저, 루트의 오른쪽 자식인 0~5는 범위와 관련 없기 때문에 (case 1) 바로 `return` 할 것이다. 왼쪽 트리로 넘어가서 탐색을 계속 하는데, 6~7도 관련이 없으므로 바로 `return`을 하고, 8은 case 2에 해당하므로 `return 2`를 한다. 9~11 노드 또한 구간에 포함되는 노드기 때문에 `return 14`를 하고 최종적으로 2와 14를 더한 16을 리턴한다.

![img](https://t1.daumcdn.net/cfile/tistory/262ADA3F58BF297C04)

<br>

### 시간 복잡도

잘 생각해보면 양쪽 재귀 호출 중 하나라도 곧장 종료하지 않고 탐색을 계속 하기 위해서는 양쪽 두 구간 모두가 겹쳐야 하는데, 이 경우는 두 번 이상 발생할 수 없다. 트리의 바닥까지 최대 두 번만 탐색하므로, 전체 시간 복잡도는 O(lgN)이다.

<br><br>

## 🍀 수 변경하기 : update

중간에 어떤 수를 변경한다면, 그 숫자가 포함된 구간을 담당하는 노드를 모두 변경해줘야 한다. 갱신 과정은 `init()`과 `sum()`를 합친 것 처럼 구현된다.

다음은 3번째 수를 변경할 때, 변경해야 하는 구간이다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg7.png)

다음 그림은 5를 변경할 때이다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/seg8.png)

`index`번째 수를 `val`로 변경한다면, 그 수가 얼마만큼 변했는지를 알아야 한다. 이 수를 `diff`라고 하면, `diff = val - a[index]`로 쉽게 구할 수 있다.

수 변경은 다음과 같은 2가지 경우가 있다.

1. `[start, end]`에 `index`가 포함되는 경우
2. `[start, end]`에 `index`가 포함되지 않는 경우

node의 구간에 포함되는 경우, `diff`만큼 증가시켜 합을 변경해줄 수 있다. 포함되니 않는 경우는 탐색을 중간하면 된다.

```cpp
void update(vector<long long> &tree, int node, int start, int end, int index, long long diff) {
    if (index < start || index > end) return;	// case 2
    tree[node] = tree[node] + diff;	// case 1
    
    // 리프 노드가 아닌 경우 자식도 변경해줘야 하기 때문에,
    // 리프 노드인지 검사를 하고 아래 자식 노드를 갱신해준다.
    if (start != end) {
        int mid = (start + end) / 2;
        update(tree,node*2, start, mid, index, diff);
        update(tree,node*2+1, mid+1, end, index, diff);
    }
}
```

```cpp
update(tree, 1, 0, N-1, index, diff);
```

<br>

### 시간 복잡도

원래 배열의 `index` 위치를 포합하는 구간은 트리에서 lgN개 있을 것이며, 이들만을 재계산하면 되기 때문에 O(lgN)만에 구간 트리를 갱신할 수 있다.

<br><br>

## 추천 문제

[Platinum 5] [2042. 구간 합 구하기](https://www.acmicpc.net/problem/2042), [10868. 최솟값](https://www.acmicpc.net/problem/10868), [2357. 최솟값과 최댓값](https://www.acmicpc.net/problem/2357), [11505. 구간 곱 구하기](https://www.acmicpc.net/problem/11505)

[Platinum 4] [2243. 사탕상자](https://www.acmicpc.net/problem/2243)

[Platinum 3] [1395. 스위치](https://www.acmicpc.net/problem/1395)

[Platinum 2] [2336. 굉장한 학생](https://www.acmicpc.net/problem/2336)

<br>

## Reference

프로그래밍 대회에서 배우는 알고리즘 문제해결전략 2 (2018, 구종만 저)

[BOJ 블로그 - 세그먼트 트리 (Segment Tree)](https://www.acmicpc.net/blog/view/9)

[Crocus - 세그먼트 트리(Segment Tree)](https://www.crocus.co.kr/648)

[안경잡이개발자 - 41. 세그먼트 트리(Segment Tree)](https://m.blog.naver.com/ndb796/221282210534)
