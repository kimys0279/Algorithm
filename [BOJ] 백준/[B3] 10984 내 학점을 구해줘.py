'''
첫 번째 줄에 학기의 수 T가 주어진다. 두 번째 줄부터 T개 학기에 대한 정보가 주어진다.
각 학기에 대한 정보는 다음과 같이 구성되어 있다. 첫 번째 줄에 들었던 과목의 수 N이 주어지고, 
다음 N개 줄에 걸쳐서 N개 과목들의 학점 C와 성적 G가 주어진다. (1 ≤ N ≤ 10, 1 ≤ C ≤ 6, C는 정수) 
G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나이며 
소수 부분은 최대 한 자리까지 주어진다.

출력
각 학기에 대해 근우의 총 학점과 평점(GPA)을 출력한다. 정답과의 절대 오차는 10-1까지 허용한다.

예제 입력 1 
2
4
3 4.3
2 2.0
4 0.0
2 4.0
3
4 0.0
4 0.0
3 0.0
예제 출력 1 
11 2.3
11 0.0'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    credit = 0
    score = 0
    for _ in range(n):
        x, y = map(float, input().split())
        credit += x
        score += x * y
    gpa = score / credit
    print(int(credit), '%.1f' %gpa)
