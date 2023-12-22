# BANK MARKETING CAMPAIGN ANALYSIS

## LOAD LIBRARIES
import pandas as pd
import numpy as np

## LOAD DATASET
df_raw = pd.read_csv('bank_dataset.csv', sep =';')

## EDA ANALYSIS
### Preliminary analysis
print(df_raw.head())
print(df_raw.shape)
#### 45211 rows, 17 columns
print(df_raw.info())
#### 45211 non-null for each columns
#### 10 categorical variables and 7 numerical
#### Categorical columns description
for col in df_raw.select_dtypes(include='object').columns:
    print(col)
    print(df_raw[col].unique())
#### Numercial columns basic statistics    
print(df_raw.describe())


### Missing values
missing_values = df_raw.isnull().sum()
print("Missing values: ",missing_values)
#### There are no missing values
df_wrgld = df_raw
print(df_wrgld.head)

############ Altre operazioni di pulizia preliminare?


### CATEGORICAL VARIABLES EXPLORATION

import matplotlib.pyplot as plt
import seaborn as sns

#### Categorical variables
print(df_wrgld.select_dtypes(include='object').columns.to_list())
categorical_variables = ['job', 'marital', 'education', 'default','housing', 'loan', 'contact', 'month', 'poutcome']

#### Setting num_cols and rows
num_cols = 3
num_rows = 3

#### Setting figure dimension
plt.figure(figsize=(15, 10))

#### Create plots with subplot
for i, column in enumerate(categorical_variables, start=1):
    plt.subplot(num_rows, num_cols, i)
    values = df_wrgld[column].value_counts()
    plt.bar(values.index, values, color='skyblue', alpha=0.5)
    plt.xticks(rotation=90)
    plt.title(f'{column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()



### NUMERICAL VARIABLES EXPLORATION
print(df_wrgld.select_dtypes(include='number').columns.to_list())
numerical_variables = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    
#### Setting cols and rows
num_cols = 3
num_rows = 3

#### Setting figure dimension
plt.figure(figsize=(20, 15))

#### Plotting
for i, column in enumerate(numerical_variables, start=1):
    plt.subplot(num_rows, num_cols, i)
    values = df_wrgld[column].value_counts()
    plt.hist(df_wrgld[column], color='skyblue', alpha=0.5, bins=30)
    plt.xticks(rotation=90)
    plt.title(f'{column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


#### Correlation matrix!!!!
#### SI





### DETECT OUTLIERS
df_wrgld[numerical_variables].describe()
#### pdays, campaign and previous columns have outliers
#### pdays has min=-1, let's count how many values compared to the total
count_minus_1 = (df_wrgld['pdays'] == -1).sum()
tot_values = len(df_wrgld['pdays'])
perc_minus_1 = (count_minus_1 / tot_values) *100
print(count_minus_1)
print(perc_minus_1)
#### -"1" possibly means that the client wasn't contacted before 
#### or stands for missing data. Since we are not sure exactly 
#### what -1 means and "-1" values consist of more than 50% of pdays
#### total values, I suggest to drop this column.


#### Check boxplots
num_otlr_vbls = ['campaign', 'previous', 'pdays']
plt.figure(figsize=(15,8))

sns.boxplot(data=df_wrgld[num_otlr_vbls], palette='Set2')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.title('Boxplot to visualize outliers')
plt.show()

#### Scatterplots
from mpl_toolkits.mplot3d import Axes3D
x = df_wrgld['campaign']
y = df_wrgld['previous']
z = df_wrgld['pdays']
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='blue', marker='o', alpha=0.5)

#### Format
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Scatter Plot 3D')

plt.show()


#### LI TRATTO?
#### ELIMINA PDAYS 
#### PLOT TABELLA PER INDAGARE DATO


### Analysis of the response variable "Y"




### DATA PREPARATION AND ENCODING


### PERFORMING ML ALGORITHMS
### regressione logistica
### Decision three
### Random forest


#### FILE ENCODING SCIKIT LEARN

#### DECISION TREE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# Dividi il dataset in variabili indipendenti (X) e variabili dipendenti (y)
X = dataset.drop('variabile_target', axis=1)  # Sostituisci 'variabile_target' con il nome della tua variabile dipendente
y = dataset['variabile_target']

# Dividi il dataset in set di addestramento e test ####### !!!!!!!!!!!!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definisci le colonne da trattare separatamente per la trasformazione
categorical_features = ['cat_var1', 'cat_var2', ..., 'cat_var10']  # Sostituisci con i nomi delle tue variabili categoriche
numeric_features = ['num_var1', 'num_var2', ..., 'num_var7']  # Sostituisci con i nomi delle tue variabili numeriche

# Crea un transformer per le variabili categoriche
categorical_transformer = OneHotEncoder()

# Crea un transformer per le variabili numeriche
numeric_transformer = StandardScaler()

# Combina i transformer in un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),
        ('num', numeric_transformer, numeric_features)
    ])

# Crea il modello di regressione logistica
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', LogisticRegression())])

# Addestra il modello
model.fit(X_train, y_train)

# Effettua le predizioni
y_pred = model.predict(X_test)

# Valuta le performance del modello
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Stampa il report di classificazione
print('Classification Report:')
print(classification_report(y_test, y_pred))



