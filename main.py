import time
import os

s = '   Welcome to Beijing. A sin city.   '
index = 0
while True:
  os.system('clear')
  print(s[index : index + 5])
  time.sleep(1)
  index += 1
