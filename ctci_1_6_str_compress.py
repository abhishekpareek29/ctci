def compress(string):
  count = 0
  string_builder = []
  char_dict = dict()
  for i in range(len(string)):
    count += 1
    if i+1 == len(string):
      string_builder.append(string[i])
      string_builder.append(count)
      count = 0
    if (i+1 < len(string)):
      if (string[i] != string[i+1]):
        string_builder.append(string[i])
        string_builder.append(count)
        count = 0

  return str(string_builder)


if __name__ == "__main__":
  string = 'asaccccddq'
  res = compress(string)
  print(res)
