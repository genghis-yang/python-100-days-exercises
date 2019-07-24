import random

face = random.randint(1, 6)
if face == 1:
  result = 'Sing a song'
elif face == 2:
  result = 'Dance'
elif face == 3:
  result = 'Bark'
elif face == 4:
  result = 'Push-up'
elif face == 5:
  result = 'Read tongue-twister'
else:
  result = 'Tell a joke'
print(result)