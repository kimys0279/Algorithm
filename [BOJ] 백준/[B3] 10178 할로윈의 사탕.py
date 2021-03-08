'''
가장 첫 번째 줄에는 테스트 케이스의 수가 입력되고, \
각 테스트 케이스마다 사탕의 개수 c와 형제의 수 v가 차례대로 입력된다.

출력
출력은 예제를 보고 ”You get __ piece(s) and your dad gets __ piece(s).” 형식에 맞추어 적절하게 출력하라.

제한
1 ≤ c, v ≤ 1,000
예제 입력 1 
5
22 3
15 5
99 8
7 4
101 5
예제 출력 1 
You get 7 piece(s) and your dad gets 1 piece(s).
You get 3 piece(s) and your dad gets 0 piece(s).
You get 12 piece(s) and your dad gets 3 piece(s).
You get 1 piece(s) and your dad gets 3 piece(s).
You get 20 piece(s) and your dad gets 1 piece(s).'''

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(a//b, a%b))


