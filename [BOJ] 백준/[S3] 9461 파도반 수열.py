'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

출력
각 테스트 케이스마다 P(N)을 출력한다.

예제 입력 1 
2
6
12
예제 출력 1 
3
16'''

import sys
input = sys.stdin.readline

s = [1, 1, 1, 2, 2]
for i in range (95):
    s.append(s[i+4]+s[i])
    
t = int(input())

for i in range(t):
    print(s[int(input()) - 1])

