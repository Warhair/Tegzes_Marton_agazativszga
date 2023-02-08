import random


def feladat1():
    print("I/A:")
    nev = input("\t Rendező neve: ")
    film = input("\t Film címe: ")
    ertekeles = random.randint(0, 10)
    print("I/B")
    print("\t Pontozás (0-10):", ertekeles)
    if ertekeles >= 8:
        print("\t Kihagyhatatlan film!")
    elif ertekeles > 3:
        print("\t Érdemes megnézni")
    else:
        print("\t Gyenge film")
