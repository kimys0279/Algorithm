'''
baby sukhwan tururururu turururu
very cute tururururu turururu
in bed tururururu turururu
…

이 때, 석환이가 부르는 노래의 N번째 단어는 무엇일까?

입력
첫 번째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫 번째 줄에 석환이가 N번째로 부를 단어를 출력한다. 
여기서 단어란 가사 중 공백으로 구분되는 연속된 알파벳 소문자열을 뜻한다. 
단, 출력할 단어가 “tururu...ru”일 때, “ru”가 k(k ≥ 5)번 반복되면 “tu+ru*k”와 같이 출력한다.

예제 입력 1 
1
예제 출력 1 
baby'''

N = int(input())
count = N // 14

if N % 14 == 1:
    print("baby")
elif N % 14 == 2:
    print("sukhwan")
elif N % 14 == 5:
    print("very")
elif N % 14 == 6:
    print("cute")
elif N % 14 == 9:
    print("in")
elif N % 14 == 10:
    print("bed")
elif N % 14 == 13:
    print("baby")
elif N % 14 == 0:
    print("sukhwan")
elif N % 14 == 3 or N % 14 == 7 or N % 14 == 11:
    if count < 3:
        print("tururu" + "ru" * count)
    else:
        print("tu+ru*%s" % (count+2))
else:
    if count < 4:
        print("turu" + "ru" * count)
    else:
        print("tu+ru*%s" % (count+1))
