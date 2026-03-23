#Підрахуйте кількість записів, для яких Count - мінімальне у наборі.
import pandas as pd

df = pd.read_csv("NationalNames.csv")
min = df['Count'].min()

min_records = len(df[df['Count'] == min])
print(min_records)