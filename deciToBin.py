def deci_to_bin(deci):
    i, power, counter, checker = 0, 0, 0, []
    while i < deci:
        i = 2 ** power
        power += 1
        counter += 1
        checker.append(i)

    checker.pop()
    checker.reverse()

    for i in checker:

        if i <= deci:
            print('1', end='')
            deci = deci - i
        elif i > deci:
            print('0', end='')

deci_to_bin(int(input()))


# ---------- method2 ---------
# Divide the number by 2.
# Get the integer quotient for the next iteration.
# Get the remainder for the binary digit.
# Repeat the steps until the quotient is equal to 0.
# source https://www.rapidtables.com/convert/number/decimal-to-binary.html

# from tabulate import tabulate

from tabulate import tabulate

def deci_to_bin2(decimal):
    data = [[]]
    deciList = []
    counter = 0

    while decimal >= 1:
        if decimal % 2 == 0:
            deciList.append('0')

        elif decimal % 2 != 0:
            deciList.append('1')


        sisabagi = decimal % 2

        data.append([])
        data[counter].append(f'{decimal}/2')
        decimal = int(decimal / 2)
        data[counter].append(decimal)
        data[counter].append(sisabagi)

        counter += 1

    data.pop()
    rv = reversed(deciList)
    table = tabulate(data, headers=['Division', "Quetient", 'Remainder'])
    print(f'\n {table}')
    print('\nresult = ', ''.join(rv))

deci_to_bin2(int(input()))
