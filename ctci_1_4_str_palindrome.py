def ispalindrome(str):
  dict_char = dict()
  lone = 0
  for i in str:
    if i != " ":
      if i in dict_char:
        dict_char[i] -= 1
      else:
        dict_char[i] = 1
  for key, val in dict_char.items():
    if val != 0:
      lone += 1
      if lone > 1:
        return False
  return True

if __name__ == "__main__":
  str = 'ttcc roruio'
  res = ispalindrome(str)
  print(res)
