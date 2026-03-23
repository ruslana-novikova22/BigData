#Знати найпопулярніші гендерно-нейтральні імена (ті, що присутні кожного року)
import pandas as pd

df = pd.read_csv("NationalNames.csv") 
name_entries_count = df.groupby('Name').size()
min_entries = name_entries_count.min()
unpopular_names_list = name_entries_count[name_entries_count == min_entries].index
top_unpopular = df[df['Name'].isin(unpopular_names_list)].groupby('Name')['Count'].sum().idxmax()
top_unpopular_value = df[df['Name'].isin(unpopular_names_list)].groupby('Name')['Count'].sum().max()

print(f"Наиболее популярное из непопулярных имен - это {top_unpopular}. Им называли {top_unpopular_value} раз") 