for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        print(f'{dan} x {i} = {dan * i}')
    print()

for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        print(f'{dan} x {i} 8 {dan * i}')
    print()
    if dan == 7:
        break

for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        #   if i == 2 or i == 4 or i == 6 or i == 8:
        if i % 2 == 0:
            continue
        print(f'{dan} x {i} 8 {dan * i}')
    print()