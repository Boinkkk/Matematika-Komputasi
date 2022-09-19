# user_input = input(str())
# def bintodecimal(stringInput):
#     listResult = []
#     listBuffer = []
#     hasil = 0
#     value = len(stringInput)
#     base = 0
#     counter = 0
#     for i in stringInput:
#         if i == '1':
#             counter += 1
#
#         elif i == '0':
#             counter += 1
#
#     if counter == value:
#         hasil = 0
#         for i in stringInput:
#             if i == '0':
#                 base = 0
#             elif i == '1':
#                 base = 1
#             buffer = (base * 2 ** (value - 1))
#             print('( 2 x', base, '^', (value - 1), ')', end=' + ')
#             hasil += buffer
#             value -= 1
#             listResult.append(hasil)
#             listBuffer.append(buffer)
#
#
#
#         print(f'\n{listBuffer}')
#         print(listResult)
#         print(f'Decimal dari {stringInput} = {hasil}')
#         print(f'bukti menggunakan converter = {int(stringInput, 2)}')
#
# bintodecimal(user_input)


def bin_to_deci_coma(user_input):
    counter = 0
    reverse_counter = 0
    for i in user_input:
        if i == '1' or i == '0':
            counter += 1
        elif i == ',':
            break
    for j in reversed(user_input):
        if j == '1' or j == '0':
            reverse_counter += 1
        elif j == ",":
            break
    bufferlist = []
    base = 0
    sumBuffer = 0
    for i in user_input:

        if i == '1':
            base = 1
        if i == '0':
            base = 0
        if i == ',':
            continue

        buffer = (base * 2 ** (counter - 1))
        print(f'({base} x 2^{counter - 1}) + ', end='')
        sumBuffer += buffer
        counter -= 1
        bufferlist.append(buffer)

    print('\nHasiil Penjumlahan : ', bufferlist)
    print('Decimal value : ', sumBuffer)


bin_to_deci_coma(input(str()))

