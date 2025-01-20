import pandas as pd
import random

# Generate roll numbers from 4101 to 4200
roll_numbers = list(range(4101, 4201))

# Generate random marks between 1 and 60 for each roll number
marks = [random.randint(1, 60) for _ in roll_numbers]

# Create a DataFrame
data = {'Roll Number': roll_numbers, 'Marks': marks}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('ESC.csv')

print("Sample dataset saved as 'Generated_Student_Marks.csv'")
