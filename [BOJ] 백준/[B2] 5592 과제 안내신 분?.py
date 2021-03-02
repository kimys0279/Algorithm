'''
입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)을 하나씩 입력합니다. 
입력한 출석번호에 중복은 없으며, 순서에 상관없이 입력받을 수 있어야 합니다.

출력
출력은 2줄입니다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고,
2번째 줄에선 그 다음 출석번호를 출력하시면 됩니다.

예제 입력 1 
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
예제 출력 1 
2
8

students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    students.remove(applied) #소거

print(min(students))
print(max(students))
'''


stu = [i for i in range(1, 31)]

for _ in range(28):
    app = int(input())
    stu.remove(app)
    
print(min(stu))
print(max(stu)))
