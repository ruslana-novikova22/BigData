#Побудувати графіки розподілення кількості імен John та Mary по роках без залежності до статі.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NationalNames.csv")

filtered_df = df[df['Name'].isin(['John', 'Mary'])]

chart_data = filtered_df.groupby(['Year', 'Name'])['Count'].sum().unstack()

chart_data.plot(figsize=(10, 6), marker='o')

plt.title('Розподіл популярності імен John та Mary по роках')
plt.xlabel('Рік')
plt.ylabel('Кількість')
plt.grid(True)
plt.show()               