'''
각 테스트 케이스마다 "Case x: "를 출력한 다음, 주사위를 두 번 던져 나온 두 수의 합을 출력한다. 
테스트 케이스 번호(x)는 1부터 시작한다.

예제 입력 1 
5
1 2
1 3
3 5
2 6
3 4
예제 출력 1 
Case 1: 3
Case 2: 4
Case 3: 8
Case 4: 8
Case 5: 7'''

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print('Case {0}: {1}'.format(i+1, a+b))
