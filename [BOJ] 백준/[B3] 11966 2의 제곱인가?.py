'''
첫째 줄에 N(1 ≤ N ≤ 230)이 주어진다.

출력
N이 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.

예제 입력 1 
1
예제 출력 1 
1
예제 입력 2 
2
예제 출력 2 
1
예제 입력 3 
3
예제 출력 3 
0
예제 입력 4 
4
예제 출력 4 
1'''


def powtwo(n):
    for i in range(31):
        if n == 2**i:
            return print('1')
    return print('0')
        
n = int(input())
powtwo(n)
