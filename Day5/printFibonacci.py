num = int(input('Please input a number: '))
first = 1
second = 1
for x in range(num):
  if x > 1:
    first, second = second, first + second
  print(x, ':', second)