'''
삼각형의 세 각을 입력받은 다음, 

세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.

입력
총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.

출력
문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.

예제 입력 1 
60
70
50
예제 출력 1 
Scalene'''

arr = []
for _ in range(3):
    arr.append(int(input()))

arr.sort()
if sum(arr) != 180:
    print('Error')
elif arr[0] == 60:
    print('Equilateral')
elif arr[0] != arr[1] and arr[1] != arr[2]:
    print('Scalene')
else:
    print('Isosceles')






