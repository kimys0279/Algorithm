'''
첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가  
빈칸을 사이에 두고 주어진다.

출력
첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를  도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.

예제 입력 1 
0 1 0 1
1 1 1 0
0 0 1 1
예제 출력 1 
B
A
B'''

def yut():
    arr = list(map(str, input().split()))
    if arr.count('0') == 1:
        return print('A')
    elif arr.count('0') == 2:
        return print('B')
    elif arr.count('0') == 3:
        return print('C')
    elif arr.count('0') == 4:
        return print('D')
    else:
        return print('E')

for i in range(3):
    yut()
