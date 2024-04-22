from random import *


def feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
        feladat = input("Mi legyen a program feladata: ")
        melyik_fajl = input("Melyik fájlt dolgozzuk fel: ")
        if feladat == "Olvasas" or "olvasas":
                if melyik_fajl == "Be1.txt":
                    befajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                else:    
                    print("Nem jó adatokat adtál meg légyszi újra írd be :3")
                    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        elif feladat == "Iras" or "iras":
                if melyik_fajl == "Be1.txt":
                    iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    iras_fajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                else:
                    print("Nem jó adatokat adtál meg légyszi újra írd be :3")
                    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)        
    
        

def iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_iro = open("Be1.txt", "a", encoding="UTF-8") 
    hozza_adott_sor = input("Mit szertenél hozzá írni (szabályokat tarts meg): ")
    Menetrend_iro.write(f"\n{hozza_adott_sor}")
    Menetrend_iro = open("Be1.txt", "r", encoding="UTF-8")
    for sor in Menetrend_iro.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)].strip("\n"))
        Indulasok_2.append(m[int(2)].strip("\n"))
        Orszag_berlet.append(m[(3)-1].strip("\n"))
    # fajl_torles()
    print(Vonat_nevek)
    Menetrend_iro.close()

def iras_fajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_iro = open("Be2.txt", "a", encoding="UTF-8")
    hozza_adott_sor = input("Mit szertenél hozzá írni (szabályokat tarts meg): ")
    Menetrend_iro.write(f"\n{hozza_adott_sor}")
    Menetrend_iro = open("Be2.txt", "r", encoding="UTF-8")
    for sor in Menetrend_iro.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)].strip("\n"))
        Indulasok_2.append(m[int(2)].strip("\n"))
        Orszag_berlet.append(m[(3)-1].strip("\n"))
    print(Vonat_nevek)
    Menetrend_iro.close()

def befajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_beolvaso = open("Be1.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)])
        Indulasok_2.append(m[int(2)])
        Orszag_berlet.append(m[(3)].strip("\n"))
    # print(Vonat_nevek)
    # print(Indulasok)
    Menetrend_beolvaso.close()


def befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_beolvaso = open("Be2.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)])
        Indulasok_2.append(m[int(2)])
        Orszag_berlet.append(m[(3)].strip("\n"))
    # print(Vonat_nevek)
    # print(Indulasok_2)
    # print(Indulasok_1)
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
    print("Vonat országbérlet lehetőségei: ")
    for i in range(len(Orszag_berlet)):
        print(f"{Orszag_berlet[i]}\n")
    print()
 



def gyakorisag_mero(Vonat_nevek):
    maxi = 0
    for i in range(1, len(Vonat_nevek)):
        if Vonat_nevek[i] > Vonat_nevek[maxi]:
            maxi = i
            maxi += 1
    print(f"A leggyakoribb vonat: {Vonat_nevek[i]}")

def megszamolas(Orszag_berlet):
    db = 0
    n = len(Orszag_berlet)
    for i in range(n):
        if Orszag_berlet[i] == " Utazható Országbérlettel":
            db += 1
    return db

def kivalogatas(Orszag_berlet, Vonat_nevek, Utazhato):
    n = len(Orszag_berlet)
    for i in range(n):
        if Orszag_berlet[i] == " Utazható Országbérlettel":
            if Vonat_nevek[i] not in Utazhato:  
                Utazhato.append(Vonat_nevek[i])
    print(f"{', '.join(Utazhato)}\n")
    

def kereses(Indulasok_1, Indulasok_2, Vonat_nevek, r):
    n = len(Vonat_nevek)
    i = 0
    print(r)
    while i < n and not (Indulasok_1[i] == r):
        i += 1
    if i < n:
        return Vonat_nevek[i]
            

    
    
    
# def fajl_torles():
#     fajl_eredetibe_allitasa = input("Ki akarod azt a fájlt törölni amit bele írtál?: ")
#     if fajl_eredetibe_allitasa == "Igen" or "igen":
#         melyik_txt = input("Melyik txt-t használtad?: ")
#         if melyik_txt == "Be1.txt":
#             Menetrend_beolvaso = open("Be1.txt", "w+", encoding="UTF-8")
#             Menetrend_beolvaso.seek(62)
#             Menetrend_beolvaso.writelines("")
#             Menetrend_beolvaso.close()

            

def rendez(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    n = len(Indulasok_1)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            ido1 = int(Indulasok_1[j]) * 60 + int(Indulasok_2[j])
            ido2 = int(Indulasok_1[j+1]) * 60 + int(Indulasok_2[j+1])
            if ido1 > ido2:
                Vonat_nevek[j], Vonat_nevek[j+1] = Vonat_nevek[j+1], Vonat_nevek[j]
                Indulasok_1[j], Indulasok_1[j+1] = Indulasok_1[j+1], Indulasok_1[j]
                Indulasok_2[j], Indulasok_2[j+1] = Indulasok_2[j+1], Indulasok_2[j]
                Orszag_berlet[j], Orszag_berlet[j+1] = Orszag_berlet[j+1], Orszag_berlet[j]

def main():
    r = randint(3, 19)
    Utazhato = []
    Vonat_nevek = []
    Indulasok_1 = []
    Indulasok_2 = []
    Orszag_berlet = []
    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    gyakorisag_mero(Vonat_nevek)
    print(f"Országbérlettel utazható vonatok száma: {megszamolas(Orszag_berlet)}")
    kivalogatas(Orszag_berlet, Vonat_nevek, Utazhato)
    rendez(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    listazas(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    print(kereses(Vonat_nevek, Indulasok_1, Indulasok_2, r))
    # fajl_torles()

main()

