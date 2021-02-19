'''
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

예제 입력 1 
1 2 3 4 5 6 7 8
예제 출력 1 
ascending
예제 입력 2 
8 7 6 5 4 3 2 1
예제 출력 2 
descending
예제 입력 3 
8 1 7 2 6 3 5 4
예제 출력 3 
mixed'''

a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse = True):
    print('descending')
else:
    print('mixed')
    
