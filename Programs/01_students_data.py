
import numpy as np
import pandas as pd

students = pd.read_csv("CSV_FILES/Book1.csv")
avg = np.mean(students, axis=0)
highest_avg_subject_index = np.argmax(avg)
subjects = ['Math', 'Science', 'English', 'History']
highest_average_subject = subjects[highest_avg_subject_index]

print(f"\n\nThe average scores for each subject are:\n {avg}")
print(
    f"\nThe subject with the highest average score is: {highest_average_subject}")
print("\n")

data = {
    'Maths': [95, 87, 89, 64],
    'Science': [99, 88, 77, 66],
    'English': [87, 76, 65, 98],
    'History': [56, 67, 78, 89]
}

df = pd.DataFrame(data)

arr = df.to_numpy()
arr.shape = (4, 4)
print(arr)
