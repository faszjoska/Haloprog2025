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
kitalallado_szam=lista100[random.randint(len(lista100))] 
tipp=int(input("Adj egy szamot:"))
while tipp != kitalallado_szam:
    ujtipp=int(input("Uj tipp:"))

print('jo a tipp')
tobbjatek=input("akarsz meg jatszani?[i/n]:")
if (tobbjatek== 'i'):
    #ez itt  abaj
else:
    exit()    

