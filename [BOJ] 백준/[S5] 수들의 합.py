s = int(input())  # 입력값을 s에 받는다
i=0
sum=0
while True:
    i+=1
    sum1=(i*(i+1))/2
    sum2=((i+1)*(i+2))/2
    if sum1<=s and sum2>s:  # 여기가 핵심
        break  # 조건이 맞아떨어지면 반복문을 중단하고
print(i)  # 출력한다.
