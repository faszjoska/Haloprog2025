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
jatek_szam=1
nem_talaltdb=0

kitalallado_szam=lista100[random.randint(0,len(lista100))] 

jatszol=True
while jatszol:
    tipp_sz=input("\nAdj egy szamot:").strip()
    
    if tipp_sz.isdecimal():
        tipp=int(tipp_sz)
    else:
        print("Egész számot kell megadni")
        continue
    while tipp != kitalallado_szam:
        nem_talaltdb+=1

        if tipp==123:
            pass
        if tipp< kitalallado_szam:
            print("Nagyobb a szám>")
        elif tipp> kitalallado_szam:
            print("Kissebb a szám<")
        else:
            pass 
        tipp_sz=input("\nAdj egy szamot (ha ki akarsz lépni EXIT):").strip()
        if tipp_sz.isdecimal():
            tipp=int(tipp_sz)
        elif tipp_sz=="EXIT":
            exit()
        else:
            print("Egész számot kell megadni")
            tipp=123
            continue
    print('jo a tipp')

    folytatas=input("Akarasz még játszani? [I/N]:")
    if folytatas == "N":
        jatszol=False
        print(f"{jatek_szam}db alkalommal játszott,{nem_talaltdb}db ennyiszer tippelt mellé")
    elif folytatas == "I":
        jatek_szam+=1
