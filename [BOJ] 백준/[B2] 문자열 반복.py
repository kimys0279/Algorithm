'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.

예제 입력 1 
2
3 ABC
5 /HTP
예제 출력 1 
AAABBBCCC
/////HHHHHTTTTTPPPPP'''

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    test_case, word = input().split()
    for j in word:
        print(j * int(test_case), end = '')
    print()




