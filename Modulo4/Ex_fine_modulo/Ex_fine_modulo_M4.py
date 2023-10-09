### EX FINE MODULO M4

# IMPORT LIBRARIES
import pandas as pd

# PATH
path = "owid_covid_data.csv"

# LOAD DATASET
df = pd.read_csv(path)

# EDA
"""
Si richiede di verificare le dimensioni del dataset e le diciture presenti nell'intestazione
"""
print(df.head())
dimensioni = df.shape
print(dimensioni)
nomi_colonne = df.columns.tolist()
for i in nomi_colonne:
    print(f"{i}\n")
print(df.dtypes)
print(df.info)
print(df.sample(10))

continenti_univoci = df["continent"].dropna().unique()
print(continenti_univoci)

# TASK NR.1
"""
Si chiede poi per ogni continente di trovare il numero di casi totali avvenuti in quello 
stesso continente; si chiede di non considerare eventuali locazioni che nel dataset non 
appartengono ad alcun continente.
"""
df_continenti = df.loc[df["continent"].notna(), ["continent", "date","total_cases"]]
print(df_continenti)

tot_casi_2023_per_continente = df_continenti.groupby("continent")["total_cases"].last()
print(tot_casi_per_continente)

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

## TASK NR.2
"""
Sempre riguardo i casi di COVID totali, si chiede di sviluppare una funzione 
che prenda in input il dataset e due nomi di continenti, e che ne confronti i seguenti 
relativi descrittori statistici: valori minimo e massimo, media, e percentuale 
rispetto al numero dei casi totali nel mondo (in questo caso calcolati anche 
sulle locazioni senza indicazione di continente)
"""
def confronto_indicatori(df, continente_1, continente_2, parametro):
    
    somma_casi_totali = float(tot_casi.sum())
    print(somma_casi_totali)
    
    continente_1 = df_continenti[df_continenti['continent'] == 'North America']
    nome_continente_1 = continente_1['continent'].iloc[0]
    continente_2 = df_continenti[df_continenti['continent'] == 'South America']
    nome_continente_2 = continente_2['continent'].iloc[0]
    
    min_c1 = continente_1[parametro].dropna().min()
    max_c1 = continente_1[parametro].dropna().max()
    mean_c1 = continente_1[parametro].dropna().mean().round(2)
    
    min_c2 = continente_2[parametro].dropna().min()
    max_c2 = continente_2[parametro].dropna().max()
    mean_c2 = continente_2[parametro].dropna().mean().round(2)
    
    perc_sul_tot_c1 = (continente_1[parametro].sum()/somma_casi_totali) * 100
    perc_sul_tot_c1 = perc_sul_tot_c1.round(2)
    perc_sul_tot_c2 = (continente_2[parametro].sum()/somma_casi_totali) * 100
    perc_sul_tot_c2 = perc_sul_tot_c2.round(2)
    
    osservazioni = {
        'Continente 1': nome_continente_1,
        'Minimo North America': min_c1,
        'Massimo North America': max_c1,
        'Media North America': mean_c1,
        'Percentuale sul totale North America': perc_sul_tot_c1,
        'Continente 2': nome_continente_2,
        'Minimo Continente 2': min_c2,
        'Massimo Continente 2': max_c2,
        'Media Continente 2': mean_c2,
        'Percentuale Continente 2': perc_sul_tot_c2,
    }

    return osservazioni

## Chiamo la funzione
confronto_casi_totali = confronto_indicatori(df, 'Nort America', 'South America', "total_cases")

## Output risultati della funzione
for x,y in confronto_casi_totali.items():
    print(f"{x} = {y}")
    

## TASK NR. 3
"""
Si chiede poi di effettuare lo stesso tipo di analisi - anche in questo caso sviluppando 
una funzione ad hoc - per il numero di vaccinazioni totali per ogni continente
""" 
confronto_vaccinazioni = confronto_indicatori(df, 'Nort America', 'South America', "total_vaccinations")

## Output risultati della funzione
for x,y in confronto_vaccinazioni.items():
    print(f"{x} = {y}")


# TASK NR.4 ANALISI SU TRE CONTINENTI
"""
Alla fine, basandosi sui calcoli fatti, il committente chiede di stilare un breve 
(tre o quattro righe) paragrafo testuale riassuntivo sulle statistiche di casi e vaccinazioni, 
che si concentri solo sulle differenze esistenti tra Europa, Sud America e Oceania.
"""
def analisi_continente(df, continenti, casi, vaccini):
    risultati = {}
    #### Definisco il data frame
    df_continenti = df.loc[df["continent"].notna(), ["continent", "date","total_cases", "total_vaccinations"]]
    #### Periodo di osservazione
    start_osserv = df_continenti["date"].min()
    end_osserv = df_continenti["date"].max()
    periodo_osserv = f"Il periodo di osservazione va dal {start_osserv} al {end_osserv}"
    print(periodo_osserv)
    #### calcolo il totale dei casi
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
    
    
analisi_report = f"Dall'analisi perpetrata abbiamo raccolto le seguenti evidenze:\n"
analisi_report += "nell'arco temporale delle osservazioni (dal 2020-01-01 al 2023-10-05)\n"
analisi_report += "sono stati registrati un numero totale di casi a livello globale pari a 771 mln ca\n"
analisi_report += "ed una campagna di vaccinazione che conta più di 10 mlrd ca di vaccini.\n"
analisi_report += "Confrontando Europa, Sud America e Oceania possiamo notare che il numero totale dei casi\n"
analisi_report += "per l'Europa è stato maggiore rispetto agli altri continenti in analisi, con 250 mln ca di casi\n"
analisi_report += "pari a circa 1/3 del totale globale.\n"
analisi_report += "Parallelamente, anche lato vaccinazioni, l'Europa rispetto a Sud America ed Oceania\n"  
analisi_report += "ha registrato più di 1 mlrd ca di vaccini pari al 12% ca delle vaccinazioni globali\n"  
analisi_report += "Analizzando il rapporto casi/vaccini l'Europa e l'Oceania registrano un indicatore\n"
analisi_report += "simile, pari a 20 casi ca ogni vaccino, mentre il Su America mostra un dato di conversione\n"  
analisi_report += "dei vaccini più positivo, il quale, in maniera puramente speculativa, potrebbe indicare\n"
analisi_report += "una maggiore efficacia della campagna di vaccinazione o una registrazione meno puntuale\n"
analisi_report += "dei casi rispetto agli altri continenti."

print(analisi_report)