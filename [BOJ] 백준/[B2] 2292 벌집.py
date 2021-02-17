'''
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

예제 입력 1 
13
예제 출력 1 
3

import sys
input = sys.stdin.readline

n = int(input())
a = [1]

for i in range(1, n):
    a.append(6 + a[i-1])
for i in a:
    if n <= a[i] and a > a[i-1]:
        print(i)'''


n = int(input())
cnt = 1
cnt_six = 6
count = 1
while n > cnt:
    count += 1
    cnt += cnt_six
    cnt_six += 6
print(count)






