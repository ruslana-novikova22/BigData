#Підрахуйте кількість унікальних імен у кожному році
import pandas as pd

df = pd.read_csv("NationalNames.csv")
print(df.groupby('Year')['Name'].nunique())