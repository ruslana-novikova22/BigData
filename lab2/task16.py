#Знайдіть рік, коли народилося найбільше дітей
import pandas as pd

df = pd.read_csv("NationalNames.csv")
a = df.groupby('Year')['Count'].max().idxmax()
print(a)