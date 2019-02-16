def check_unique_char(str):
  for i, char in enumerate(str):
    for j, char_match in enumerate(str):
      if j != i:
        if char == char_match:
          return False
  return True

def check_unique_chars_parth(str):
  h = set()
  for ch in str:
    if ch in h:
      return False
    else:
      h.add(ch)
  return True

if __name__ == "__main__":
  str = 'abdsa'
  res = check_unique_chars_parth(str)
  # res = check_unique_char(str)
  print(res)
