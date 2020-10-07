<최장 증가 부분 수열>
https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4

  
import sys
 
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
DP=[0]
 
 
 
for i in range(N):
 
    low=0
    high=len(DP)-1
 
 
    while low<=high:#A[i]보다 작거나 같은수중에 제일 큰거 위치 찾기
        mid=(low+high)//2
        if DP[mid]<A[i]:
            low=mid+1
        else:
            high=mid-1
 
    if low>=len(DP):#위치가 배열보다 크다면 넣어준다
        DP.append(A[i])
    else:#해당 위치의 숫자를 바꿔준다.항상 작거나 같은수를 반환하기때문에 비교하지 않아도된다.
        DP[low]=A[i]
 
print(len(DP)-1)
