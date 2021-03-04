'''
A가 받은 표가 B보다 많은 경우에는 A
B가 받은 표가 A보다 많은 경우에는 B
같은 경우에는 Tie
를 출력한다.

예제 입력 1 
6
ABBABB

예제 출력 1 
B'''

n = int(input())
arr = list(str(input()))
a = b = 0
for i in range(len(arr)):
    if arr[i] == 'A':
        a += 1
    elif arr[i] == 'B':
        b += 1
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')
        
