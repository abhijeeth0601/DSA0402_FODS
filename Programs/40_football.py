import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = pd.read_csv('CSV_FILES/FOOTBALL.csv')
c = a.sort_values(by='no_of_goals', ascending=False)
print(f"The top 5 player with high goal : \n{c.head()}")

s = a.sort_values(by='salary', ascending=False)
print(f"High paid players: \n {s.head()}")

m = int(np.mean(a['age']))

x = a[a['age'] > m]
print(f"average age of players: \n{x}")

# z = ['LW', 'RW', 'ST', 'CAM', 'CDM', 'CM', 'CB', 'LB', 'RB', 'GK']
pc = a['position '].value_counts()
plt.figure(figsize=(8, 6))
pc.plot(kind='bar')
plt.xlabel('position')
plt.ylabel('no of player')
plt.title('distribution of players based on their positions')
# plt.bar(z, pc)
plt.show()
