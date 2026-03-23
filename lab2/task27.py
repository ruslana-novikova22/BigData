#Знайти найпопулярніші імена в кожному році.
import pandas as pd

df = pd.read_csv("NationalNames.csv")

sorted_df = df.sort_values(['Year', 'Count'], ascending=[True, False])

most_popular_per_year = sorted_df.drop_duplicates(subset='Year', keep='first')

result = most_popular_per_year[['Year', 'Name', 'Count']]

print(result) 