import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('loan_data.csv')

purpose_counts = df['purpose'].value_counts()

plt.figure(figsize=(10, 8))
plt.pie(purpose_counts, labels=purpose_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Purpose')
plt.show()