#Підрахуйте кількість гендерно-нейтральних імен (однакових для дівчат та хлопців)
import pandas as pd

df = pd.read_csv("NationalNames.csv")
count = df.groupby('Name')['Gender'].nunique()
print(len(count[count == 2]))