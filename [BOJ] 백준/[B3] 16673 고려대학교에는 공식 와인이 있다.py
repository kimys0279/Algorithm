'''
Kn+Pn2 
입력
C, K, P가 공백으로 구분되어 주어진다. (0 ≤ C ≤ 100, 0 ≤ K ≤ 1000,  0 ≤ P ≤ 100)

출력
첫 번째 줄에 수빈이가 C년 동안 수집한 와인 수를 출력한다.

예제 입력 1 
3 1 1
예제 출력 1 
20
1년차 2병, 2년차 6병, 3년차 12병으로 총 20병을 수집하였다.'''

c, k, p = map(int, input().split())
m = 0

for i in range(1, c+1):
    m += k*i + p * (i**2)
print(m)







