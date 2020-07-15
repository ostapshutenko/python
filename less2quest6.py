#название:компьютер цена:20000 количество:5 eд:шт
#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

my_list = list()
buf = 0
i = 1

while True:
    buf = input()
    if buf == ' ' or buf == '':
        break
    buf = buf.split(' ')
    #print(buf)

    j=0
    while j < len(buf):
        buf[j] = buf[j].split(':')
        j += 1
    #print(buf)

    bf_dict = {str(buf[0][0]):str(buf[0][1]), str(buf[1][0]):float(buf[1][1]), str(buf[2][0]):float(buf[2][1]), str(buf[3][0]):str(buf[3][1])}
    bf_tuple = (i, bf_dict)
    my_list.append(bf_tuple)
    i += 1
#название:компьютер цена:20000 количество:5 eд:шт

bf_dict = {'название':[],'цена':[], 'количество':[], 'ед': []}
for index in my_list:
    c = index[1]["название"]
    if bf_dict["название"].count(c) < 1:
        bf_dict["название"].append(c)
    c = index[1]["цена"]
    if bf_dict["цена"].count(c) < 1:
        bf_dict["цена"].append(c)
    c = index[1]["количество"]
    if bf_dict["количество"].count(c) < 1:
        bf_dict["количество"].append(c)
    c = index[1]["eд"]
    if bf_dict["ед"].count(c) < 1:
        bf_dict["ед"].append(c)
    #print(index)
print(bf_dict["название"])
print(bf_dict["цена"])
print(bf_dict["количество"])
print(bf_dict["ед"])
