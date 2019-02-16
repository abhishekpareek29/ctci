def check_anagram(str1, str2):
  d = dict()
  for i in str1:
    if i in d.keys():
      d[i] += 1
    else:
      d[i] = 1
  for j in str2:
    if j in d.keys():
      d[j] -= 1
    else:
      return False
  for key, val in d.items():
    if val != 0:
      return False
  return True

if __name__ == "__main__":
  str1, str2 = 'abcd', 'cdab'
  res = check_anagram(str1, str2)
  print(res)
