'''
1
예제 출력 1 
*
예제 입력 2 
2
예제 출력 2 
* *
 * *
예제 입력 3 
3
예제 출력 3 
* * *
 * * *
* * *
예제 입력 4 
4
예제 출력 4 
* * * *
 * * * *
* * * *
 * * * *'''

n = int(input())

if n == 1:
    print('* ')
else:
    for i in range(n):
        if i % 2 == 0:
            print('* ' * n)
        else:
            print(' *' * n)
