#Обчисліть кількість унікальних жіночих та чоловічих імен у цілому наборі даних
import pandas as pd

df = pd.read_csv("NationalNames.csv")
print(df.groupby('Gender')['Name'].nunique())