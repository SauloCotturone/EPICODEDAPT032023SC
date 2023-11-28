## EX3 

### 3.1
stringa = "Epicode"
index = 0
while index < len(stringa):
    print(stringa[index])
    index += 1


### 3.2
numero = 0
while numero <= 20:
    print(numero)
    numero += 1


### 3.3
potenza = 0
while potenza <= 10:
    operazione = 2 ** potenza
    print(operazione)
    potenza += 1
    

### 3.4
N = int(input("Inserisci la potenza che vuoi calcolare: "))

potenza = 0

while potenza <= N:
    operazione =  2 ** potenza
    print(operazione)
    potenza += 1
    
    
### 3.5
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend"]

if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza")
else:
    print("Le liste hanno lunghezze differenti")


### 3.6
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]
corsi.append("Frontend")
corsi.append("Cybersecurity")

if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza")
else:
    print("Le liste hanno lunghezze differenti")


### 3.7
stringa_input = input("Scrivi quì la parola: ")
lunghezza = len(stringa_input)
if lunghezza <= 6:
    print("Inserisci una stringa più lunga")
else:
    primi_tre_car  = stringa_input[:3]
    ultimi_tre_car = stringa_input[-3:]
    print(f"{primi_tre_car}...{ultimi_tre_car}")
    

### 3.8
numero_test = int(input("Scrivi quì il numero: "))

fattore = []
for i in range(2, numero_test+1):
    while numero_test % i == 0:
        fattore.append(numero_test)
        numero_test //= i
print(f"I fattori di {numero_test} sono {fattore}")
  
    
    
    


    
    
    