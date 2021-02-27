'''
입력 N이 홀수인 경우 '*'을 이용해 가로의 길이가 N인 전북대학교 심볼을 출력한다. (예제 참고)

짝수인 경우, 'I LOVE CBNU'를 출력한다.

예제 입력 1 
3
예제 출력 1 
***
 *
* *
예제 입력 2 
4
예제 출력 2 
I LOVE CBNU
예제 입력 3 
7
예제 출력 3 
*******
   *
  * *
 *   *
*     *'''

n = int(input())

if n % 2 == 0:
    print('I LOVE CBNU')
else:
    print('*' * n)
    print(' ' * (n//2) + '*')
    for i in range(1, n//2+1):
        print(' '*(n//2-i) + '*' + ' '*(2*i-1) + '*')

