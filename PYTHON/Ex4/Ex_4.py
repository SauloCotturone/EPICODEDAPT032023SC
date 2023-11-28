## EX_4
    
### 4.1
"""
Esercizio
Abbiamo la stringa:
nome_scuola = "Epicode"
Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto 
for.
"""
nome_scuola = "Epicode"

for carattere in nome_scuola:
    print(carattere)


### 4.2
"""Esercizio
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera) 
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa.
"""
elementi = "NPKOHC"

for elemento in elementi:
    print(elemento)


### 4.3
"""Esercizio
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera) 
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento 
–".
"""
elementi = "NPKOHC"

for elemento in elementi:
    print("elemento-",elemento, sep="")


### 4.4
"""Esercizio
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera) 
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento 
– numero n" dove al posto di n scriveremo un numero progressivo che parte 
da 1
elementi = "NPKOHC"
numero = 1
"""
for elemento in elementi:
        print("elemento-",elemento,"numero",numero)
        numero += 1


### 4.5
"""Esercizio
Modificare la parola "marmalade" in modo sostituire le "e" con le "a" e 
viceversa.
Salvare il risultato in una variabile e stamparla a video.
Fare diverse versioni: 
• una con un ciclo for,
• una con un ciclo while,
• una con il metodo delle stringhe .replace()
"""
parola = "marmalade"
nuova_parola = ""

## costrutto for
for i in parola:
    if i == "a":
        nuova_parola += "e"
    elif i == "e":
        nuova_parola += "a"
    else:
        nuova_parola += i
print(nuova_parola)

## costrutto while
parola = "marmalade"
nuova_parola = ""
contatore = 0
while contatore < len(parola):
    if parola[contatore] == "a":
        nuova_parola += "e"
    elif parola[contatore] == "e":
        nuova_parola += "a"
    else:
        nuova_parola += parola[contatore]
    contatore += 1
print(nuova_parola) 

## metodo delle stringhe
parola = "marmalade"
nuova_parola = parola.replace("e", "i")
nuova_parola = nuova_parola.replace("a", "e")
nuova_parola = nuova_parola.replace("i", "a")
print(nuova_parola)


### 4.6
"""
Esercizio
Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo for.
Utilizzeremo:
• la funzione range(), e.g.:
for contatore in range(10):
pass # modificare qui
"""
for numero in range(10):
    potenze_di_due = 2**numero
    print(potenze_di_due)


### 4.7
"""Calcolare (ma non stampare) le prime N potenze di 2; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for."""
## costrutto while
N = 10
numero = 0
potenze_list = []
while numero < N:
    potenza = 2 **numero
    potenze_list.append(potenza)
    numero += 1
print(potenze_list)

## costrutto for
N = 10
potenze_list = []
for i in range(N):
    potenza = 2**i
    potenze_list.append(potenza)
print(potenze_list)


### 4.8
"""Calcolare (ma non stampare) le prime N potenze di 3; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for"""
## costrutto while
N = 10
contatore = 0
potenza_tre_lista = []
while contatore < N:
    potenza_tre = 3**contatore
    potenza_tre_lista.append(potenza_tre)
    contatore += 1
print(potenza_tre_lista)

## costrutto for
N = 10
potenza_tre_lista = []
for i in range(N):
    potenza_tre = 3**i
    potenza_tre_lista.append(potenza_tre)
print(potenza_tre_lista)


### 4.9
"""
Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Proviamo con diversi valori di K, oppure facciamola inserire all'utente.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for
"""
## costrutto while
K = int(input("Inserisci un valore: "))
N = 10
contatore = 0
potenza_k_lista = []
while contatore < N:
    potenza_di_k = K**contatore
    potenza_k_lista.append(potenza_di_k)
    contatore += 1
print(potenza_k_lista)

## costrutto for
K = int(input("Inserisci un valore: "))
N = 10
potenza_k_lista = []
for i in range(N):
    potenza_di_k = K**i
    potenza_k_lista.append(potenza_di_k)
print(potenza_k_lista)


### 4.10
"""
Calcolare e stampare tutte le potenze di 2 
minori di 25000
"""
x = 2
potenza = 0
while x**potenza <= 25000:
    print(x**potenza)
    potenza += 1


### 4.11
"""
Calcolare e stampare tutte le 
potenze di 2 minori di un certo numero N
"""
N = int(input("Inserisci un valore: "))
potenza = 0
while x**potenza <= N:
    print(x**potenza)
    potenza += 1
    

### 4.12
"""
Calcolare e stampare tutte le prime 100 potenze di 2, ogni 3 (e.g. 2⁰, 2³, 2⁶, 2⁹,
…).
Oltre a stamparle, memorizzarle in coda a una lista e stamparla alla fine.
Usate due metodi diversi:
1. usare un costrutto for e range(100), e poi un costrutto if per visualizzare
e memorizzare solo ogni 3
2. usare un costrutto for e range(0, 100, 3)
"""
potenze = []
for i in range(0, 100, 3):
    potenza = 2**i
    print(f"2^{i} = {potenza}")
    potenze.append(potenza)
    
print(potenze)


### 4.13
"""
Abbiamo una lista con dei numeri: numeri = [4, 9, 5, 1, 7, 10, 2, 3]
utilizzando un costrutto for, trovare il massimo di questa lista e stamparlo a
video
"""
max = 0
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
for i in numeri:
    if i > max:
        max = i
print(max)


### 4.14
"""
Abbiamo raccolto tutte le età degli studenti in una lista:
eta_studenti = [20, 30, 40, 50, 60]
utilizzando un ciclo for, calcolare la media delle età. Alla fine, stampa (a video)
il risultato
"""
x = 0
eta_studenti = [20, 30, 40, 50, 60]
for i in eta_studenti:
    x += i
print(float((x/len(eta_studenti))))


### 4.15
"""
Abbiamo una lista con i guadagni degli ultimi 12 mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video
"""
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
x = 0
for i in guadagni:
    x += i
avg = x/len(guadagni)
print(f"La media dei guadagni è {avg}")


### 4.16
"""
Abbiamo una lista con i guadagni degli ultimi N mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video;
stampare anche il numero di mesi considerati
"""
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
x = 0
for i in guadagni:
    x += i
avg = x/len(guadagni)
mesi = len(guadagni)
print(f"La media dei guadagni in {mesi} mesi è stata {avg}")


### 4.17
"""
Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
utilizzare un ciclo for per stampare i nomi di tutti gli studenti con questa formattazione:
Studenti:
- Alex
- Bob
- Cindy
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
for i in studenti:
    print(f"- {i}\n")
    

### 4.18
"""
Abbiamo tre liste (sono tutte della stessa lunghezza):
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
stampare a video, usando print(), ogni studente che corso segue e di che edizione,
e.g.:
Alex segue Cybersecurity, edizione 1
Bob segue Data Analyst, edizione 2
...
facendo in modo che non ci sia uno spazio tra il corso e la virgola subito dopo
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
for i,x,y in zip(studenti, corsi, edizioni):
    print(f"{i} segue {x}, edizione {y}")
    

### 4.19
"""
Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo",
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
stampiamo, per ogni parola, quante volte appare la lettera "e"
"""
parole = ["Albergo", "Sedia", "Borgo", "Petalo", 
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
n = []
for i in parole:
    n.append(i.count("e"))

for i in range(len(parole)):
    print(f"Nella parola '{parole[i]}' la lettera 'e' appare {n[i]} volte.")
    

### 4.20
"""
Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo",
"Belvedere", "Semestre", "Esteta", "Sosta", "Orpello",
"Abete", "Orologio", "Cesta", "Ermellino"]
stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo
attenzione al fatto che appare sia maiuscola che minuscola
"""
parole = ["Albergo", "Sedia", "Borgo", "Petalo", 
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
n = []
for i in parole:
    n.append(i.lower().count("e"))

for i in range(len(parole)):
    print(f"Nella parola '{parole[i]}' la lettera 'e' appare {n[i]} volte.")
    

### 4.21
"""
Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine
stamparla
"""
lista = []
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C","MNOPQR89S03A456D", 
"STUVWX95Z04A654E", "XYZABC01D05A789F","DEFGHI95J06A987G"]
for i in lista_cf:
    if "95" in i:
        lista.append(i)

print(lista)


### 4.22
"""
Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
Per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al
cognome
"""
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C","MNOPQR89S03A456D", 
"STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
for i in lista_cf:
    print(f"Nome: {i[:3]} - Cognome: {i[3:6]}")
    

### 4.23
"""
Abbiamo tre liste della stessa lunghezza:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Stampare a video tutti e soli gli studenti che frequentano una prima edizione; utilizzare
solo i dati necessari
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
for x,y in zip(studenti, edizioni):
    if y == 1:
        print(x)
        

### 4.24
"""
Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo
che:
• Ada guida una Punto
• Ben guida una Multipla
• Charlie guida una Golf
• Debbie guida una 107 Poi stampiamo il dizionario per intero, e poi l'auto
associata a Debbie
"""
dir = {"Ada":"Punto",
       "Ben":"Multipla",
       "Charlie":"Golf",
       "Debbie":"107"}
print(dir)
auto_debbie = dir["Debbie"]
print(f"Debbie guida una {auto_debbie}")


### 4.25
"""
Abbiamo un dizionario che assegni ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Aggiungere i proprietari Emily e Fred che posseggono 
rispettivamente una A1 e
una Octavia; eliminare i dati relativi a Ben.
Stampare il dizionario per controllare che sia 
tutto corretto
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
dizionario_auto.update({"Emily":"A1", "Fred":"Octavia"})
print(dizionario_auto)
dizionario_auto.pop("Ben")
print(dizionario_auto)


### 4.26
"""
Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia",
"Grace": "Yaris", "Hugh": "Clio"}
Aggiornare il dizionario dizionario_auto con i dati contenuti in
nuovi_proprietari e stamparlo. Cosa è successo a Ben?
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia",
"Grace": "Yaris", "Hugh": "Clio"}
dizionario_auto.update(nuovi_proprietari)
print(dizionario_auto)
## Aa Ben è stata assegnata la nuova auto "Polo" nel 
## dizionario aggiornato


### 4.27
"""
Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma
di dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e
Debbie, e visualizzare le auto relative
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}
proprietari_da_cercare = ["Hugh", "Ada", "Emily", "Debbie"]
for i in proprietari_da_cercare:
    if i in dizionario_auto:
        output = dizionario_auto[i]
        print(f"{i} guida una {output}")
    else:
        print(f"{i} non trovato nel dizionario")
        
        
### 4.28
"""
Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di
dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e
Charlie, e visualizzare le auto relative.
Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è
presente visualizzeremo un messaggio adeguato
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}
proprietari_da_cercare = ["Ada", "Emily", "Jade", "Ben", "Hugh", 
"Kelly", "Charlie"]
for i in proprietari_da_cercare:
    if i in dizionario_auto:
        output = dizionario_auto[i]
        print(f"{i} guida una {output}")
    else:
        print(f"{i} non trovato nel dizionario")
        

### 4.29
"""
Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .keys(), stampiamone tutte le chiavi
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
print(diz.keys())


### 4.30
"""
Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .values(), stampiamone tutte i valori
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
print(diz.values())


### 4.31
"""
Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore
presenti nel dizionario su righe diverse
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
for i, j in diz.items():
    print(f"{i}:{j}")


### 4.32
"""
Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il
valore minimo, la somma, e stampiamo i risultati
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
valori = diz.values()
massimo = max(valori)
minimo = min(valori)
somma = sum(valori)
print(f"Il valore massimo è {massimo}, minimo {minimo}, somma {somma}")



### 4.33
"""
Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario
e la sua auto, formattandolo come:
Ada guida una Punto
Ben guida una Multipla
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
for i,j in dizionario_auto.items():
    print(f"{i} guida una {j}")


### 4.34
"""
Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto
che non sono una Multipla
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
for i in dizionario_auto.values():
    if i != "Multipla":
        print(i)


### 4.35
"""
Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
• Charlie ha 31 action figures e 18 graphic novels
• Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi 
visualizzarli
"""
diz_collezione = {
    "Ada":
        {"Funko Pop":10,
         "Action figures":5,
         "Manga": 35
         },
    "Ben":
        {"Funko Pop":2,
         "Action figures":6,
         "Manga": 40,
         "Graphic novels":2
          },
    "Charlie":
        {"Action Figures": 31,
        "Graphic Novels": 18
        },
    "Debbie": {
        "Funko Pop": 1,
        "Graphic Novels": 9,
        "Manga": 25,
        "Action Figures": 2
        } 
}
for i,x in diz_collezione.items():
    print(f"{i} ha la seguente collezione:")
    for y,j in x.items():
        print(f"- {y} {j}")


### 4.36
"""
Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe
della DC)
• Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8
della DC)
• Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel),
25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli
"""
Ada = {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    }

Ben = {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": {
            "DC": 2
        }
    }

Charlie = {
        "Action Figures": 31,
        "Graphic Novels": {
            "Marvel": 10,
            "DC": 8
        }
    }

Debbie = {
        "Funko Pop": 1,
        "Graphic Novels": {
            "DC": 4,
            "Marvel": 5
        },
        "Manga": 25,
        "Action Figures": 2
    }
dir_collezionisti = {"Ada": Ada,
                     "Ben": Ben,
                     "Charlie": Charlie,
                     "Debbie": Debbie}

for nome,collezione in dir_collezionisti.items():
    print(f"{nome} possiede la seguente collezione:")
    for tipologia,info_aggiuntive in collezione.items():
        if isinstance(info_aggiuntive, int):
            print(f"{tipologia} nr. {info_aggiuntive}")
        else:
            print(f"{tipologia}")
            for sotto_categoria, numero_elementi in info_aggiuntive.items():
                print(f"- di cui {numero_elementi} della {sotto_categoria}")
                
                
### 4.37
"""
Riguardo l'esercizio precedente, stampiamo le risposte a:
1. quanti Funko Pop ha Ada?
2. quanti manga ha Ben?
3. quante graphic novels della Marvel ha Debbie?
4. quanti Funko Pop hanno Ada e Ben in tutto?
5. quanti manga hanno in tutto i collezionisti?
6. quante graphic novel della DC hanno in tutto i collezionisti?
7. quante graphic novel hanno in tutto i collezionisti?
"""
## 1. quanti Funko Pop ha Ada?
Ada = {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    }
for x,y in Ada.items():
    if x == "Funko Pop":
        print(y)

## 2. quanti manga ha Ben?
Ben = {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": {
            "DC": 2
        }
    }
for oggetto, quantià in Ben.items():
    if oggetto == "Manga":
        print(quantià)

## 3. quante graphic novels della Marvel ha Debbie?
Debbie = {
        "Funko Pop": 1,
        "Graphic Novels": {
            "DC": 4,
            "Marvel": 5
        },
        "Manga": 25,
        "Action Figures": 2
    }
for oggetto, quantità in Debbie.items():
    if oggetto == "Graphic Novels":
        if isinstance(quantità, int):
            print("cane")
        else:
            print(f"{oggetto}:")
            for sotto_categoria, numeri in quantità.items():
                print(f"di cui {numeri} {sotto_categoria}")


## 4. quanti Funko Pop hanno Ada e Ben in tutto?
Ada = {
        "Funko Pop": 10,
        "Action Figures": 5,
        "Manga": 35
    }

Ben = {
        "Funko Pop": 2,
        "Action Figures": 6,
        "Manga": 40,
        "Graphic Novels": {
            "DC": 2
        }
    }

tot_funko_pop = Ada["Funko Pop"] + Ben["Funko Pop"]
print(tot_funko_pop)

## 5. quanti manga hanno in tutto i collezionisti?
tot_manga = 0
for nome, collezione in dir_collezionisti.items():
        if "Manga" in collezione:
            tot_manga += collezione["Manga"]
print(f"I collezionisti hanno in tutto {tot_manga} Manga")
            
## 6. quante graphic novel della DC hanno in tutto i collezionisti?        
tot_graphic_novels_dc = 0
for nome, collezione in dir_collezionisti.items():
    if "Graphic Novels" in collezione:
        graphic_novels = collezione["Graphic Novels"]
        if "DC" in graphic_novels:
            tot_graphic_novels_dc += graphic_novels["DC"]

print(f"I collezionisti hanno in tutto {tot_graphic_novels_dc} Graphic Novels della DC")

## 7. quante graphic novel hanno in tutto i collezionisti?
tot_graphic_novels = 0
for nome, collezione in dir_collezionisti.items():
    if "Graphic Novels" in collezione:
        graphic_novels = collezione["Graphic Novels"]
        for value in graphic_novels.values():
            tot_graphic_novels += value
        
print(f"I collezionisti hanno in tutto {tot_graphic_novels} Graphic Novels!")


for nome, collezione in dir_collezionisti.items():
    if "Graphic Novels" in collezione:
        graphic_novels = collezione["Graphic Novels"]
print(graphic_novels)
   
                     
                



