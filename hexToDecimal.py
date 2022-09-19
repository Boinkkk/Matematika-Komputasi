hexNumber = input(str())
base = 0
sumBuffer = 0
resultlist = []
listHex = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}
counter = 0
for i in hexNumber:
    if i == ',' or i == '.':
        break
    else:
        counter += 1

for i in hexNumber:
    for j in listHex:
        if i == j:
            base = int(listHex[j])
            break
        else:
            base = i
    if i == ',':
        continue

    intBase = int(base)

    buffer = intBase * 16 ** (counter - 1)
    resultlist.append(buffer)
    print(f'({intBase} x 16^{counter-1}) + ', end='')
    sumBuffer += buffer
    counter -= 1

print(f"\nhasil penjumlahan = {resultlist}")
print(f'Decimal : {sumBuffer}')


