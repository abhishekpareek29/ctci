def isoneaway(str1, str2):
  len1 = len(str1)
  len2 = len(str2)
  founddiff = False
  if abs(len2 - len1) <= 1:
    if len1 == len2:
      for i in range(len2):
        if str1[i] != str2[i]:
          if founddiff:
            return False
          founddiff = True
      return True
    else:
      if len1 > len2:
        for i in range(len2):
          if str1[i] != str2[i]:
            if str1[i+1] != str2[i]:
              return False
        return True
      if len2 > len1:
        for i in range(len1):
          if str2[i] != str1[i]:
            if str2[i+1] != str1[i]:
              return False
        return True
  else:
    return False

if __name__ == "__main__":
  str1 = 'dsadsadsa'
  str2 = 'dsadsadsa'
  res = isoneaway(str1, str2)
  print(res)
