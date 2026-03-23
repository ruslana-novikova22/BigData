#Отримайте загальну інформацію про дані у наборі даних.
import pandas as pd

df = pd.read_csv("NationalNames.csv")
print(df[["Id", "Year", "Count"]].describe().to_string())