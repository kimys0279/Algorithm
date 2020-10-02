def reverse_words_brute(string):
  word, sentence = [], []
  for character in string:
    if character != " ":
      word.append(character)
    else:
      #조건문에서 빈 리스트는 False. 여러 공백이 있는 경우 조건문을 건너뛴다
      if word:
        sentence.append("".join(word))
      word = []

  #마지막 단어가 있다면 문장에 추가한다.
  if word != "":
    sentence.append("".join(word))
  sentence.reverse()
  return " ".join(sentence)


if __name__ == "__main__":
  str1 = "파이썬 알고리즘 정말 재미있다"
  str2 = reverse_words_brute(str1)
  print(str2)
