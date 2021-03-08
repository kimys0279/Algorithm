'''
첫째 줄에 테스트 케이스의 수 (< 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.

출력
각 테스트 케이스마다 n을 만드는 쌍을 사전순으로 출력한다. n을 만드는 쌍이 없는 경우에는 
아무것도 출력하지 않는다.

예제 입력 1 
4
2
3
4
5
예제 출력 1 
Pairs for 2:
Pairs for 3: 1 2
Pairs for 4: 1 3
Pairs for 5: 1 4, 2 3'''

n = int(input())
for _ in range(n):
    arr, num = [], int(input())
    for i in range(1, num):
        for j in range(i, num):
            if (i != j and i < j and i+j == num):
                arr.append('{} {}'.format(i, j))
    print('Pairs for {}: {}'.format(num, ', '.join(arr)))

