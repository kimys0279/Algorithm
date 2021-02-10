import sys
input = sys.stdin.readline

N = int(input())

hills = list(map(int, input().split()))

ans = 0
maxHill = 0
cnt = 0

for hill in hills:
    if hill > maxHill:
        maxHill = hill
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
    
print(ans)

'''
n = int(input())
a = list(map(int, input().split()))
cnt = 0
ls = []

for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            cnt += 1
        elif a[i] < a[j]:
            break
    ls.append(cnt)
print(max(ls))
'''         

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
