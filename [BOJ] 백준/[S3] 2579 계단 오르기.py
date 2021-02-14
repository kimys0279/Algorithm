import sys
input = sys.stdin.readline

n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())
    
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    
print(dp[n - 1])

'''
num = int(input())
a = []

for _ in range(num):
    a.append(int(input()))
    
def sum(n):
    if n >= 3:
        sum(n) = max(sum(n-2) + a[n], sum(n-3) + a[n-1] + a[n])
    else:
        sum(n) = a[n]
print(sum(num-1))
'''
