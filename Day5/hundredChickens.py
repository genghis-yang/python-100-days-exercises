for chicken in range(3, 100, 3):
  for hen in range(100 - chicken + 1):
    cock = 100 - hen - chicken
    if cock * 5 + hen * 3 + chicken / 3 == 100:
      print(cock, 'cocks,', hen, 'hens,', chicken, 'chicken')