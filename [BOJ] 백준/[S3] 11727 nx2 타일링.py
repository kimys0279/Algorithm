'''
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
3
예제 입력 2 
8
예제 출력 2 
171'''

import sys
input = sys.stdin.readline

def sqway(n):
    a = []
    for i in range(n):
        if i >= 2:
            a.append(2*a[i-2] + a[i-1])
        elif i == 1:
            a.append(3)
        else:
            a.append(1)
    return a[n-1] % 10007

n = int(input())

print(sqway(n))


