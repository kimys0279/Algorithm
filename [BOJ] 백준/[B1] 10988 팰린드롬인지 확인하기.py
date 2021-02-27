'''
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 
알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

예제 입력 1 
level
예제 출력 1 
1
예제 입력 2 
baekjoon
예제 출력 2 
0'''

1.
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)

    
2. 
name = input()
name2=""
for i in range(len(name)-1,-1,-1):
    name2+=name[i]  # for문으로 문자를 역순으로 name2에 저장
if name==name2:
    print(1)
else:
    print(0)
