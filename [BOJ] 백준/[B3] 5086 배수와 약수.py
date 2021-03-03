'''
첫 번째 숫자가 두 번째 숫자의 약수이다.
첫 번째 숫자가 두 번째 숫자의 배수이다.
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

입력
입력은 여러 테스트 케이스로 이루어져 있다. 
각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 
두 수가 같은 경우는 없다.

출력
각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 
둘 다 아니라면 neither를 출력한다.

예제 입력 1 
8 16
32 4
17 5
0 0
예제 출력 1 
factor
multiple
neither'''

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    elif b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')




