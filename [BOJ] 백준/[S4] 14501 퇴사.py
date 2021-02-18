'''
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. 
(1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

예제 입력 1 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
예제 출력 1 
45'''

import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
    
dp.append(0)

for i in range(n-1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i+1]
        
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])
        
print(dp[0])
    







