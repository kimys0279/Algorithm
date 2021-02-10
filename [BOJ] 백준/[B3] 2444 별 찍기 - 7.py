'''
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

예제 입력 1 
5
예제 출력 1 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i) + '*' * (2*i - 1))

for j in range(1, N):
    print(' ' * j + '*' * (2*N - (2*j + 1)))











