'''
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 
그 중 최솟값을 찾는 프로그램을 작성하시오. 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 
완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

입력
첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.

출력
M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
245
64
예제 입력 2 
75
80
예제 출력 2 
-1'''

m = int(input())
n = int(input())
arr = []
i = 1

while i**2 <= n:
    if m <= i**2 <= n:
        arr.append(i**2)
    i += 1

if arr == []:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])

    
'''
시간초과코드
def findpow(a, b):
    arr = []
    for i in range(a+1, b+1):
        for j in range(b):
            if i == j**2:
                arr.append(j**2)
    if arr.count == 0:
        return print(-1)
    else:
        return print(sum(arr)), print(min(arr))
    
m = int(input())
n = int(input())
findpow(m, n)
'''
