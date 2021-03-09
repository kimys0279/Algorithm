'''
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61'''
m = int(input())
n = int(input())
arr = []

for i in range(m, n+1):
  count = 0
  for j in range(1, i+1):
    if i%j == 0:
      count += 1
      if count > 2:
        break
  if count == 2:
    arr.append(i)

if len(arr) != 0:
  print(sum(arr))
  print(min(arr))
else:
  print('-1')










