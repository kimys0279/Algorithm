'''
각 테스트 케이스 마다, 해빈이가 최종적으로 구매하려는 자동차의 가격을 한줄씩 출력한다.

예제 입력 1 
2
10000
2
1 2000
3 400
50000
0
예제 출력 1 
13200
50000'''

n = int(input())
for i in range(n):
    base = int(input())
    for j in range(int(input())):
        a, b = map(int, input().split())
        base += a*b
    print(base)
    


