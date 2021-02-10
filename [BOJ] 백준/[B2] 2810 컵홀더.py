'''
어떤 좌석의 배치가 SLLLLSSLL일때, 컵홀더를 *로 표시하면 아래와 같다.

*S*LL*LL*S*S*LL*
위의 예에서 적어도 두 명은 컵홀더를 사용할 수 없다.

입력
첫째 줄에 좌석의 수 N이 주어진다. (1 ≤ N ≤ 50) 둘째 줄에는 좌석의 정보가 주어진다.

출력
컵을 컵홀더에 놓을 수 있는 최대 사람의 수를 출력한다.

예제 입력 1 
9
SLLLLSSLL
예제 출력 1 
7
'''

import sys
input = sys.stdin.readline
N = int(input())
member = input()

cnt = member.count('LL')

if cnt <= 1:
    print(N)
else:
    print(N - cnt + 1)












