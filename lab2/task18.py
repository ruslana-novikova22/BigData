#Підрахуйте кількість років, коли дівчаток народжувалось більше, ніж хлопчиків.
import pandas as pd

df = pd.read_csv("NationalNames.csv")
a = df.groupby(['Year', 'Gender'])['Count'].sum().unstack()
b = a[a['F']>a['M']]
print(len(b))