'''
상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 
상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 
두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
출력
첫째 줄에 상수의 대답을 출력한다.
예제 입력 1 
734 893
예제 출력 1 
437
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
def reverse(n):
    if n <= 0:
        return
    print(n%10, end = '')
    return reverse(n//10)
print(max(reverse(A), reverse(B)))
'''

a, b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))
