#Порахуйте, скільки разів хлопчиків називали Barbara
import pandas as pd

df = pd.read_csv("NationalNames.csv")
count_men = df[(df['Name'] == 'Barbara') & (df['Gender'] == 'M')]
total = count_men['Count'].sum()
print(total)