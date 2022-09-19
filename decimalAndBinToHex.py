from textwrap import wrap
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
    data = []
    resultHex = []
    counter = 0
    while userinput >= 1:
        factor = userinput % 16
        for i in listHex:
            if factor == listHex[i]:
                resultHex.append(i)
                break
        else:
            resultHex.append(factor)

        # print(userinput, factor)

        data.append([])
        data[counter].append(f'{userinput}/16')
        userinput = int(userinput / 16)
        data[counter].append(userinput)
        data[counter].append(factor)
        counter += 1

    table = tabulate(data, headers=['Division', "Quetient", 'Remainder'])
    print(table, '\n')
    rv = reversed(resultHex)
    for i in rv:
        print(f'{i}', end='')


# deci_to_hex(int(input()))

def bin_to_hex(userinput):
    listHex = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    value = userinput[::-1]
    result = wrap(value, 4) # memisahkan 4 digit dari belakang
    print('hasil pemisahan = ', result)
    counter = 0
    buffer = 0
    index = 0
    list_match = []
    for a in result:
        list_match.append([])
        for i in result[buffer]:
            base = 2**counter
            if i == '1':
                list_match[index].append(base)
            counter += 1
        buffer += 1
        index += 1
        counter = 0
    print(list_match)

    index_2 = 0
    sum_j = []
    for j in list_match:
        sum_i = 0
        for i in list_match[index_2]:
            sum_i += i
        sum_j.append(sum_i)
        index_2 += 1
    print(sum_j)
    rv = reversed(sum_j)
    print('Hasil HEX : ', end='')
    for i in rv:
        for j in listHex:
            if i == listHex[j]:
                print(j, end='')
                break
        else:
            print(i, end='')


bin_to_hex(str(input()))

