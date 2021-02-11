'''
초콜릿을 쪼개다보면 초콜릿이 녹을 수 있기 때문에, 정화는 가급적이면 초콜릿을 쪼개는 횟수를 최소로 하려 한다. 
초콜릿의 크기가 주어졌을 때, 이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하는 프로그램을 작성

입력
첫째 줄에 두 정수 N, M(1≤N, M≤300)이 주어진다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
2 2
예제 출력 1 
3
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N == M:
    print(N*M - 1)
elif N > M:
    print((M-1) + (N-1)*M)
else:
    print((N-1) + (M-1)*N)








