import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'fat_percentage': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4,
                       27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}
df = pd.DataFrame(data)
print(df)

print(df.mean(), "\n", df.median(), "\n", df.std())


plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['age', 'fat_percentage']])
plt.title("Boxplots of Age and Fat Percentage")
plt.xlabel("Variable")
plt.ylabel("Value")
plt.show()

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['fat_percentage'])
plt.title("Scatter Plot of Age vs Fat Percentage")
plt.xlabel("Age")
plt.ylabel("Fat Percentage")
plt.show()


# Create Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['fat_percentage'], dist="norm", plot=plt)
plt.title("Q-Q Plot of Fat Percentage")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()
