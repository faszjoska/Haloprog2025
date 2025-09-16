import random


# lista létrehozasa
lista100=[]

# lista feltoltese random 40 db ketjegyu szamokkal
while len(lista100)!=40:
    szam=random.randint(10,99)
    if szam not in lista100:
        lista100.append(szam)
print(len(lista100))
#muxik

# egyszam jatek
jatek_szam=0
nem_talaltdb=0

kitalallado_szam=lista100[random.randint(0,len(lista100))] 

jatszol=True
while jatszol:
    jatek_szam+=1
    tipp_sz=input("Adj egy szamot:").strip()
    
    if tipp_sz.isdecimal():
        tipp=int(tipp_sz)
    else:
        print("Egész számot kell megadni")
        continue
    while tipp != kitalallado_szam:
        if tipp< kitalallado_szam:
            print("Nagyobb a szám")
        else:
            print("Kissebb a szám")
        tipp_sz=input("Adj egy szamot:\n(ha ki akarsz lépni EXIT)").strip()
        if tipp_sz.isdecimal():
            tipp=int(tipp_sz)
        elif tipp_sz=="EXIT":
            exit()
        else:
            print("Egész számot kell megadni")
            continue
    print('jo a tipp')

    folytatas=input("Akarasz még játszani? [I/N]:")
    if folytatas == "N":
        jatszol=False

