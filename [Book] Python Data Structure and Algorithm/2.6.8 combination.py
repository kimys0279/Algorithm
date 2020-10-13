def combinations(s):
  if len(s) < 2:
    return s
  res = []
  for i, c in enumerate(s):
    res.append(c) #추가된 부분
    for j in combinations(s[:i] + s[i+1:]):
      res.append(c + j)
  return res

if __name__ == "__main__":
  result = combinations("abc")
  print(result)
