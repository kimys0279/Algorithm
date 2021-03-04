'''
입력
입력의 첫 줄에는 테스트 케이스의 숫자 T가 주어진다.
매 입력의 첫 줄에는 학교의 숫자 정수 N(1 ≤ N ≤ 100)이 주어진다.
이어서 N줄에 걸쳐 학교 이름 S(1 ≤ |S| ≤ 20, S는 공백없는 대소문자 알파벳 문자열)와 
해당 학교가 지난 한 해동안 소비한 술의 양 L(0 <= L <= 10,000,000)이 공백으로 구분되어 정수로 주어진다.
같은 테스트 케이스 안에서 소비한 술의 양이 같은 학교는 없다고 가정한다.

출력
각 테스트 케이스마다 한 줄에 걸쳐 술 소비가 가장 많은 학교의 이름을 출력한다.

예제 입력 1 
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000
예제 출력 1 
Korea
Korea'''

T = int(input())

for _ in range(T):
    N = int(input())
    alcohol = []
    
    for _ in range(N):
        S, L = map(str, input().split())
        alcohol.append([S,int(L)])
        
    alcohol = sorted(alcohol, key = lambda x: x[1])
    print(alcohol[-1][0])
        
