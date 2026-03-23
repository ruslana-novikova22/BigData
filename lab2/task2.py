#Останні 8 рядків зі списку
import pandas as pd

df = pd.read_csv("NationalNames.csv")

print(df.tail(8))