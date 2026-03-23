#Знайдіть кількість дівчаток та хлопчиків, які народились кожного року
import pandas as pd

df = pd.read_csv("NationalNames.csv")
print(df.groupby(['Year', 'Gender'])['Count'].sum())