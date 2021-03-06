'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

예제 입력 1 
baekjoon
예제 출력 1 
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1'''

word = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(word.find(chr(i)))

    
'''
1. 코드에 대한 전체적인 풀이

이번 문제는 입력받은 문자열의 각 알파벳이 문자열 안에서 위치한 순서를 출력하는 문제이다. 
순서를 출력을 할 때는 a~ z 알파벳 순서에 맞춰서 입력받은 문자열에서 해당 알파벳이 없으면 -1을 출력하고 
있으면 문자열 안에서 첫 번째 위치한 순서를 숫자로 출력한다. 

 

a~z까지의 알파벳은 아스키코드의 숫자 범위로 리스트를 생성했다. 아스키코드에서 a= 97이고 z= 122이다. 
97 ~ 122까지의 숫자가 a~z까지의 알파벳에 대응하는 아스키코드이다. 

 

find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다. 
만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다. 
이 문제에서 요구하는 바를 그대로 출력할 수 있는 함수여서 find 함수를 사용한 코드를 작성했다.

 

2. 코드 상단, 문자열을 입력받고 알파벳 리스트를 생성한다.

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위
입려 받은 문자열은 word 변수에 선언하였다. 
알파벳 리스트는 아스키코드를 이용해서 생성했다. a~z까지는 아스키코드에서 숫자 97~122에 해당하기 때문에 
range 함수를 이용해서 97~122까지의 숫자 범위를 생성하고 list 함수를 이용해서 리스트로 변환하였다. 

 

3. 코드 하단에서 find 함수를 사용한다. 

for x in alphabet :
    print(word.find(chr(x))) 
alphabet 리스트의 숫자로 이루어진 각각의 원소를 for문을 이용하여 변수 x에 선언하고서 
우선 문자열로 변환하기 위해 chr 함수를 사용하였다. chr 함수는 아스키코드에 해당하는 
숫자를 문자열로 변환시키는함수이다. 

 

find 함수를 이용해서 입력받은 문자열 안에 chr 함수로 변환된 문자가 있는지 찾는다. 
만일 문자열이 있으면 찾는 문자가 첫 번째에 위치한 인덱스 숫자를 출력하고 없으면 -1을 출력하게 된다.

 

4. 아스키코드 변환 함수

위 문제에서 사용한 chr함수와 find 함수에 대해 추가적으로 설명하면, chr( ) 함수는 숫자(아스키코드) -> 문자로
변환하는 함수이고 반대로 문자 -> 숫자(아스키코드)로 변환할 때는 ord( ) 함수를 사용한다. 

 

5. find 함수와 index 함수의 비교

find 함수는 문자열에서만 사용 가능한 함수이다. 이와 유사한 기능을 하는 함수로 index 함수가 있다. 
index 함수는 문자열뿐만 아니라 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 
반환하는 함수로 쓰인다. find 함수와 다른 점은 find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 
출력하지만 index함수는 >AttributeError가 발생한다.'''



