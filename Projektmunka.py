from random import *
import webbrowser
import os


def feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
        feladat = input("Mi legyen a program feladata (Iras, Olvasas): ")
        melyik_fajl = input("Melyik fájlt dolgozzuk fel: ")
        if feladat == "Olvasas" or  feladat == "olvasas":
                if melyik_fajl == "Be1.txt":
                    befajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                else:    
                    print("Nem jó adatokat adtál meg légyszi újra írd be :3")
                    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        elif feladat == "Iras" or feladat == "iras":
                if melyik_fajl == "Be1.txt":
                    iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                elif melyik_fajl == "Be2.txt":
                    iras_fajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
                else:
                    print("Nem jó adatokat adtál meg légyszi újra írd be :3")
                    feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        elif feladat == "Kuhar" or feladat == "kuhar":
            webbrowser.open_new("https://www.youtube.com/watch?v=gDBCG1e-qPY")
            feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        else:
             print("Nem jó adatokat adtál meg légyszi újra írd be :3")
             feladat_eldontes(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)  

    
        

def iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
        hozza_adott_sor = input("Mit szertenél hozzá írni (szabályokat tarts meg és a stoppal visszatudzs ugrani a feladat kiválasztáshoz): ")
        if "-" not in hozza_adott_sor :
            print("Kérlek írd be újra")
            print("Minta: Z50 - 5 - 18 - Utazható Országbérlettel")
            iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        else:
            Menetrend_iro = open("Be1.txt", "a", encoding="UTF-8") 
            Menetrend_iro.write(f"\n{hozza_adott_sor}")
            Menetrend_iro = open("Be1.txt", "r", encoding="UTF-8")
            for sor in Menetrend_iro.readlines():
                m = sor.split("-")
                Vonat_nevek.append(m[0])
                Indulasok_1.append(m[int(1)].strip("\n"))
                Indulasok_2.append(m[int(2)].strip("\n"))
                Orszag_berlet.append(m[(3)-1].strip("\n"))
            print(Vonat_nevek)
            Menetrend_iro.close()

                    
def iras_fajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
        hozza_adott_sor = input("Mit szertenél hozzá írni (szabályokat tarts meg és a stoppal visszatudzs ugrani a feladat kiválasztáshoz): ")
        if "-" not in hozza_adott_sor :
            print("Kérlek írd be újra")
            print("Minta: Z50 - 5 - 18 - Utazható Országbérlettel")
            iras_fajl_1(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
        else:
            Menetrend_iro = open("Be2.txt", "a", encoding="UTF-8") 
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
        Indulasok_1.append(m[(1)].strip()) 
        Indulasok_2.append(m[(2)].strip()) 
        Orszag_berlet.append(m[(3)].strip("\n"))
    Menetrend_beolvaso.close()


def befajl_2(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    Menetrend_beolvaso = open("Be2.txt", "r", encoding="UTF-8")
    for sor in Menetrend_beolvaso.readlines():
        m = sor.split("-")
        Vonat_nevek.append(m[0])
        Indulasok_1.append(m[int(1)])
        Indulasok_2.append(m[int(2)])
        Orszag_berlet.append(m[(3)].strip("\n"))
    Menetrend_beolvaso.close()


def listazas(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet):
    print("Hogy szertenéd hogy ki írassuk az adatokat?")
    print("1 Txt szerint 1 sorban 4 adat?")
    print("2 Vagy minden adatot külön lista szerűen?")
    kiiras = input("")
    print("\n")
    if kiiras == "1":
        print("Vonatok Nevei:")
        for i in range(len(Vonat_nevek)):
            print(Vonat_nevek[i], end=" ")
        print("\n")
        print("Vonat Órai indulása:")
        for i in range(len(Indulasok_1)):
            print(Indulasok_1[i], end=" ")
        print("\n")
        print("Vonat Perci indulása:")
        for i in range(len(Indulasok_2)):
            print(Indulasok_2[i], end=" ")
        print("\n")
        print("Vonat országbérlet lehetőségei: ")
        for i in range(len(Orszag_berlet)):
            print(f"{Orszag_berlet[i]}\n")
        print("\n")
    elif kiiras == "2":
        for i in range(len(Vonat_nevek)):
            print(Vonat_nevek[i] + Indulasok_1[i] + Indulasok_2[i] + Orszag_berlet[i])
            print("")
 



def Indulas_mero(Indulasok_1):
    maxi = 0
    for i in range(1, len(Indulasok_1)):
        if Indulasok_1[i] > Indulasok_1[maxi]:
            maxi = i
            maxi += 1
    print(f"A leg későbbi indulás {Indulasok_1[i]}")
    
def gyakorisag_mero(Vonat_nevek):
    Gyakorisag = {}
    for darab in Vonat_nevek:
        if darab in Gyakorisag:
                Gyakorisag[darab] += 1
        else:
            Gyakorisag[darab] = 1
    leggyakoribb = None
    maxi = 0
    for darab, megszamitas in Gyakorisag.items():
        if  megszamitas > maxi:
            maxi = megszamitas
            leggyakoribb = darab
    
    return leggyakoribb


def megszamolas(Orszag_berlet):
    db = 0
    n = len(Orszag_berlet)
    for i in range(n):
        if Orszag_berlet[i] == " Utazható Országbérlettel":
            db += 1
    return db

def kivalogatas(Orszag_berlet, Vonat_nevek, Utazhato):
    n = len(Orszag_berlet)
    j = 0
    for i in range(n):
        if Orszag_berlet[i] == " Utazható Országbérlettel":
            if Vonat_nevek[i] not in Utazhato: 
                Utazhato.append(Vonat_nevek[i])
    print("Orzságbérlettel utazható vonatok:", end=" ")
    for j in range(len(Utazhato)):
        print(Utazhato[j], end=" ")
    print("")
        
    

def kereses(Indulasok_1, Vonat_nevek, r):
    n = len(Vonat_nevek)
    i = 0
    while i < n and not (int(Indulasok_1[i]) == r):
        i += 1
    if i < n:
        return Vonat_nevek[i]
            
            
def osszegzes(Indulasok_1, Indulasok_2):
    s = 0
    m = 0
    n = len(Indulasok_1)
    for i in range(0, n-1):
        if Indulasok_1[i] == Indulasok_1[i+1]:
            m += 0
        else:
            m += 1
    s = (m * 60) + (int(Indulasok_2[n-1]) - int(Indulasok_2[0])) 
        
    return s

    
    

            

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
    Indulas_mero(Indulasok_1)
    print(f"Országbérlettel utazható vonatok száma: {megszamolas(Orszag_berlet)}")
    kivalogatas(Orszag_berlet, Vonat_nevek, Utazhato)
    print(f"A leggyakoribb vonat: {gyakorisag_mero(Vonat_nevek)}")
    rendez(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    listazas(Vonat_nevek, Indulasok_1, Indulasok_2, Orszag_berlet)
    print(f"A legelső indulás és a legutolsó indulás közt eltelt idő: {osszegzes(Indulasok_1, Indulasok_2)}")
    print(f"A keresett vonat: {kereses(Indulasok_1, Vonat_nevek, r)}")

main()

