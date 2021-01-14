n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)



''
C++

#include <bits/stdc++.h>

using namespace std;

int n = 1260;
int cnt;

int coinTypes[4] = {500, 100, 50, 10};

int main(void) {
    for (int i = 0; i < 4; i++) {
        cnt += n / coinTypes[i];
        n %= coinTypes[i];    
    }
    cout << cnt << '\n';
}
''
