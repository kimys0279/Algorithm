'''
예제 입력 1 
4 8 4
1 8
4 5
6 20
9 12
예제 출력 1 
380
1번, 2번 문제의 어려운 버전을 해결해 2×140 = 280점을, 
3번 문제의 쉬운 버전을 해결해 100점을 얻어 총 380점을 얻는다.
현정이가 4문제를 풀 수 있을 정도로 대회 시간은 충분하지만, 4번 문제는 현정이에겐 너무 어려워서 풀 수 없다.
'''

import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

ans = min(hard, K) * 140
if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)    
        
        
        
    













