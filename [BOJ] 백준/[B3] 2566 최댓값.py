'''
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

예제 입력 1 
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80
예제 출력 1 
90
5 7

max_num = 0

for i in range(9):
    row = list(map(int, input().split())) #굳이 행렬을 저장할 필요는 없다
    if max(row) > max_num:
        max_num = max(row) #최댓값
        x = i + 1 #행
        y = row.index(max_num) + 1 #열
print(max_num)
print(x,y)
'''

maxn = 0

for i in range(9):
    row = list(map(int, input().split()))
    if max(row) > maxn:
        maxn = max(row)
        x = i+1
        y = row.index(maxn) + 1
        
print(maxn)
print(x, y)




