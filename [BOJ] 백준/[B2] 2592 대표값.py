num=[int(input()) for _ in range(10)]

print(round(sum(num)/10))
print(max(num,key=num.count))
