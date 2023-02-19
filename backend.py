import pandas as pd
import numpy as np
import csv

def top3(n):
    symptoms = ['cold', 'fever', 'sore throat', 'headache', 'stuffy nose', 'cough', 'diarrhea', 'nausea', 'constipation', 'stomach ache', 'earache', 'toothache', 'trouble breathing', 'skin irritation', 'muscle pain']
    user = []
    user_symptoms = user.append(str(n))
    for symptom in symptoms:
        if n in user:
            user.append(symptom)

    df = pd.read_csv('remedies3.csv').sort_values('rating', ascending=False)
    df2 = df[df['symptom'].isin([n])]
    df3 = df2.loc[df2['rating'] >= 4]
    df4 = df3.loc[df3['symptom'] == n].iloc[:1]

    df_filtered = df3.drop('symptom', axis=1).drop('rating', axis=1)

    rslt_df = df_filtered['recipe'].tolist()

    return rslt_df