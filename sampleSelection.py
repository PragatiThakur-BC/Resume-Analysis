import os
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(os.path.join("Dataset", "job_descriptions.csv"))

class_counts = df['Job Title'].value_counts()
# print(class_counts)

print(len(df))
print("Before Sampling")
class_counts_percent = round((df['Job Title'].value_counts() / len(df)) * 100, 3)
print(class_counts_percent)
print(class_counts_percent.sum())


duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicate_rows)


#Sampling
total_samples = 50000
sample_counts = (class_counts / class_counts.sum() * total_samples).astype(int)

# Initialize an empty DataFrame to store the selected samples
selected_df = pd.DataFrame()

# Iterate over each class and randomly select samples
for class_label, count in sample_counts.items():
    class_samples = df[df['Job Title'] == class_label].sample(count, replace=True)
    selected_df = pd.concat([selected_df, class_samples])

# Shuffle the selected samples
selected_df = selected_df.sample(frac=1).reset_index(drop=True)

# Check if the folder for sample datasets exists, if not, create it
if not os.path.exists("SampleDataset"):
    os.makedirs("SampleDataset")

# Save selected_df as a new CSV file in the SampleDataset folder
selected_df.to_csv(os.path.join("SampleDataset", "sampleJD.csv"), index=False)

print("After Sampling")
class_counts_percent = round((selected_df['Job Title'].value_counts() / len(selected_df)) * 100, 3)
print(class_counts_percent)
print(class_counts_percent.sum())
