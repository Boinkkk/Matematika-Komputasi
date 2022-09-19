from tabulate import tabulate


def deci_to_hex(userinput):
    listHex = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    resultHex = []
    while userinput >= 1:
        factor = userinput % 16
        for i in listHex:
            if factor == listHex[i]:
                resultHex.append(i)
                break
        else:
            resultHex.append(factor)

        # print(userinput, factor)

        userinput = int(userinput / 16)

    rv = reversed(resultHex)
    store = []
    for i in rv:
        store.append(i)
    return store


def text_to_hex(userinput):
    list = []
    counter = 0
    for i in userinput:
        join = ''
        list.append([])
        list[counter].append(i)
        converter = ord(i) #ASCII VALUE
        hex_value = deci_to_hex(converter)

        for j in hex_value:
            join += str(j)

        list[counter].append(join)
        counter += 1

    table = tabulate(list, headers=['Char', 'HEX'], tablefmt="grid")
    print(table)


text_to_hex('Karena lapar, Mulyono menjarah kulkasnya.')

# deci_to_hex(int(input()))
#


