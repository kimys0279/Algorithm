'''
임의의 3의 배수 자연수 n이 주어진다. (3 ≤ n ≤ 3000)

출력
자연수 n을 분해하는 방법의 개수를 출력하라.

예제 입력 1 
9
예제 출력 1 
1
예제 입력 2 
12
예제 출력 2 
3'''

n = int(input())

if n < 9:
    print('0')
    
else:
    n = n//3
    k = 0
    for i in range(1,n-1):
        k += i
    print(k)




