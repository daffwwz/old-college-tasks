import pandas as pd

# Define the file path
file_path = 'output_0065.prof'

try:
    with open(file_path, 'r') as file:
        text_data = file.readlines()
except Exception as e:
    print(f"Failed to read.prof file: {e}")
    exit()

# Split the text data into columns
data = [line.split() for line in text_data]

rows = []
for row in data:
    if len(row) == 1:
        rows.append([row[0]])
    else:
        rows.append(row)

# Create a Pandas DataFrame
df = pd.DataFrame(rows, columns=['particle', 'x', 'y', 'z', 'u', 'v', 'w', 'temp', 'pres'])

# Add a new column with the first row and column value
df['time'] = df.iloc[0, 0]

# Move the new column to the first position
df.insert(0, 'time', df.pop('time'))

# Extract the first row with a value of 0
filtered_df = df[df['particle'] == '0']

# Write the filtered DataFrame to a CSV file
filtered_df.to_csv('salt3_65.csv', index=False)
