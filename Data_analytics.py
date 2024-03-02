import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
loan_data = pd.read_csv('loan_data.csv')

# Handle the data
loan_data['fico'] = pd.to_numeric(loan_data['fico'])
loan_data['purpose'] = loan_data['purpose'].astype('category')

# Visualize FICO scores
plt.figure(figsize=(10, 6))
plt.hist(loan_data['fico'], bins=30, edgecolor='black')
plt.title('Histogram of FICO Scores')
plt.xlabel('FICO Score')
plt.ylabel('Count')
plt.show()

# Visualize loan purposes
loan_purpose_counts = loan_data['purpose'].value_counts()
plt.figure(figsize=(10, 6))
loan_purpose_counts.plot(kind='bar')
plt.title('Bar Plot of Loan Purposes')
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.show()