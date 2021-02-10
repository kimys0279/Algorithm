'''
첫째 줄에 N과 M이 주어진다. (1 ≤ M < N ≤ 10) 
둘째 줄에 떨어지는 사과의 개수 J가 주어진다. (1 ≤ J ≤ 20) 
다음 J개 줄에는 사과가 떨어지는 위치가 순서대로 주어진다.

출력
모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값을 출력한다.

예제 입력 1 
5 1
3
1
5
3
예제 출력 1 
6
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

start = 1
end = m
distance = 0

for i in range(j):
    p = int(input())
    
    if p < start:
        distance += (start - p)
        start = p
        end = p + m - 1
    elif p > end:
        distance += (p - end)
        end = p
        start = end - m + 1
print(distance)


    













