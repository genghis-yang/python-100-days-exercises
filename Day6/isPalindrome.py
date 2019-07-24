def is_palindrome(n):
  s = str(n)
  l = len(s)
  for i in range(0, int(l / 2 + 1)):
    if s[i] != s[l - i - 1]:
      return False
  return True