import math
import random

# 브루트 포스
def finding_prime(number):
  num = abs(number)
  if num < 4: return True
  for x in range(2, num):
    if num % x == 0:
      return False
  return True

#제곱근
def finding_prime_sqrt(number):
  num = abs(number)
  if num < 4 : return True
  for x in range(2, int(math.sqrt(num))+1):
    if number % x == 0:
      return False
  return True

#페르마의 정리
def finding_prime_fermat(number):
  if number <= 102:
    for a in range(2, number):
      if pow(a, number - 1, number) != 1:
        return False
    return True
  else:
    for i in range(100):
      a = random.randint(2, number - 1)
      if pow(a, number - 1, number) != 1:
        return False
    return True

def test_finding_prime():
  number1 = 17
  number2 = 20
  assert(finding_prime(number1) is True)
  assert(finding_prime(number2) is False)
  assert(finding_prime_sqrt(number1) is True)
  assert(finding_prime_sqrt(number2) is False)
  assert(finding_prime_fermat(number1) is True)
  assert(finding_prime_fermat(number2) is False)
  print("테스트 통과!")

if __name__ == "__main__":
  test_finding_prime()
  
