length = float(input('Please input the length: '))
unit = str(input('Please input the unit(centimeter/inch): '))
if unit == 'inch':
  print(length, unit + 'es', '=', length * 2.54, 'centimeters')
elif unit == 'centimeter':
  print(length, unit + 's', '=', length / 2.54, 'inches')
