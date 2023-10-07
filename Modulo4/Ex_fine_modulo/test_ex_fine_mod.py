# COVID CASES

## IMPORT PANDAS
import pandas as pd

## PATH
path = "owid_covid_data.csv"

## LOAD DATA
df = pd.read_csv(path)

## EXPLORATION DF
df.shape
df.head()
df.sample(10)
nomi_colonne = df.columns.tolist()
for i in nomi_colonne:
    print(f"{i}\n")

## TASK NR. 1
"""
Si chiede poi per ogni continente di trovare il numero di casi totali avvenuti in quello 
stesso continente; si chiede di non considerare eventuali locazioni che nel dataset non 
appartengono ad alcun continente.
"""
df_continenti = df.loc[df["continent"].notna(), ["continent", "date","total_cases"]]
print(df_continenti)

tot_casi_2023_per_continente = df_continenti.groupby("continent")["total_cases"].last()
print(tot_casi_2023_per_continente)

### Essendo casi cumulativi di una serie temproale, per ottenere i casi totali avvenuti durante l'arco
### temporale analizzato, bisogna calcolare la differenza tra i dati cumulativi in giorni successivi

#### per prima cosa convertiamo la serie di dati "date" in tipo datetime
df_continenti["date"] = pd.to_datetime(df_continenti["date"])
#### calcoliamo la variazione giornaliera dei casi
diff_tot_casi = df_continenti["total_cases"].diff()
#### sommiamo i dati ottenuti per ottenere il totale dei casi senza cumulazione
tot_casi = diff_tot_casi.sum()
print(tot_casi)
#### troviamo il numero di casi totali durante l'arco temporale di osservazione per ogni continente
df_continenti["variazione"] = df_continenti.groupby("continent")["total_cases"].diff()
tot_casi_per_continente =  df_continenti.groupby("continent")["variazione"].sum()
print(tot_casi_per_continente)
#### Li rappresento graficamente
import matplotlib.pyplot as plt
x = tot_casi_per_continente.index
y = tot_casi_per_continente.values
plt.bar(x, y, color = "blue", alpha = 0.8)
plt.title("Tot casi per continente")
plt.tight_layout()



"""
Alla fine, basandosi sui calcoli fatti, il committente chiede di stilare un breve 
(tre o quattro righe) paragrafo testuale riassuntivo sulle statistiche di casi e vaccinazioni, 
che si concentri solo sulle differenze esistenti tra Europa, Sud America e Oceania.
"""
def analisi_continente(df, continenti, casi, vaccini):
    risultati = {}
    #### calcolo il totale dei casi
    df_continenti = df.loc[df["continent"].notna(), ["continent", "date","total_cases", "total_vaccinations"]]
    diff_tot_casi = df_continenti[casi].diff()
    tot_casi = diff_tot_casi.sum()
    risultati["tot_casi"] = tot_casi
    
    #### calcolo il totale delle vacinazioni
    diff_tot_vaccini = df_continenti[vaccini].diff()
    tot_vaccini = diff_tot_vaccini.sum()
    risultati["tot_vaccini"] = tot_vaccini

    #### calcolo il numero di casi per ogni continente
    for continente in continenti:
    #### Creiamo una copia del sottoinsieme di dataframe creato per evitare che modifiche allo stesso
    #### possano influenzare il dataframe originale   
        df_continenti = df[df["continent"]==continente].copy()
    #### calcolo il numero di casi per ogni continente in analisi 
        df_continenti["diff_casi"] = df_continenti[casi].diff()
        tot_casi_per_continente = df_continenti["diff_casi"].sum()
        risultati[f"Totale Casi {continente}"] = tot_casi_per_continente
        
    #### calcolo il numero di vaccinazioni per ogni continente in analisi
        df_continenti["diff_vaccini"] =df_continenti[vaccini].diff()
        tot_vaccini_per_continente = df_continenti["diff_vaccini"].sum()
        risultati[f"Totale Vaccini {continente}"] = tot_vaccini_per_continente
        
    #### calcolo la % dei casi di ogni continente con il totale dei casi
        perc_casi = (tot_casi_per_continente / tot_casi) * 100
        risultati[f"% Casi {continente} rispetto al totale casi"] = f"{perc_casi:.2f}%"
    
    #### calcolo la % di vaccini di ogni continente con il totale dei vaccini
        perc_vaccini = (tot_vaccini_per_continente / tot_vaccini) * 100
        risultati[f"% Vaccini {continente} rispetto al totale vaccini"] = f"{perc_vaccini:.2f}%"
    
    #### calcolo il rapporto tra numero di casi e vaccini per ogni continente
        rapporto_casi_vaccini = (tot_casi_per_continente/tot_vaccini_per_continente)*100
        risultati[f"Rapporto Casi/Vaccini {continente}"] = f"{rapporto_casi_vaccini:.2f}"
        
    return risultati
    
### Chiamo la funzione
continenti_target = ["Europe", "South America", "Oceania"]
risultato_analisi_continenti = analisi_continente(df, continenti_target, "total_cases", "total_vaccinations")

### Stampo i risultati
for chiave, valore in risultato_analisi_continenti.items():
    print(f"{chiave}: {valore}")
    
        
 
