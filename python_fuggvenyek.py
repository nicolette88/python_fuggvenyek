# 1.	feladat
print('---1. Feladat---')


def my_function(start=2000, finish=3200, oszthato=7, nem_oszthato=5):
    listOfNumbers = []
    for x in range(start, finish + 1):
        if ((x % oszthato == 0) and (x % nem_oszthato != 0)):
            listOfNumbers.append(x)
    return listOfNumbers


print(my_function())

# 2.	Feladat
print('---2. Feladat---')


def my_function2(inputArray):
    counter = 0
    for name in inputArray:
        if (name == 'Pista'):
            counter += 1
    return counter


inputArray = [
    'Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László',
    'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista'
]
print(my_function2(inputArray))

# 3.	Feladat
print('---3. Feladat---')

# bonyolultabb megoldás hibakezeléssel
print('---3. Feladat bonyolultabb---')


def print_hello(count):
    for x in range(count):
        print(str(x + 1) + '.    Helló!')


def convert_to_number(text):
    returnText = ""
    try:
        returnText = int(text)
    except:
        returnText = "error"
    return returnText


text = input("> input: ")
num = convert_to_number(text)
if (num == "error"):
    print("Oops, something went wrong...")
else:
    print_hello(num)

# egyszerűbb megoldás - hibakezelés nincs benne
print('---3. Feladat egyszerubb---')


def print_hello2(count):
    for x in range(count):
        print(str(x + 1) + '.    Helló!')


def convert_to_number2(text):
    return int(text)


text = input("> input: ")
num = convert_to_number2(text)
print_hello2(num)

# 4.	Feladat
print('---4. Feladat---')

import math  # math.pi


def convert_to_number3(text):
    return int(text)


def kerulet(r):
    # K = 2 * pi * r
    return 2 * math.pi * r


def terulet(r):
    # T= pi * r * r
    return math.pi * r * r


text = input("> radius: ")
radius = convert_to_number3(text)
print('terulet: ' + str(terulet(radius)))
print('kerulet: ' + str(kerulet(radius)))

# 5.	Feladat
print('---5. Feladat---')


def kiir(text, csoport):
    print(text)
    for name in csoport:
        print(name)


def listaRendezesBontas(inputList):
    sortedList = sorted(inputList)
    lenght = len(sortedList)
    split_index = lenght // 2
    group1 = sortedList[:split_index]
    group2 = sortedList[split_index:]
    #kiiras
    kiir("   1.csoport:", group1)
    kiir("   2.csoport:", group2)


nameList = [
    'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
    'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
    'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás'
]
#nameList = [
#     'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
#     'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
#     'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint'
# ]
listaRendezesBontas(nameList)
