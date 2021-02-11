'''
총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 
첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 항상 우승자가 유일한 경우만 입력으로 주어진다.

출력
첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력한다.

예제 입력 1 
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5
예제 출력 1 
4 19
'''
import sys
input = sys.stdin.readline

max = 0
max_i = 0

for i in range(1, 6):
    score_sum = sum(list(map(int, input().split())))
    if score_sum > max:
        max = score_sum
        max_i = i
print(max_i, max)








