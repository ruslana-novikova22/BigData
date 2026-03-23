#Знайдіть 5 найпопулярніших чоловічих імен у 2010 році
import pandas as pd

df = pd.read_csv("NationalNames.csv")
men_df = df[(df['Gender'] == 'M') & (df['Year'] == 2010)]
top_5 = men_df.sort_values(by='Count', ascending=False).head(5)
print(top_5)