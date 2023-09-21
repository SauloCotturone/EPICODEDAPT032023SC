
### Ex 2

### 2.1
scuola = "Epicode"
print(scuola[0])
print(scuola[0:3])
scuola_maiusc = scuola.upper()
print(scuola_maiusc)


### 2.2
x = 10
x += 2
x = x*3
print(x)

### 2.3
litri_nel_serbatoio  = float(input("Litri nel serbatoio: "))
efficienza_km_litri  = float(input("Efficienza km/l pari a: "))
prezzo_benzina_litro = float(input("Prezzo per litro: "))
costo_100_km = (100/efficienza_km_litri) * prezzo_benzina_litro
print("Il costo per 100 km è pari a: ", costo_100_km)

### 2.4
nome_animale = input("Il mio animale preferito è il: ")
print(nome_animale[:3, "...", -3:])

### 2.5
stringhe =["Epicode", "Windows", "Excel", "Powerpoint", "Word"]
for stringa in stringhe:
    lunghezza_stringa = len(stringa)
    if 5 >= lunghezza_stringa <= 8:
        print("La stringa", stringa, "ha un numero di caratteri compreso tra 5 e 8") 
    else:
        print("La stringa", stringa, "ha un numero di caratteri minore di 5 o maggiore di 8")

      
### 2.6
codici_prodotto = ["knt-S1", "cba-G9", "qtr-Z8"]
codice_1 = codici_prodotto[0][-3:]
codice_2 = codici_prodotto[1][-3:]
codice_3 = codici_prodotto[2][-3:]
print(codice_1)
print(codice_2)
print(codice_3)


##

    
    
    
