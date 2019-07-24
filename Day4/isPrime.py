import math
num = int(input('Please input an integer: '))
end = int(math.sqrt(num))
is_prime = True
for x in range(2, end + 1):
  if num % x == 0:
    is_prime = False
    break
if is_prime:
  print(num, 'is a prime')
else:
  print(num, 'is NOT a prime')