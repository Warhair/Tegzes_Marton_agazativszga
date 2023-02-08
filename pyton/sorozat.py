import random


lista = []
def feladat2():
    print("II/A, B, C")
    print("\t", end="")
    i = 0
    while i < 10:
        szam = random.randint(10, 350)
        lista.append(szam)
        print(szam, end="#")
        if i == 9:
            print(szam)
        i += 1
    konzol_kiir()

def parosok_szama(list):
    paros = 0
    for i in list:
        if i % 2 == 0:
            paros += 1
            i += 1
        i += 1
    return paros

def konzol_kiir():
    print("II D, E:")
    print("\t A  párosok szama: ", parosok_szama(lista))

def file_kiir():
    print("II F:")
    f = open("kimutatas.txt", "w")
    f.write("\t A  párosok szama: ", parosok_szama(lista))
    f.close()






