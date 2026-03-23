#Знайдіть загальну кількість народжень за рік.
import pandas as pd

df = pd.read_csv("NationalNames.csv")
print(df.groupby('Year')['Count'].sum().head())