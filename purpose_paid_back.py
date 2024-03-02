import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('loan_data.csv')

purpose_counts = df['purpose'].value_counts().sort_index()

paid_back_counts = df[df['not.fully.paid'] == True]['purpose'].value_counts().sort_index()

not_paid_back_counts = purpose_counts - paid_back_counts

plt.figure(figsize=(10, 8))
bar_width = 0.35

index = range(len(purpose_counts))
plt.bar(index, paid_back_counts, bar_width, label='Paid Back')
plt.bar(index, not_paid_back_counts, bar_width, bottom=paid_back_counts, label='Not Paid Back', alpha=0.5)

plt.xlabel('Purpose')
plt.ylabel('Count')
plt.title('Distribution of Purpose by Paid Back Status')
plt.xticks(index, purpose_counts.index, rotation=45)
plt.legend()

plt.tight_layout()
plt.show()