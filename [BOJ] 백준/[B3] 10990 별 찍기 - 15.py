'''
예제 출력 1 
*
예제 입력 2 
2
예제 출력 2 
 *
* *
예제 입력 3 
3
예제 출력 3 
  *
 * *
*   *
예제 입력 4 
4
예제 출력 4 
   *
  * *
 *   *
*     *
'''

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    if i == 1:
        print(' ' * (n-i) + '*')
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i - 3) + '*')




