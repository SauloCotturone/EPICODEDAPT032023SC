# BANK MARKETING CAMPAIGN ANALYSIS

## LOAD LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
df_raw.describe()


### Missing values
missing_values = df_raw.isnull().sum()
print("Missing values: ",missing_values)
#### There are no missing values
df_wrgld = df_raw
print(df_wrgld.head)



### CATEGORICAL VARIABLES EXPLORATION

#### Categorical variables
print(df_wrgld.select_dtypes(include='object').columns.to_list())
categorical_variables = ['job', 'marital', 'education', 'default','housing', 'loan', 'contact', 'month', 'poutcome']

#### Setting num_cols and rows
num_cols = 3
num_rows = 3

#### Setting figure dimension
plt.figure(figsize=(15, 10))

#### Create plots with 
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
df_wrgld[numerical_variables].describe()

#### Plotting
#### Setting cols and rows
num_cols = 3
num_rows = 3

#### Setting figure dimension
plt.figure(figsize=(20, 15))

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



### DETECT OUTLIERS     
df_wrgld[numerical_variables].describe()
#### pdays, campaign and previous columns have outliers

#### Check boxplots
num_otlr_vbls = ['campaign', 'previous', 'pdays']
plt.figure(figsize=(15,8))

sns.boxplot(data=df_wrgld[num_otlr_vbls], palette='Set2')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.8)
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


### Pdays has min=-1, let's count how many values compared to the total
count_minus_1 = (df_wrgld['pdays'] == -1).sum()
tot_values = len(df_wrgld['pdays'])
perc_minus_1 = (count_minus_1 / tot_values) *100
print(count_minus_1)
print(perc_minus_1)
#### -"1" possibly means that the client wasn't contacted before 
#### or stands for missing data. Since we are not sure exactly 
#### what -1 means and "-1" values consist of more than 50% of pdays
#### total values, I suggest to drop this column.
df_wrgld = df_wrgld.drop('pdays', axis=1)
#### check
print(df_wrgld.head())
numerical_variables =  ['age', 'balance', 'day', 'duration', 'campaign', 'previous']


#### Checking % of values in Campaign & Previosu greater than 10
print(len (df_wrgld[df_wrgld['campaign'] > 10]) / len(df_wrgld) * 100)
print(len (df_wrgld[df_wrgld['previous'] > 10]) / len(df_wrgld) * 100)
#### Substituting values above 30 with the variable mean
subst_outliers = ['campaign', 'previous']
for var in subst_outliers:
    mean_value = df_wrgld[var].median()
    df_wrgld.loc[df_wrgld[var] > 10, var] = mean_value

df_wrgld[numerical_variables].describe()


### Duration
#### duration: last contact duration, in seconds (numeric). Important note: this attribute 
#### highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is 
#### not known before a call is performed. Also, after the end of the call y is obviously known. 
#### Thus, this input should only be included for benchmark purposes and should be discarded if 
#### the intention is to have a realistic predictive model.
df_wrgld = df_wrgld.drop('duration', axis=1)
print(df_wrgld.head())



### Analysis of the response variable "Y"
#### Categorical variables
value_counts = df_wrgld['y'].value_counts()
value_counts.plot.bar(title = 'Deposit value counts')

colors = sns.color_palette(['#001F3F', '#87CEEB']) 
for var in categorical_variables:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=var, hue='y', data=df_wrgld, order=df_wrgld[var].value_counts().index, palette = colors)
    plt.title(f'{var} and Deposit')
    plt.xlabel(var)
    plt.show()

#### Numerical Variables
numerical_variables = ['age', 'balance', 'day', 'campaign', 'previous']

plt.figure(figsize=(20, 15), facecolor='white')

for i, feature in enumerate(numerical_variables, 1):
    plt.subplot(2, 3, i)
    
    # Applica il logaritmo solo alla variabile 'balance'
    if feature == 'balance':
        sns.boxplot(x="y", y=np.log1p(df_wrgld[feature]), data=df_wrgld)
        plt.xlabel(f'log({feature})')
    else:
        sns.boxplot(x="y", y=df_wrgld[feature], data=df_wrgld)
        plt.xlabel(feature)

plt.tight_layout()
plt.show()



### DATA PREPARATION AND ENCODING

### PERFORMING ML ALGORITHMS
### Logistic Regression
### Decision tree
### Random forest
### XGBoost


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

X = df_wrgld.drop('y', axis=1)
y = df_wrgld['y']

#### Identifying Num e Cat columns
print(df_wrgld.columns.tolist())
numeric_features = ['age', 'balance', 'day', 'campaign', 'previous']
categorical_features = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

#### Encoding
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Modelli
logistic_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(random_state=42))
])

decision_tree_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(random_state=42))
])

random_forest_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=100, n_jobs = -1))
])


#### Models
models = {
    'Logistic Regression': logistic_model,
    'Decision Tree': decision_tree_model,
    'Random Forest': random_forest_model
}

#### Training
for model_name, model in models.items():
    print(f"\n{model_name}:\n")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    #### Model Diagnostic
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='yes')
    recall = recall_score(y_test, y_pred, pos_label='yes')
    f1 = f1_score(y_test, y_pred, pos_label='yes')

    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')



### FEATURE IMPORTANCE BASED ON FEATURE PERMUTATION
from sklearn.inspection import permutation_importance

rf_model = random_forest_model.fit(X_train, y_train)

result = permutation_importance(
    rf_model, X_test, y_test, n_repeats=2, random_state=42, n_jobs=-1, scoring = 'f1_micro'
)

feature_names = X.columns
forest_importances = pd.Series(result.importances_mean, index=feature_names)

forest_importances_sorted = forest_importances.sort_values(ascending=False)

fig, ax = plt.subplots()
forest_importances_sorted.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean f1 decrease")
fig.tight_layout()
plt.show()
