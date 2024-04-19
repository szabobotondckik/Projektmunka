def feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
        feladat = input("Mi legyen a program feladata: ")
        melyik_fajl = input("Melyik fájlt dolgozzuk fel: ")
        if feladat == "Olvasas" or "olvasas":
            try:
                if melyik_fajl == "Be1.txt":
                    befajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
            except:
                print("NUH UH")
        if feladat == "Iras" or "iras":
            try:
                if melyik_fajl == "Be1.txt":
                    iras_fajl(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    iras_fajl(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
            except:
                print("NUH UH")


def iras_fajl(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_iro = open("Be1.txt", "a", encoding="UTF-8")
    for sor in Menetrend_iro.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)].strip("\n"))
        Indulasok_2.append(m[int(2)].strip("\n"))
    print(Vonat_nevek)

def befajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_beolvaso = open("Be1.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)].strip("\n"))
        Indulasok_2.append(m[int(2)].strip("\n"))
        Orszag_berlet.append(m[int(3)].strip("\n"))
    # print(Vonat_nevek)
    # print(Indulasok)
    Menetrend_beolvaso.close()


def befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_beolvaso = open("Be2.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)].strip("\n"))
        Indulasok_2.append(m[int(2)].strip("\n"))
        Orszag_berlet.append(m[int(3)].strip("\n"))
    # print(Vonat_nevek)
    print(Indulasok_2)
    print(Indulasok_1)
    Menetrend_beolvaso.close()


def listazas(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    print("Vonatok Nevei:")
    for i in range(len(Vonat_nevek)):
        print(Vonat_nevek[i], end=" ")
    print("\n")
    print("Vonat Órai indulása:")
    for i in range(len(Indulasok_1)):
        print(Indulasok_1[i], end=" ")
    print()
    print("Vonat Perci indulása:")
    for i in range(len(Indulasok_2)):
        print(Indulasok_2[i], end=" ")
    print()
    for i in range(len(Orszag_berlet)):
        print(Orszag_berlet[i], end=" ")
 



def gyakorisag_mero(Vonat_nevek):
    maxi = 0
    for i in range(1, len(Vonat_nevek)):
        if Vonat_nevek[i] > Vonat_nevek[maxi]:
            maxi = i
            print(f"A leggyakoribb vonat: {Vonat_nevek[i]}")

def megszamolas(Orszag_berlet):
    db = 0
    n = len(Orszag_berlet)
    for i in range(n):
        if Orszag_berlet[i] == "Utazható Országbérlettel":
            db += 1
    return db



def main():
    Vonat_nevek = []
    Indulasok_1 = []
    Indulasok_2 = []
    Orszag_berlet = []
    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    gyakorisag_mero(Vonat_nevek)
    print(megszamolas(Orszag_berlet))
    listazas(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)


main()

