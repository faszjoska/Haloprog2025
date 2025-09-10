import random


# lista létrehozasa
lista100=[]

# lista feltoltese random 100 db ketjegyu szamokkal
for i in range(100):
    szam=random.randint(10,99)
    lista100.append(szam)
print(len(lista100))
#muxik