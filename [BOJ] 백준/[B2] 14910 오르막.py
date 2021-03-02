'''
첫째 줄에 공백으로 구분된 N(1 ≤ N ≤ 1,000,000)개의 정수가 주어진다. 
입력으로 주어지는 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
비내림차순으로 나열되어 있으면 Good을 출력하고, 그렇지 않으면 Bad을 출력한다.

예제 입력 1 
7
예제 출력 1 
Good
예제 입력 2 
1 2 3 4 5
예제 출력 2 
Good'''

def cliff(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True

arr = list(map(int, input().split()))
if cliff(arr):
    print('Good')
else:
    print('Bad')

