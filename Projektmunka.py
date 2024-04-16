def befajl_1(Vonat_nevek, Indulasok):
    Menetrend_beolvaso = open("S50 - 303.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok.append(m[int(1)].strip("\n"))
    print(Vonat_nevek)
    print(Indulasok)
    Menetrend_beolvaso.close()


def listazas(Vonat_nevek, Indulasok):
    print("Vonatok Nevei:")
    for i in range(len(Vonat_nevek)):
        print(Vonat_nevek[i], end=" ")
    print("\n")
    print("Vonatok Indulásai:")
    for i in range(len(Indulasok)):
        print(Indulasok[i], end=" ")



def gyakorisag_mero(Vonat_nevek):
    maxi = 0
    for i in range(1, len(Vonat_nevek)):
        if Vonat_nevek[i] > Vonat_nevek[maxi]:
            maxi = i
            print(f"A leggyakoribb vonat: {Vonat_nevek[i]}")


def main():
    Vonat_nevek = []
    Indulasok = []
    befajl_1(Vonat_nevek, Indulasok)
    gyakorisag_mero(Vonat_nevek)
    listazas(Vonat_nevek, Indulasok)

main()
