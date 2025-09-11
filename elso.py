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
ktalallado_szam=lista100[random.randint(len(lista100))] 

tipp=int(input("Tipped?: (egész szám)"))
while (tipp != kitalalando_szam):

    tipp=int(input("Tipped?: (egész szám) "))
    print("Eltaláltad a számot!")

folytatas = input("Akarsz-e még játszani? [I/N]:")

if (folytatas == "I"):
    #??????????

else:
    exit ()