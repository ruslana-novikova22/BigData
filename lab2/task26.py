#Побудувати графіки розподілення кількості жіночих імен John та чоловічих імен Mary по роках.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NationalNames.csv")

girls = df[(df['Name'] == 'John') & (df['Gender'] == 'F')]
boys = df[(df['Name'] == 'Mary') & (df['Gender'] == 'M')]

john_girls = girls.groupby('Year')['Count'].sum().rename('John (F)')
mary_boys = boys.groupby('Year')['Count'].sum().rename('Mary (M)')

combined_df = pd.concat([john_girls, mary_boys], axis=1)

combined_df.plot(figsize=(10, 6), marker='.')

plt.title('Кількість імен John(F) та Mary(M) по роках')
plt.xlabel('Рік')
plt.ylabel('Кількість дітей')
plt.grid(True)
plt.legend()
plt.show()    