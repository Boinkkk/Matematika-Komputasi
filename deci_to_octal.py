from tabulate import tabulate
def deci_to_octal(userinput):
    listHex = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    data = []
    resultHex = []
    counter = 0
    while userinput >= 1:
        factor = userinput % 8
        for i in listHex:
            if factor == listHex[i]:
                resultHex.append(i)
                break
        else:
            resultHex.append(factor)

        # print(userinput, factor)

        data.append([])
        data[counter].append(f'{userinput}/8')
        userinput = int(userinput / 8)
        data[counter].append(userinput)
        data[counter].append(factor)
        counter += 1

    table = tabulate(data, headers=['Division', "Quetient", 'Remainder'])
    print(table, '\n')
    print('octal : ', end='')
    rv = reversed(resultHex)
    for i in rv:
        print(f'{i}', end='')

deci_to_octal(int(input()))

