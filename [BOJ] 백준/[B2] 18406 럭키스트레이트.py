
data = input()
lenn = len(data)
sum = 0

for i in range(lenn//2):
    sum += int(data[i])

for i in range((lenn//2), lenn):
    sum -= int(data[i])
    
if sum == 0:
  print("LUCKY")
else:
  print("READY")
