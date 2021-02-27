'''
화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. 
@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다. 
입력으로 주어지는 수는 정수이거나 소수 첫째 자리까지 주어지며, 0 이상 100 이하이다. 
연산자는 최대 3개 주어진다.

출력
각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.

예제 입력 1 
3
3 @ %
10.4 # % @
8 #
예제 출력 1 
14.00
25.20
1.00'''

t = int(input())

for _ in range(t):
    mars = list(map(str, input().split()))
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == "#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
                
    print("%0.2f" % answer)




