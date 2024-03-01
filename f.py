def objem_koule(polomer):
    if polomer != 0:
        objem = (4/3) * (3.14 * (polomer**3))
        return objem
    else:
        print("Nelze dělit nulou")

polomer = int(input("Zadej poloměr koule: "))
objem = int(input("Zadejte objem koule: "))