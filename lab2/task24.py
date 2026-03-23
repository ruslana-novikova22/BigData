#Знайти найпопулярніше серед непопулярних імен (непопулярне ім’я, яким називали дітей найбільшу кількість разів)
import pandas as pd

df = pd.read_csv("NationalNames.csv")

name_totals = df.groupby('Name')['Count'].sum()
name_max_per_year = df.groupby('Name')['Count'].max()
rare_but_peaky = name_max_per_year[name_totals < 10].sort_values(ascending=False)

print(rare_but_peaky.head(5))                 