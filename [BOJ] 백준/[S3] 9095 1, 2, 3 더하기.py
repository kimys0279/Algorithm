'''
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
'''

import sys
input = sys.stdin.readline

def make(n):
    a = [1, 2, 4]
    for i in range(3, n+1):
        a.append(a[i-1] + a[i-2] + a[i-3])
    return a[n-1]
    
T = int(input())

for j in range(T):
    b = int(input())
    print(make(b))



