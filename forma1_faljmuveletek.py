verseny_adatok=[]


try: 
    with open("F1-2024dec.csv",encoding="utf-8")as falj:
        
        for sor in falj:
            verseny_adatok.append(sor)
except IOError as ex:
    print(f"falj hiba{ex}")

""" 
    1. sorozatszammitas 
    2. kiválasztás
    3. megszámlálás
    4. eldöntés
    5. szétválogatás
    6. max/min
    7. keresés
    8. rendezés
    9. kiválogatás
    10. unio 
    11. metszet 
   
    
     
      
"""


#1.
osszeg=0
db=len(verseny_adatok)-1
for i in range (1,len(verseny_adatok)):
    sor=verseny_adatok[i].split(",")
    osszeg=osszeg+int(sor[1])


atlag=osszeg/db
print(f"{atlag}az átlag pontszám")

