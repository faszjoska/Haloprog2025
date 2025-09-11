import random


# lista létrehozasa
lista100=[]

# lista feltoltese random 100 db ketjegyu szamokkal
for i in range(100):
    szam=random.randint(10,99)
    lista100.append(szam)
print(len(lista100))
#muxik

# egyszam jatek
jatek_szam=0
nem_talaltdb=0

kitalallado_szam=lista100[random.randint(0,len(lista100))] 

jatszol=True
while jatszol:
    tipp=int(input("Adj egy szamot:"))
    while tipp != kitalallado_szam:
        tipp=int(input("Adj egy szamot:"))

    print('jo a tipp')

    folytatas=input("Akarasz még játszani? [I/N]:")
    if folytatas == "N":
        jatszol=False

