verseny_adatok=[]


try: 
    with open("F1-2024dec.csv",encoding="utf-8")as falj:
        
        for sor in falj:
            verseny_adatok.append(sor)
except IOError as ex:
    print(f"falj hiba{ex}")

"""
    1. [✔] Sorozatszámítás/összegzés
    2. [✔] Kiválasztás
    3. [✔] Megszámolás
    4. [✔] Eldöntés 1
       [✔] Eldöntés 2
    5. [✔] Maximum/minimum kiválasztás
    6. [] Keresés (lineáris)
    
    7. [] Kiválogatás (külön, helyben)
    8. [] Szétválogatás
    9. [] Unió
    10.[] Metszet
    
    11. Rendezés
       [] egyszerű cserés
       [] buborékos
       [] minimumkiválasztásos
    """

#1.
osszeg=0
db=len(verseny_adatok)-1
for i in range (1,len(verseny_adatok)):
    sor=verseny_adatok[i].split(",")
    osszeg=osszeg+int(sor[1])


atlag=osszeg/db
print(f"{atlag}az átlag pontszám")

#2. Mi a bekért versenyzo adatai?
pilota=input("Kérek egy pilótát:")
ciklusvaltozo=1
while verseny_adatok[ciklusvaltozo].split(",")[0]!=pilota:
    ciklusvaltozo+=1
print(verseny_adatok[ciklusvaltozo])

#3.
db1=0
for i in range (1,len(verseny_adatok)):
    if int(verseny_adatok[i].split(",")[1])>300:
        db1+=1
print(db1)

#4.1 Van-e 0 pntos versenyző?
'''
ciklusvaltozo=1
while ciklusvaltozo<len(verseny_adatok) and int(verseny_adatok[ciklusvaltozo].split(",")[1])>0:
    ciklusvaltozo+=1
if ciklusvaltozo<len(verseny_adatok):
    print("Van 0 pontos versenyző")
else:
    print("Nincs 0 pontos versenyző")
'''
#4.2 Mindenki szerzett pontot a 2024-es szezon alatt?
ciklusvaltozo=1
while ciklusvaltozo<len(verseny_adatok) and int(verseny_adatok[ciklusvaltozo].split(",")[1])>0:
    ciklusvaltozo+=1
print(ciklusvaltozo)
if ciklusvaltozo>=len(verseny_adatok):
    print("MINDEKI SZERZETT PONTOT A 2024-ES SZEZON ALATT😎")
else:
    print("VAN OLYAN AKI NEM SZERZETT PONTOT A 2024-ES SZEZON ALATT😆")

#5. Ki vezeti a 2024-es szezon világbajnokságát?
max_ertek=int(verseny_adatok[1].split(",")[1])
max_index=1
for i in range(2,len(verseny_adatok)):
    if int(verseny_adatok[i].split(",")[1])>max_ertek:
        max_index=i
        max_ertek=int(verseny_adatok[i].split(",")[1])
print(f"{verseny_adatok[max_index].split(",")[0]} vezeti a 2024-es világbajnokságot. ")

