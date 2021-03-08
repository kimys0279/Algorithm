'''
첫째 줄에 멀티탭의 개수 N이 주어진다. (1 ≤ N ≤ 500,000) 
이어서 둘째 줄부터 N개의 줄에 걸쳐 각 멀티탭이 몇 개의 플러그를 꽂을 수 있도록 되어 있는지를 나타내는 
자연수가 주어진다. 이 자연수는 1,000을 넘지 않는다.

출력
첫째 줄에 최대로 전원에 연결될 수 있는 컴퓨터의 수를 출력한다.

예제 입력 1 
3
1
1
1
예제 출력 1 
1'''
import sys
input = sys.stdin.readline

n = int(input())
num = 1

for i in range(n):
    num += int(input()) - 1

print(num)
