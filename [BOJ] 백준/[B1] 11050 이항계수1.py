'''
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 
를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10'''

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)
