'''
문제
두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 두 정수가 주어진다. 두 수는 백만보다 작거나 같은 양의 정수이다. 입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스마다, 첫 번째 수가 두 번째 수보다 크면 Yes를, 아니면 No를 한 줄에 하나씩 출력한다.

예제 입력 1 
1 19
4 4
23 14
0 0
예제 출력 1 
No
No
Yes


a, b = map(int, input().split())

while a != 0 and b != 0 :
  
  if a>b:
    print('Yes')
  elif a<b:
    print('No')
  a, b = map(int, input().split())
  
# elif a<b: 로 하면 안됨, else: 로 하면 됨. 이유?
'''

a, b = map(int,input().split(" ")) # 값을 입력받음

while a!=0 and b!=0: # a,b 둘다 0이 아니면 계속 반복
    if a>b:
        print("Yes")
    else:
        print("No")
    a, b = map(int,input().split(" "))  # a,b도 계속 반복적으로 받아줌
