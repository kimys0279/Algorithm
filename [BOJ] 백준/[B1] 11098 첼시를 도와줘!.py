'''
첫 번째 줄에는 테스트 케이스의 개수 n이 주어진다 (n≤100). 

각 테스트 케이스의 첫 번째 줄 p는 고려해야될 선수의 수이다 (1≤p≤100).  

그 아래 p개의 줄에는 선수의 정보가 표시된다. 

각각의 줄은 선수의 가격 C 와 이름을 입력한다 (C<2*109).

모든 선수의 가격은 서로 다르다. 
선수의 이름은 20자 이하여야 하며, 사이에 공백이 있어서는 안 된다.
 

출력
각각의 테스트 케이스에서 가장 비싼 선수의 이름을 출력해야한다.

예제 입력 1 
2
3
10 Iversen
1000000 Nannskog
2000000 Ronaldinho
2
1000000 Maradona
999999 Batistuta
예제 출력 1 
Ronaldinho
Maradona'''

for _ in range(int(input())):
    max = 0
    maxName = ""
    for i in range(int(input())):
        num, name = input().split()
        num = int(num)
        if (num > max):
            max = num
            maxName = name
    print(maxName)
        







