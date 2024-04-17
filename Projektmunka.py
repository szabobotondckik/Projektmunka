def feladat_eldontes(Vonat_nevek, Indulasok, Orszag_berlet):
        feladat = input("Mi legyen a program feladata: ")
        if feladat == "Olvasas" or "olvasas":
            try:
                melyik_fajl = input("Melyik fájlt dolgozzuk fel: ")
                if melyik_fajl == "S50 - 303.txt":
                    befajl_1(Vonat_nevek, Indulasok)
                elif melyik_fajl == "Vonatok de orzság bérlet.txt":
                    befajl_2(Vonat_nevek, Indulasok, Orszag_berlet)
            except:
                print("NUH UH")



def befajl_1(Vonat_nevek, Indulasok):
    Menetrend_beolvaso = open("S50 - 303.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok.append(m[int(1)].strip("\n"))
    print(Vonat_nevek)
    print(Indulasok)
    Menetrend_beolvaso.close()


def befajl_2(Vonat_nevek, Indulasok, Orszag_berlet):
    Menetrend_beolvaso = open("Vonatok de orzság bérlet.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok.append(m[int(1)].strip("\n"))
        Orszag_berlet.append(m[int(2)].strip("\n"))
    print(Vonat_nevek)
    print(Indulasok)
    print(Orszag_berlet)
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
    Orszag_berlet = []
    feladat_eldontes(Vonat_nevek, Indulasok, Orszag_berlet)
    gyakorisag_mero(Vonat_nevek)
    listazas(Vonat_nevek, Indulasok)


main()

