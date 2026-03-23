#Підрахуйте скільки років проводилось спостереження
import pandas as pd

df = pd.read_csv("NationalNames.csv")
start = df['Year'].min()
end = df['Year'].max()

long = end - start + 1 
print(f'Спостереження проводилось {long} років')